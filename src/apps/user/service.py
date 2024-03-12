from sqlalchemy.ext.asyncio import AsyncSession
from .models import User
from .crud import db_create_user, db_query_user_list


async def service_create_user(db: AsyncSession, name: str, age: int) -> User:
    """
    业务逻辑层
    :param db:
    :param name:
    :param age:
    :return:
    """
    user = await db_create_user(db, name, age)
    return user


async def service_query_user_list(db: AsyncSession) -> list[User]:
    user_list = await db_query_user_list(db)
    return user_list


