from fastapi import APIRouter, Depends
from app.api.deps import get_current_user
from app.models.users import User
from app.schemas.user_schemas import UserResponse

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/me", response_model=UserResponse)
def get_current_user_info(current_user: User = Depends(get_current_user)):
    """
    Get current authenticated user information.
    
    This endpoint requires JWT authentication via Bearer token.
    It serves as the template for all future permission checks.

    Args:
        current_user: Current authenticated user (injected via JWT dependency)
        
    Returns:
        Current user information (id, email, username, created_at)
        
    Raises:
        HTTPException 401: If token is invalid, expired, or user not found
        
    Example:
        Headers: Authorization: Bearer <your_jwt_token>
        Response: {
            "id": 1,
            "email": "user@example.com",
            "username": "johndoe",
            "created_at": "2026-02-12T10:30:00"
        }
    """
    return UserResponse.model_validate(current_user)
