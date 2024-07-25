from fastapi import FastAPI

from app.config.lifespan import lifespan

app = FastAPI(
    lifespan=lifespan
)