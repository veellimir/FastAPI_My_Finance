from fastapi_users.authentication import JWTStrategy

from app.config.project_config import settings


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=settings.secret, lifetime_seconds=settings.lifetime)