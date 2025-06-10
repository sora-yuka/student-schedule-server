from typing import Optional, Tuple, Any
from django.contrib.auth import get_user_model
from rest_framework.request import Request
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import AccessToken


User = get_user_model()


class CookiesJWTAuthentication(JWTAuthentication):
    def authenticate(self, request: Request) -> Optional[Tuple[User, AccessToken]]:
        access_token = request.COOKIES.get("access_token")
        
        if not access_token:
            return None
        validated_token = self.get_validated_token(raw_token=access_token)
        
        try:
            user = self.get_user(validated_token=validated_token)
        except AuthenticationFailed as error:
            # logger will be soon
            print("Error during auth: ", error)
        
        return (user, validated_token)