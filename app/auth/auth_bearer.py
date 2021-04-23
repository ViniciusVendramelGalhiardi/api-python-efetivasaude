from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from .auth_handler import decodeJWT
from app.model.response import Response, getResponse
from fastapi.responses import JSONResponse

class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(JWTBearer, self).__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                response = getResponse(403, "Invalid authentication scheme.", "")
                raise HTTPException(status_code=403, detail=response.__dict__)
            if not self.verify_jwt(credentials.credentials):
                response = getResponse(403, "Invalid authentication scheme.", "")
                raise HTTPException(status_code=403, detail=response.__dict__)
            return credentials.credentials
        else:
            response = getResponse(403, "Invalid authorization code.", "")
            raise HTTPException(status_code=403, detail=response.__dict__)

    def verify_jwt(self, jwtoken: str) -> bool:
        isTokenValid: bool = False

        try:
            payload = decodeJWT(jwtoken)
        except:
            payload = None
        if payload:
            isTokenValid = True
        return isTokenValid 