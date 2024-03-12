import time

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from fastapi_pagination.ext.sqlalchemy import paginate
from .models import User


async def db_create_user(db: AsyncSession, name: str, age: int) -> User:
    """
    数据层
    :param db:
    :param name:
    :param age:
    :return:
    """
    user = User(name=name, age=age)
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user


async def db_query_user_list(db: AsyncSession) -> list[User]:
    sql = select(User)
    user_list = await paginate(db, sql)
    return user_list



