from pydantic import BaseModel, EmailStr, Field
from datetime import datetime


class UserRegister(BaseModel):
    """Schema for user registration"""
    email: EmailStr = Field(..., description="User's email address")
    username: str = Field(..., min_length=3, max_length=32, description="Username (3-32 characters)")
    password: str = Field(..., min_length=6, description="Password (minimum 6 characters)")


class UserLogin(BaseModel):
    """Schema for user login"""
    email: EmailStr = Field(..., description="User's email address")
    password: str = Field(..., description="User's password")


class UserResponse(BaseModel):
    """Schema for user response (excludes password)"""
    id: int
    email: str
    username: str
    created_at: datetime

    class Config:
        from_attributes = True  # Allows ORM model conversion


class TokenResponse(BaseModel):
    """Schema for JWT token response"""
    access_token: str
    token_type: str = "bearer"
    user: UserResponse
