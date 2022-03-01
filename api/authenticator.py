from fastapi import Depends, HTTPException
from fastapi.security import HTTPBasicCredentials, HTTPBearer

from modules.models.models import env

security = HTTPBearer()


async def offline_has_access(token: HTTPBasicCredentials = Depends(security)) -> None:
    """Validates the token if mentioned as a dependency.

    Args:
        token: Takes the authorization header token as an argument.
    """
    auth = token.dict().get('credentials')
    if auth.startswith('\\'):
        auth = bytes(auth, "utf-8").decode(encoding="unicode_escape")
    if auth == env.offline_pass:
        return
    raise HTTPException(status_code=403, detail='Request not authorized.')


async def robinhood_has_access(token: HTTPBasicCredentials = Depends(security)) -> None:
    """Validates the token if mentioned as a dependency.

    Args:
        token: Takes the authorization header token as an argument.
    """
    auth = token.dict().get('credentials')
    if auth.startswith('\\'):
        auth = bytes(auth, "utf-8").decode(encoding="unicode_escape")
    if auth == env.robinhood_endpoint_auth:
        return
    raise HTTPException(status_code=403, detail='Request not authorized.')