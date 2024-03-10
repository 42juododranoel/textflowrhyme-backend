from textflowrhyme.apps.users.utils.fastapi_users import fastapi_users

check_unverified = fastapi_users.current_user(active=True)
check_verified = fastapi_users.current_user(active=True, verified=True)
check_superuser = fastapi_users.current_user(active=True, verified=True, superuser=True)
