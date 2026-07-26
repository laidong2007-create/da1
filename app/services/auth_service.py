from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.user_repository import UserRepository
from app.core.security import hash_password, verify_password, create_access_token
from app.schemas.auth import UserCreate

class AuthService:
    def __init__(self, db: AsyncSession):
        self.repo = UserRepository(db)

    async def register(self, user_in: UserCreate):
        hashed_pwd = hash_password(user_in.password)
        from app.models.user import User
        user = User(username=user_in.username, email=user_in.email, hashed_password=hashed_pwd)
        return await self.repo.create(user)

    async def authenticate(self, username: str, password: str):
        user = await self.repo.get_by_username(username)
        if not user or not verify_password(password, user.hashed_password):
            return None
        return create_access_token({"sub": user.username})