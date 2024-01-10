from pydantic import BaseModel

from src.data_type import ScheduleType


class ScheduleScheme(BaseModel):
    id: int
    type: ScheduleType = "group"
    data: str
    api_key: int


class JSONScheduleScheme(BaseModel):
    discipline: str
    group: str
    auditorium: str
    teacher: str
    lesson_number: int
    day_of_week: int
    number_of_week: int
    date: str
    start: str
    finish: str



class TypesScheduleScheme(BaseModel):
    id: int
    name_types_schedule: str
