from fastapi_users import schemas


class SchemUserRead(schemas.BaseUser[int]):
    role_id: int


class SchemUserCreate(schemas.BaseUserCreate):
    role_id: int


class SchemUserUpdate(schemas.BaseUserUpdate):
    pass
