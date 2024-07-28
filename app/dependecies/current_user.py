from fastapi import Depends

from app.main.users.current_user import current_user

dependencies_current_user = Depends(current_user)
