from sqlalchemy.engine.base import Engine
from sqlalchemy.orm.decl_api import registry


def create_db(engine: Engine, mapper_registry: registry) -> None:
    with engine.begin() as connection:
        mapper_registry.metadata.create_all(connection)

    return None
