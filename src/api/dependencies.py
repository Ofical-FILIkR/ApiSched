from typing import Annotated

from fastapi import Depends

from src.schedule.uow import IUnitOfWork, UnitOfWork

UOWDep = Annotated[IUnitOfWork, Depends(UnitOfWork)]
