from .models import User
from rest_framework import serializers


class PhoneSerializer(serializers.Serializer):
    phone = serializers.CharField()

class CodeVerifySerializer(serializers.Serializer):
    phone = serializers.CharField()
    code = serializers.CharField()

class InviteCodeSerializer(serializers.Serializer):
    invite_code = serializers.CharField()

class UserProfileSerializer(serializers.ModelSerializer):
    referrals = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ['phone', 'invite_code', 'activated_invite_id', 'referrals']

    def get_referrals(self, obj):
        return [u.phone for u in obj.referrals.all()]