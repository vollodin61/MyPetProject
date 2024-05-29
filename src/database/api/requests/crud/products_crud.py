import logging

from fastapi import APIRouter

from src.database.api.config.dependencies import UOWDep
from src.database.api.schemas.product_schemas import PydCreateProduct, PydProductTypes, PydProductStatuses
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


@product_router.get("/several")
async def get_several_products(uow: UOWDep, name: str = None, product_type: PydProductTypes = None,
                               price: int = None, status: PydProductStatuses = None, description: str = None):
    pre_dict = {'name': name, "product_type": product_type, 'price': price, 'status': status, 'description': description}
    dct = {key: value for key, value in pre_dict.items()}
    products = await ProductsService().get_several_products(uow=uow, filter_by=dct)
    return products


@product_router.get("/get_all")
async def get_all_products(uow: UOWDep):
    products = await ProductsService().get_products(uow=uow)
    return products


@product_router.post("/create")
async def post_from_tilda(uow: UOWDep, product: PydCreateProduct):
    product_id = await ProductsService().add_product(uow, product)
    return {"status": "ok", "product_id": product_id, "details": "product successfully created!)!)"}


@product_router.post("/update_product")
async def update_product(uow: UOWDep, product: PydCreateProduct, id: int):
    product_id = await ProductsService().edit_product(uow=uow, product=product, product_id=id)
    return {"status": "ok", "product_id": product_id, "details": "product successfully updated!)!)"}
