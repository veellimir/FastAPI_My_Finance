from sqlalchemy.orm import DeclarativeBase, declared_attr
from sqlalchemy import MetaData
from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.config.project_config import settings
from app.utils.convertor import camel_case_to_snake_case


class Base(DeclarativeBase):
    metadata = MetaData(
        naming_convention=settings.db.naming_convention,
    )

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return camel_case_to_snake_case(cls.__name__)


class BaseDAO:
    model = None

    @classmethod
    async def find_all(cls, session: AsyncSession, **filter_by):
        query = select(cls.model).filter_by(**filter_by)
        result = await session.execute(query)
        return result.scalars().all()

    @classmethod
    async def add(cls, session: AsyncSession, **data):
        query = insert(cls.model).values(**data)
        await session.execute(query)
        await session.commit()