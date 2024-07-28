from fastapi import APIRouter, HTTPException

from sqlalchemy.future import select

from app.dependecies.async_session import dependencies_async_session
from app.dependecies.current_user import dependencies_current_user

from app.main.users.dao import RoleDAO
from app.main.users.models import User, Role
from app.main.users.schemas import SchemUserRead

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


router = APIRouter(
    prefix="/users",
    tags=["Пользователи"]
)


@router.get("/get_current_user", summary="получить текущего пользователя")
async def get_current_user(user: User = dependencies_current_user):
    return SchemUserRead(
        id=user.id,
        role_id=user.role_id,
        email=user.email,
        is_active=user.is_active,
        is_superuser=user.is_superuser,
        is_verified=user.is_verified
    )


@router.post("/create_role", summary="создать роль пользователя")
async def create_user_role(name: str, session: "AsyncSession" = dependencies_async_session):
    try:
        async with session.begin():
            result = await session.execute(select(Role).where(Role.name == name))
            existing_role = result.scalars().first()

            if existing_role:
                raise HTTPException(status_code=400, detail="Роль уже существует!")

            await RoleDAO.add(session, name=name)
            return {"message": "Роль успешно создана"}
    except HTTPException as e:
        raise e


@router.get("/get_list_role", summary="получить список ролей пользователя")
async def get_all_roles(session: "AsyncSession" = dependencies_async_session):
    roles = await RoleDAO.find_all(session)
    return roles
