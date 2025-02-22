from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

async_engine = create_async_engine(
    url="postgresql+asyncpg://postgres:1234@db:5432/dockerDB"
)
# async_engine = create_async_engine(
#     url="postgresql+asyncpg://postgres:1234@localhost:5432/dockerDB"
# )

AsyncSessionMaker = async_sessionmaker(bind=async_engine, expire_on_commit=False)


async def get_db():
    async with AsyncSessionMaker() as session:
        return session


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30))
    description = Column(String)
