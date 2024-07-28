from app.config.repository.base import BaseDAO

from .models import Role


class RoleDAO(BaseDAO):
    model = Role
