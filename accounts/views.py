import time
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework.views import APIView
import random
import string
from accounts.models import User
from accounts.serializers import PhoneSerializer, CodeVerifySerializer, UserProfileSerializer, InviteCodeSerializer

fake_verification_codes = {}
def get_random_code():
    return ''.join(random.choices(string.digits, k=4))

class RequestCodeView(APIView):
    @swagger_auto_schema(request_body=PhoneSerializer)
    def post(self, request):
        serializer = PhoneSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        phone = serializer.validated_data['phone']
        code = get_random_code()
        fake_verification_codes[phone] = code

        time.sleep(2)
        return Response({'detail': f'Code sent to {phone} Code: {code}'})

class VerifyCodeView(APIView):
    @swagger_auto_schema(request_body=CodeVerifySerializer)
    def post(self, request):
        serializer = CodeVerifySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        phone = serializer.validated_data['phone']
        code = serializer.validated_data['code']
        if fake_verification_codes.get(phone) != code:
            return Response({'detail': 'Invalid code'}, status=400)
        user, created = User.objects.get_or_create(phone=phone)
        user.is_verified = True
        user.save()
        return Response({'detail': 'Verified successfully'})

class UserProfileView(APIView):
    @swagger_auto_schema(manual_parameters=[openapi.Parameter('phone', openapi.IN_QUERY, description='Phone number', type=openapi.TYPE_STRING)])
    def get(self, request):
        phone = request.query_params.get('phone', '').strip()
        try:
            user = User.objects.get(phone=phone, is_verified=True)
        except User.DoesNotExist:
            return Response({'detail': 'User not found or not verified'}, status=404)
        serializer = UserProfileSerializer(user)
        return Response(serializer.data)

class ActivateInviteView(APIView):
    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['phone', 'invite_code'],
            properties={
                'phone': openapi.Schema(type=openapi.TYPE_STRING, example='+79001234567'),
                'invite_code': openapi.Schema(type=openapi.TYPE_STRING, example='A1B2C3')
            }))
    def post(self, request):
        phone = request.data.get('phone')
        invite_code = request.data.get('invite_code')
        try:
            user = User.objects.get(phone=phone, is_verified=True)
        except User.DoesNotExist:
            return Response({'detail': 'User not found'}, status=404)
        if user.activated_invite:
            return Response({'detail': 'Invite code already used'}, status=400)
        try:
            inviter = User.objects.get(invite_code=invite_code)
        except User.DoesNotExist:
            return Response({'detail': 'Invalid invite code'}, status=400)
        if inviter == user:
            return Response({'detail': 'Cannot use your own invite code'}, status=400)
        user.activated_invite = inviter
        user.save()
        return Response({'detail': 'Invite activated'})