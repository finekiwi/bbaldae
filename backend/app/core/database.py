from collections.abc import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

from app.config import get_settings


class Base(DeclarativeBase):
    pass


_engine = None
_session_factory = None


def get_engine() -> AsyncEngine:
    """Return the async SQLAlchemy engine, creating it lazily on first call."""
    global _engine
    if _engine is None:
        settings = get_settings()
        url = settings.DATABASE_URL.replace("postgresql://", "postgresql+asyncpg://")
        _engine = create_async_engine(url, echo=False)
    return _engine


def get_session_factory() -> async_sessionmaker[AsyncSession]:
    """Return the async session factory, creating it lazily on first call."""
    global _session_factory
    if _session_factory is None:
        _session_factory = async_sessionmaker(
            get_engine(),
            class_=AsyncSession,
            expire_on_commit=False,
        )
    return _session_factory


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    """Yield an async DB session. Commit/rollback is the caller's responsibility."""
    async with get_session_factory()() as session:
        yield session
