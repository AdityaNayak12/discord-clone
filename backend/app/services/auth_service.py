from app.models.users import User
from sqlalchemy.orm import Session
from app.core.security import get_password_hash

def get_user_by_email(db: Session, email: str) -> User | None:
    return db.query(User).filter_by(email=email).first()

def update_user_password(db: Session, user: User, new_password: str):
    user.hashed_password = get_password_hash(new_password)
    db.add(user)
    db.commit()
    db.refresh(user)
