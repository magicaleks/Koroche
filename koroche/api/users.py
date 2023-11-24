from fastapi import APIRouter, Response
from koroche.api.validation.user import CreateUser, DeleteUser, UpdateUser
from koroche.user.manager import UserManager
from koroche.user.model import User

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/get/uid/{uid}", response_model=User, response_description="Get user by it's uid")
def get_user_by_uid(uid: str):
    """Get user"""

    user = UserManager.get(uid=uid)

    return user if user else Response(status_code=404)


@router.get("/get/email/{email}", response_model=User, response_description="Get user by it's email")
def get_user_by_email(email: str):
    """Get user"""

    user = UserManager.get(email=email)

    return user if user else Response(status_code=404)


@router.post("/create", response_model=User, response_description="Create user")
def create_user(schema: CreateUser):
    """Create user"""

    user = UserManager.create(name=schema.name, email=schema.email, password=schema.password, locale=schema.locale)

    return user


@router.post("/update", response_description="Update user")
def update_user(schema: UpdateUser):
    """Update user"""

    UserManager.update(schema.uid, schema.update)

    return Response()


@router.post("/delete", response_description="Delete user")
def delete_user(schema: DeleteUser):
    """Delete user"""

    UserManager.delete(schema.uid)

    return Response()
