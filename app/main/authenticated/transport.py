from fastapi_users.authentication import CookieTransport, AuthenticationBackend

from .strategy import get_jwt_strategy

cookie_transport = CookieTransport(
    cookie_name="MyFinance",
    cookie_max_age=3600
)

auth_backend = AuthenticationBackend(
    name="jwt",
    transport=cookie_transport,
    get_strategy=get_jwt_strategy
)