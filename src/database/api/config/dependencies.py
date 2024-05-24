from typing import Annotated

from fastapi import Depends

from src.database.api.utils.unitofwork import IUnitOfWork, UnitOfWork

UOWDep = Annotated[IUnitOfWork, Depends(UnitOfWork)]
