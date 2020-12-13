from fastapi import APIRouter, Depends

from services.foo import FooService
from schemas.foo import FooItem, FooItemCreate

from utils.service_result import handle_result

from config.database import get_db

router = APIRouter(
    prefix="/foo",
    tags=["items"],
    responses={404: {"description": "Not found"}},
)


@router.post("/item/", response_model=FooItem)
async def create_item(item: FooItemCreate, db: get_db = Depends()):
    result = FooService(db).create_item(item)
    return handle_result(result)


@router.get("/item/{item_id}", response_model=FooItem)
async def get_item(item_id: int, db: get_db = Depends()):
    result = FooService(db).get_item(item_id)
    return handle_result(result)
