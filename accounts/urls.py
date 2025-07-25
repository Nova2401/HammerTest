from django.urls import path
from .views import *

urlpatterns = [
    path('auth/request-code/', RequestCodeView.as_view()),
    path('auth/verify-code/', VerifyCodeView.as_view()),
    path('profile/', UserProfileView.as_view()),
    path('activate-invite/', ActivateInviteView.as_view()),
]