from fastapi import APIRouter, Depends
from fastapi_pagination import Page
from sqlalchemy.orm import Session
from src.core.db.db_base import get_async_session
from src.core.domain.custom_response import CommonResponse
from src.core.domain.constant import ResponseCode, ResponseMessage
from .schemas import CreateUserParams, CreateUser, ListUser, CreateUserResponse
from .service import service_create_user, service_query_user_list

router = APIRouter()


@router.post("/", response_model=CommonResponse[CreateUser])
# @router.post("/", response_model=CreateUser)
async def create_user(
        create_user_params: CreateUserParams,
        db: Session = Depends(get_async_session)
):
    """
    接口层
    :param create_user_params:
    :param db:
    :return:
    """
    name = create_user_params.name
    age = create_user_params.age
    print(f'name:{name}')
    print(f'age:{age}')

    user = await service_create_user(db, create_user_params.name, create_user_params.age)
    return CommonResponse(data=user, code=ResponseCode.create_success, message=ResponseMessage.create_success)


@router.get("/", response_model=Page[ListUser])
async def query_user_list(
        db: Session = Depends(get_async_session)
):
    """
    接口层
    :param db:
    :return:
    """

    user_list = await service_query_user_list(db)
    print(f'user_list:{user_list}')
    return user_list
