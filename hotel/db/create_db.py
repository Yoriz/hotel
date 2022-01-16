from sqlalchemy.engine.base import Engine
from sqlalchemy.orm.decl_api import registry
from db.tables import mapper_registry
from hotel.db.init_db import ENGINE


def create_db(engine: Engine, mapper_registry: registry) -> None:
    with engine.begin() as connection:
        mapper_registry.metadata.create_all(connection)

    return None

def main():
    create_db(engine=ENGINE, mapper_registry=mapper_registry)

if __name__ == "__main__":
    main()