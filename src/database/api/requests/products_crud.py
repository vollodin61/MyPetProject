import logging

from icecream import ic
from fastapi import APIRouter, Depends
from loguru import logger
from sqlalchemy import update, select, text

from src.database.api.config.dependencies import UOWDep
from src.database.api.schemas.product_schemas import PydCreateProduct
from src.database.api.services.product_services import ProductsService

from src.logs.my_ice import ice

logging.basicConfig(level=logging.DEBUG)
product_router = APIRouter(
    prefix='/products',
    tags=['Products']
)


@product_router.get("/one/{product_id}")
async def get_product_by_id(uow: UOWDep, product_id: int):
    product = await ProductsService().get_product(uow=uow, product_id=product_id)
    return product


@product_router.post("/create")
async def post_from_tilda(uow: UOWDep, product: PydCreateProduct):
    product_id = await ProductsService().add_product(uow, product)
    return {"product_id": product_id}
