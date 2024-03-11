from pydantic import BaseModel, EmailStr, Field
from uuid import UUID


class CreateUserParams(BaseModel):
    name: str = Field(min_length=1, max_length=20)
    age: int = Field(gt=0, le=100)


class CreateUser(BaseModel):
    id: int
    name: str
    age: int
    uuid: UUID | None = None
    email: str | None = None
    organization_id: int | None = None


class CreateUserResponse(BaseModel):
    data: CreateUser
    code: int = 200


class ListUser(BaseModel):
    id: int
    name: str
    age: int
    uuid: UUID | None = None
    email: str | None = None
    organization_id: int | None = None
