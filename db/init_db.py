from typing import Optional
from sqlalchemy.engine import create_engine
from sqlalchemy.engine.base import Engine
from sqlalchemy.orm import sessionmaker

MEMORY_URL = "sqlite+pysqlite:///:memory:"


def init_engine(url: Optional[str] = None) -> Engine:
    return create_engine(url or MEMORY_URL, echo=True, future=True)


def init_session_maker(engine: Engine) -> sessionmaker:
    return sessionmaker(bind=engine, expire_on_commit=False, future=True)
