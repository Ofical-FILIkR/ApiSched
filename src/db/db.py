from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

from dotenv import dotenv_values

configs = dotenv_values(".env")


engine = create_async_engine(f"postgresql+psycopg://{configs['USER_DB']}:{configs['PASSWORD_DB']}@{configs['HOST_DB']}:{configs['PORT_DB']}/{configs['NAME_DB']}")
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


class Base(DeclarativeBase):
    pass


async def get_async_session():
    async with async_session_maker() as session:
        yield session
