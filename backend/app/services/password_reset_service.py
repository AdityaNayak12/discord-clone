from datetime import datetime, timedelta
import secrets
from sqlalchemy.orm import Session
from app.models.password_reset_token import PasswordResetToken
from app.models.users import User

RESET_TOKEN_EXPIRE_HOURS = 1

def create_password_reset_token(db: Session, user: User) -> PasswordResetToken:
    token = secrets.token_urlsafe(32)
    expires_at = datetime.utcnow() + timedelta(hours=RESET_TOKEN_EXPIRE_HOURS)
    reset_token = PasswordResetToken(user_id=user.id, token=token, expires_at=expires_at)
    db.add(reset_token)
    db.commit()
    db.refresh(reset_token)
    return reset_token

def verify_password_reset_token(db: Session, token: str) -> User | None:
    reset_token = db.query(PasswordResetToken).filter_by(token=token).first()
    if not reset_token or reset_token.expires_at < datetime.utcnow():
        return None
    user = db.query(User).filter_by(id=reset_token.user_id).first()
    return user

def delete_password_reset_token(db: Session, token: str):
    db.query(PasswordResetToken).filter_by(token=token).delete()
    db.commit()
