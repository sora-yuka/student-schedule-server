import jwt
from typing import Any, Dict, Optional, Union
from jwt.exceptions import InvalidTokenError, ExpiredSignatureError
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.request import Request
from django.conf import settings
from django.contrib.auth import get_user_model
from channels.db import database_sync_to_async
from datetime import datetime, timedelta, timezone


User = get_user_model()


class JWTAuthentication(BaseAuthentication):
    def authenticate(self, request: Request) -> Optional[User]:
        pass
    
    def verify_token(self, payload: Dict[str, Union[str, int]]) -> None:        
        if "exp" not in payload:
            raise InvalidTokenError("Token has no expiry date")
        
        exp_timestamp = payload["exp"]
        current_timestamp = datetime.utcnow().timestamp()
        
        if current_timestamp > exp_timestamp:
            raise ExpiredSignatureError("Token has expired")
        
    @database_sync_to_async
    def authenticate_websocket(self, scope: Dict[str, Any], token: str) -> Optional[User]:
        try:
            payload = jwt.decode(jwt=token, key=settings.SECRET_KEY, algorithms=["HS256"])
            self.verify_token(payload=payload)
            user = User.objects.get(id=payload["user_id"])
            return user
        except (InvalidTokenError, ExpiredSignatureError, User.DoesNotExist):
            raise AuthenticationFailed("Error occured while validating token")