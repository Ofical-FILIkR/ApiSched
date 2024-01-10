from fastapi import APIRouter

from src.api.dependencies import UOWDep
from src.data_type import ScheduleType
from src.schedule.service import ScheduleService

router = APIRouter(
    prefix="/day",
    tags=["day"],
)


@router.get("/all_pairs")
async def get_all_pairs(
    data: str,
    uow: UOWDep
):
    print(data)
    res = await ScheduleService().get_all_pairs(uow, data)
    return res


@router.get("/one_weak")
async def get_one_weak(
    num_weak: int,
    data: str,
    uow: UOWDep
):
    res = await ScheduleService().get_one_weak(uow, data, num_weak)
    return res


@router.get("/one_day")
async def get_one_day(
    num_weak: int,
    num_day: int,
    data: str,
    uow: UOWDep
):
    print(data)
    res = await ScheduleService().get_one_day(uow, data, num_weak, num_day)
    return res
