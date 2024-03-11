from pydantic import BaseModel
from typing import Generic, TypeVar

T = TypeVar('T')


class CommonResponse(BaseModel, Generic[T]):
    """
    自定义响应体结构
    """
    code: int
    message: str | None = None
    data: T
