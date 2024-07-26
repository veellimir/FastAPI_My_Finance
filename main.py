from fastapi import FastAPI

from app.config.lifespan import lifespan
from app.main.authenticated.router import router as auth_router
from app.main.users.router import router as user_router


app = FastAPI(
    lifespan=lifespan
)


app.include_router(auth_router)
app.include_router(user_router)
