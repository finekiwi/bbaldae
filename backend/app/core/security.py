from datetime import datetime, timedelta, timezone

from jose import JWTError, jwt

from app.config import get_settings


def create_access_token(data: dict, expires_delta: timedelta | None = None) -> str:
    """Encode a JWT access token with the given payload and optional expiry."""
    settings = get_settings()
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + (
        expires_delta or timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM)


def decode_token(token: str) -> dict | None:
    """Decode and verify a JWT token. Returns the payload dict or None if invalid."""
    settings = get_settings()
    try:
        payload = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
        return payload
    except JWTError:
        return None
