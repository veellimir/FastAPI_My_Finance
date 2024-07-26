from fastapi import APIRouter, Depends

from app.main.users.current_user import current_user
from app.main.users.models import User
from app.main.users.schemas import SchemUserRead

router = APIRouter(
    prefix="/users",
    tags=["Пользователи"]
)


@router.get("/get_current_user", summary="получить текущего пользователя")
async def get_current_user(user: User = Depends(current_user)):
    return SchemUserRead(
        id=user.id,
        role_id=user.role_id,
        email=user.email,
        is_active=user.is_active,
        is_superuser=user.is_superuser,
        is_verified=user.is_verified
    )