from pydantic import BaseModel


class FooItemBase(BaseModel):
    description: str


class FooItemCreate(FooItemBase):
    public: bool


class FooItem(FooItemBase):
    id: int

    class Config:
        orm_mode = True
