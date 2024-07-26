from fastapi_users.db import SQLAlchemyBaseUserTable

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey

from app.config.repository.base import Base
from app.mixins.user_mixin import IntIdPkMixin


class User(Base, IntIdPkMixin, SQLAlchemyBaseUserTable[int]):
    role_id: Mapped[int] = mapped_column(ForeignKey("role.id", ondelete="cascade"), nullable=False)


class Role(Base, IntIdPkMixin):
    name: Mapped[str] = mapped_column(unique=True)
