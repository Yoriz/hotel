from typing import Optional

from sqlalchemy.engine import create_engine
from sqlalchemy.engine.base import Engine
from sqlalchemy.orm import sessionmaker

MEMORY_URL = "sqlite+pysqlite:///:memory:"
DB_URL = "sqlite:///data/hotel.db"
ECHO = True


def init_engine(url: Optional[str] = None) -> Engine:
    return create_engine(url or MEMORY_URL, echo=ECHO, future=True)


def init_session_maker(engine: Engine) -> sessionmaker:
    return sessionmaker(bind=engine, future=True)


ENGINE = init_engine(url=DB_URL)
SessionMaker = init_session_maker(engine=ENGINE)
