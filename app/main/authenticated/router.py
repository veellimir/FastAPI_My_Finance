from fastapi import APIRouter
from fastapi_users import FastAPIUsers

from app.main.authenticated.user_manager import get_user_manager
from app.main.authenticated.transport import auth_backend

from app.main.users.models import User
from app.main.users.schemas import SchemUserCreate, SchemUserRead

router = APIRouter(tags=["Аутентификация"])

PREFIX = "/auth/user"

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend]
)

router.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix=PREFIX,
)

router.include_router(
    fastapi_users.get_register_router(SchemUserRead, SchemUserCreate),
    prefix=PREFIX,
)

# current_user = fastapi_users.current_user()