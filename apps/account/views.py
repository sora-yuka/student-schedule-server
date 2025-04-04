from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView


User = get_user_model()



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