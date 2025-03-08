from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework_simplejwt.views import (
    TokenObtainPairView as TokenObtain,
    TokenRefreshView as TokenRefresh
)


User = get_user_model()


class TokenObtainPairView(TokenObtain):
    def post(self, request: Request, *args, **kwargs) -> Response:
        try:
            token_response = super().post(request, *args, **kwargs)
            token_data = token_response.data
            
            access_token = token_data.get("access")
            refresh_token = token_data.get("refresh")
            
            response = Response(data={
                "MESSAGE": "Access is permitted",
                "ACCESS TOKEN": access_token,
            }, status=status.HTTP_200_OK)
            
            response.set_cookie(
                key="access_token",
                value=access_token,
                path="/",
                secure=True,
                httponly=True,
                samesite="Strict",
            )
            
            response.set_cookie(
                key="refresh_token",
                value=refresh_token,
                path="/",
                secure=True,
                httponly=True,
                samesite="Strict",
            )
            return response
        except Exception as error:
            # logger will be here soon
            return Response(data={
                "MESSAGE": "Access is denied",    
            }, status=status.HTTP_400_BAD_REQUEST)
            

class TokenRefreshView(TokenRefresh):
    def post(self, request: Request, *args, **kwargs) -> Response:
        try:
            refresh_token = request.COOKIES.get("refresh_token")
            request.data._mutable = True
            request.data["refresh"] = refresh_token
            
            token_response = super().post(request, *args, **kwargs)
            token_data = token_response.data
            
            access_token = token_data.get("access_token")
            
            response = Response(data={
                "MESSAGE": "Access is permitted",
            }, status=status.HTTP_200_OK)
            
            response.set_cookie(
                key="access_token",
                value=access_token,
                path="/",
                secure=True,
                httponly=True,
                samesite="Strict",
            )
        except Exception as error:
            # logger will be here soon
            return Response(data={
                "MESSAGE": "Token refresh failed",
            }, status=status.HTTP_400_BAD_REQUEST)
            

class UserLogoutView(APIView):
    def post(self, request: Request, *args, **kwargs) -> Response:
        response = Response(data={
            "MESSAGE": "Successfully logged out",
        }, status=status.HTTP_200_OK)
        
        response.delete_cookie(key="access_token", path="/", samesite="Strict")
        response.delete_cookie(key="refresh_token", path="/", samesite="Strict")
        return response


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