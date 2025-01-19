from channels.middleware import BaseMiddleware
from rest_framework.exceptions import AuthenticationFailed
from django.db import close_old_connections
from .authentication import JWTAuthentication

class JWTWebsocketMiddleware(BaseMiddleware):
    async def __call__(self, scope, receive, send):
        close_old_connections()
        
        headers = scope["headers"]
        token = None
        
        for header in headers:
            if header[0] == b"authorization" and header[1].startswith(b"Bearer "):
                token = header[1][7:].decode("utf-8")
        
        if token is None:
            await send({
                "type": "websocket.close",
                "close_code": 4000,
            })
        
        authentication = JWTAuthentication()
        
        try:
            user = await authentication.authenticate_websocket(scope, token)
            
            if user is not None:
                scope["user"] = user
            else:
                await send({
                    "type": "websocket.close",
                    "close_code": 4000,
                })
                
            return await super().__call__(scope, receive, send) 
            
        except AuthenticationFailed:
            await send({
                "type": "websocket.close",
                "close_code": 4002,
            })