from typing import Optional

from sqlalchemy.ext.asyncio import AsyncSession

from fastapi import Depends, Request
from fastapi_users import BaseUserManager, IntegerIDMixin
from fastapi_users.db import SQLAlchemyUserDatabase

from app.main.users.models import User
from app.config.project_config import settings
from app.config.repository.database import db_helper

SECRET_RESET = settings.secret_reset
SECRET_VERIFY = settings.secret_verify


class UserManager(IntegerIDMixin, BaseUserManager[User, int]):  # Update default role_id in BaseUserManager
    reset_password_token_secret = SECRET_RESET
    verification_token_secret = SECRET_VERIFY

    async def on_after_register(self, user: User, request: Optional[Request] = None):
        print(f"User {user.id} has registered.")

    async def on_after_forgot_password(
        self, user: User, token: str, request: Optional[Request] = None
    ):
        print(f"User {user.id} has forgot their password. Reset token: {token}")

    async def on_after_request_verify(
        self, user: User, token: str, request: Optional[Request] = None
    ):
        print(f"Verification requested for user {user.id}. Verification token: {token}")


async def get_user_db(session: AsyncSession = Depends(db_helper.session_getter)) -> AsyncSession:
    yield SQLAlchemyUserDatabase(session, User)


async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)
