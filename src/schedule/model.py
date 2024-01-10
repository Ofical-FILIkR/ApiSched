from pydantic import BaseModel
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.data_type import DayNum
from src.db.db import Base
from src.schedule.scheme import ScheduleScheme


class CoupleScheme(BaseModel):
    name: str
    teacher: str
    group: str
    audience: str
    num: int
    day: DayNum


class ScheduleModel(Base):
    __tablename__ = "api_keys"

    id: Mapped[int] = mapped_column(primary_key=True)
    type_schedule: Mapped[int] = mapped_column(ForeignKey("types_schedule.id"))
    data: Mapped[str]
    api_key: Mapped[int]

    def to_read_model(self) -> ScheduleScheme:
        return ScheduleScheme(
            id=self.id,
            data=self.data,
            api_key=self.api_key
        )

