from src.schedule.uow import IUnitOfWork


class ScheduleService:
    async def get_all_pairs(
        self,
        uow: IUnitOfWork,
        data: str
    ):
        async with uow:
            schedule_data = await uow.schedules.get_data_schedule(data)
            if schedule_data["state"] == "error":
                return schedule_data
            schedule = await uow.schedules.get_all_pairs(schedule_data["data"])
            if schedule["state"] == "error":
                return schedule
            schedule = await uow.schedules.convert_schedule(schedule["schedule"])
            return schedule

    async def get_one_weak(
            self,
            uow: IUnitOfWork,
            data: str,
            num_weak: int
    ):
        async with uow:
            schedule_data = await uow.schedules.get_data_schedule(data)
            if schedule_data["state"] == "error":
                return schedule_data
            all_schedule = await uow.schedules.get_all_pairs(schedule_data["data"])
            if all_schedule["state"] == "error":
                return all_schedule
            schedule_one_weak = await uow.schedules.get_one_weak(all_schedule["schedule"], num_weak)
            schedule = await uow.schedules.convert_schedule(schedule_one_weak)
            return schedule

    async def get_one_day(
        self,
        uow: IUnitOfWork,
        data: str,
        num_weak: int,
        num_day: int
    ):
        async with uow:
            schedule_data = await uow.schedules.get_data_schedule(data)
            if schedule_data["state"] == "error":
                return schedule_data
            all_schedule = await uow.schedules.get_all_pairs(schedule_data["data"])
            if all_schedule["state"] == "error":
                return all_schedule
            schedule_one_weak = await uow.schedules.get_one_weak(all_schedule["schedule"], num_weak)
            schedule_one_day = await uow.schedules.get_one_day(schedule_one_weak, num_day)
            schedule = await uow.schedules.convert_schedule(schedule_one_day)
            return schedule

