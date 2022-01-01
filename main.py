from db.init_db import init_engine, init_session_maker
from db.create_db import create_db
from db.tables import mapper_registry
from db.add_test_data import add_test_data

CREATE_DB = True
ADD_TEST_DATA = True
DB_URL = "sqlite:///hotel.db"


def main():
    engine = init_engine(url=DB_URL)
    SessionMaker = init_session_maker(engine=engine)
    if CREATE_DB:
        create_db(engine=engine, mapper_registry=mapper_registry)
    if ADD_TEST_DATA:
        add_test_data(session_maker=SessionMaker)


if __name__ == "__main__":
    main()
