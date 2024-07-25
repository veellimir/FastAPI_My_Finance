from contextlib import asynccontextmanager
from fastapi import FastAPI

from .repository.database import db_helper


@asynccontextmanager
async def lifespan(app: FastAPI):
    # start
    yield
    # down
    await db_helper.dispose()