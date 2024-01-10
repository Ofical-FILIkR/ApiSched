from enum import Enum


class ScheduleType(Enum):
    group = "group"
    teacher = "teacher"
    audience = "audience"


class DayNum(Enum):
    Monday = "1"
    Tuesday = "2"
    Wednesday = "3"
    Thursday = "4"
    Friday = "5"
    Saturday = "6"


url_api_template = "https://erp.pkgh.ru/api/Rasp?id{type_schedule}={id}"
