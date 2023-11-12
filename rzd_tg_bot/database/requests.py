from typing import List
from sqlalchemy import desc, func, select, update

from .models import User, async_session


async def add_user_if_not_exists(tg_id: int, name: str) -> None:
    async with async_session() as session:
        async with session.begin():
            user = await session.execute(select(User).filter_by(tg_id=tg_id))
            user = user.scalar_one_or_none()

            if not user:
                new_user = User(tg_id=tg_id, name=name)
                session.add(new_user)


async def increase_score(tg_id: int) -> None:
    async with async_session() as session:
        async with session.begin():
            await session.execute(update(User).where(User.tg_id == tg_id).values(score=User.score + 1))


async def get_user(tg_id: int) -> User:
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))
        return user


async def get_top_users() -> List[User]:
    async with async_session() as session:
        result = await session.execute(select(User).order_by(desc(User.score)).limit(10))
        return result.scalars().all()


async def get_user_rank(tg_id: int) -> int:
    async with async_session() as session:
        result = await session.execute(
            select(func.count(User.score)).where(User.score > select(User.score).where(User.tg_id == tg_id))
        )
        rank = result.scalar_one() + 1
        return rank
