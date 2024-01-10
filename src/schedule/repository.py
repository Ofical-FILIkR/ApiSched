import json
from abc import ABC, abstractmethod

import requests
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.data_type import url_api_template
from src.schedule.model import ScheduleModel
from src.schedule.scheme import JSONScheduleScheme


class ScheduleRepository(ABC):
    @abstractmethod
    async def convert_schedule(self, data):
        NotImplementedError

    @abstractmethod
    async def get_data_schedule(self, data: str):
        NotImplementedError

    @abstractmethod
    async def get_all_pairs(self, data):
        NotImplementedError


class ScheduleRepositoryImpl(ScheduleRepository):
    model = ScheduleModel

    def __init__(self, session: AsyncSession):
        self.session = session

    async def convert_schedule(self, data):
        pairs = []
        for pair in data:
            pairs.append(JSONScheduleScheme(
                discipline=pair["дисциплина"],
                group=pair["группа"],
                auditorium=pair["аудитория"],
                teacher=pair["преподаватель"],
                lesson_number=pair["номерЗанятия"],
                day_of_week=pair["деньНедели"],
                number_of_week=pair["типНедели"],
                date=pair["дата"],
                start=pair["начало"],
                finish=pair["конец"]
            ))
        return pairs

    async def get_data_schedule(self, data: str):
        stmt = select(self.model).filter_by(data=data.upper())
        res = await self.session.execute(stmt)
        pairs = res.first()
        if pairs is None: return {
            "state": "error",
            "msg": "no data found"
        }
        return {
            "state": "ok",
            "data": pairs[0]
        }

    async def get_all_pairs(self, data):
        url = url_api_template.format(
            type_schedule=data.type_schedule,
            id=data.api_key
        )
        schedule = json.loads(requests.get(url).text)
        if schedule['state'] == '-1': return {
            "state": "error",
            "msg": schedule["msg"]
        }
        return {
            "state": "ok",
            "schedule": schedule['data']['rasp']
        }

    async def get_one_weak(self, data, num_weak):
        pairs = []
        for pair in data:
            if pair["типНедели"] == num_weak:
                pairs.append(pair)
        return pairs

    async def get_one_day(self, data, num_day):
        pairs = []
        for pair in data:
            if pair["деньНедели"] == num_day:
                pairs.append(pair)
        return pairs

