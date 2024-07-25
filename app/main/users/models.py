from sqlalchemy.orm import Mapped, mapped_column

from app.config.repository.base import Base
from app.mixins.user_mixin import IntIdPkMixin


class User(IntIdPkMixin, Base):
    username: Mapped[str] = mapped_column(unique=True)