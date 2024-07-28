from fastapi import Depends

from app.config.repository.database import db_helper

dependencies_async_session = Depends(db_helper.session_getter)
