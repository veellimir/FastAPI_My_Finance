from sqlalchemy.orm import DeclarativeBase, declared_attr
from sqlalchemy import MetaData

from app.config.project_config import settings
from app.utils.convertor import camel_case_to_snake_case


class Base(DeclarativeBase):
    metadata = MetaData(
        naming_convention=settings.db.naming_convention,
    )

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return camel_case_to_snake_case(cls.__name__)


