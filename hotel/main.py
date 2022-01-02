from db.add_test_data import add_test_data
from db.create_db import create_db
from db.init_db import init_engine, init_session_maker
from db.tables import mapper_registry

CREATE_DB = True
ADD_TEST_DATA = True
DB_URL = "sqlite:///data/hotel.db"
ENGINE = init_engine(url=DB_URL)
SESSION_MAKER = init_session_maker(engine=ENGINE)


def main():
    if CREATE_DB:
        create_db(engine=ENGINE, mapper_registry=mapper_registry)
    if ADD_TEST_DATA:
        add_test_data(session_maker=SESSION_MAKER)


if __name__ == "__main__":
    main()
