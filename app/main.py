from typing import Annotated

from fastapi import FastAPI, Depends
from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db, User
from app.schemes import UserScheme

app = FastAPI()


@app.get("/")
async def welcome():
    return {"message": "Hello world."}


@app.post("/users/new")
async def add_user(user: UserScheme, db_session: Annotated[AsyncSession, Depends(get_db)]):
    await db_session.execute(insert(User).values(**user.model_dump()))
    await db_session.commit()
    return {"message": "User created."}


@app.get("/users/{user_id}")
async def get_user(user_id: int, db_session: Annotated[AsyncSession, Depends(get_db)]):
    user = await db_session.execute(select(User).where(user_id == User.id))
    return {"data": user.scalar()}


