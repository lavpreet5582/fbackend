from typing import List, Union
from xmlrpc.client import Boolean

from pydantic import BaseModel


class ItemBase(BaseModel):
    title: str
    description: Union[str, None] = None
    is_done:bool = False
    is_in_progress:bool = False


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    items: List[Item] = []

    class Config:
        orm_mode = True
