from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel, EmailStr
from app.database.sessions import get_db
from app.models.users import User
from app.services.password_reset_service import (
    create_password_reset_token, verify_password_reset_token, delete_password_reset_token
)
from app.services.auth_service import get_user_by_email, update_user_password
from app.utils.email_utils import send_email

router = APIRouter(prefix="/password-reset", tags=["password-reset"])

class PasswordResetRequest(BaseModel):
    email: EmailStr

class PasswordResetConfirm(BaseModel):
    token: str
    new_password: str

@router.post("/request")
def request_password_reset(data: PasswordResetRequest, db: Session = Depends(get_db)):
    user = get_user_by_email(db, data.email)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    reset_token = create_password_reset_token(db, user)
    # Send reset token via email
    reset_link = f"https://your-frontend-url/reset-password?token={reset_token.token}"
    subject = "Password Reset Request"
    body = f"Hello,\n\nTo reset your password, click the following link: {reset_link}\nIf you did not request this, please ignore this email."
    error = send_email(user.email, subject, body)
    if error:
        raise HTTPException(status_code=500, detail=f"Failed to send email: {error}")
    return {"msg": "Password reset email sent"}

@router.post("/confirm")
def confirm_password_reset(data: PasswordResetConfirm, db: Session = Depends(get_db)):
    user = verify_password_reset_token(db, data.token)
    if not user:
        raise HTTPException(status_code=400, detail="Invalid or expired token")
    update_user_password(db, user, data.new_password)
    delete_password_reset_token(db, data.token)
    return {"msg": "Password updated successfully"}
