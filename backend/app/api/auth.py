from fastapi.security import OAuth2PasswordRequestForm
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.sessions import get_db
from app.services.auth_service import register_user, login_user

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/register")
def register(email: str, username: str, password: str, db: Session = Depends(get_db)):
    user = register_user(db, email, username, password)

    return {
        "message": "User registered successfully",
        "user_id": user.id,
        "email": user.email,
        "username": user.username
    }


@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    result = login_user(db, form_data.username, form_data.password)

    return {
        "access_token": result["access_token"],
        "token_type": result["token_type"]
    }
