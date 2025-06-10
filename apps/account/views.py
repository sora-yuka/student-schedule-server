from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError

from rest_framework_simplejwt.views import (
    TokenObtainPairView as TokenObtain,
    TokenRefreshView as TokenRefresh
)


User = get_user_model()


class TokenObtainPairView(TokenObtain):
    def post(self, request: Request, *args, **kwargs) -> Response:
        try:
            token_response = super().post(request=request, *args, **kwargs)
            token_data = token_response.data
            
            access_token = token_data.get("access")
            refresh_token = token_data.get("refresh")
            
            response = Response(data="Authorization successfull", status=status.HTTP_200_OK)
            
            response.set_cookie(
                key="access_token",
                value=access_token,
                path="/",
                secure=False,
                httponly=True,
                samesite="Lax"
            )
            
            response.set_cookie(
                key="refresh_token",
                value=refresh_token,
                path="/",
                secure=False,
                httponly=True,
                samesite="Lax"
            )
            
            return response
        except TokenError as error:
            raise InvalidToken(detail=error.args[0])
        
        
class TokenRefreshView(TokenRefresh):
    def post(self, request: Request, *args, **kwargs) -> Response:
        try:
            refresh_token = request.COOKIES.get("refresh_token")
            request.data._mutable = True
            request.data["refresh"] = refresh_token
            
            token_response = super().post(request=request, *args, **kwargs)
            token_data = token_response.data
            
            access_token = token_data.get("access")
            
            response = Response(data="Token refreshed", status=status.HTTP_200_OK)
            
            response.set_cookie(
                key="access_token",
                value=access_token,
                path="/",
                secure=False,
                httponly=True,
                samesite="Lax"
            )
            
            return response
        except TokenError as error:
            raise InvalidToken(detail=error.args[0])


class CheckAuthView(APIView):
    def get(self, request: Request, *args, **kwargs) -> Response:
        current_user = self.request.user
        
        if current_user.is_anonymous:
            return Response(data={
                "MESSAGE": "Unauthorized user",
            }, status=status.HTTP_401_UNAUTHORIZED)
            
        return Response(data={
            "MESSAGE": "Authorized user",
        }, status=status.HTTP_200_OK)