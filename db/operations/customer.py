from data.classes import Customer, asdict
from sqlalchemy.orm.session import Session
from db.tables import DBCustomer


def add_customer(customer: Customer, session: Session) -> Customer:
    db_customer = DBCustomer(**asdict(customer))
    session.add(db_customer)
    session.flush()
    customer.id = db_customer.id
    return customer


def main():
    from db.init_db import init_engine, init_session_maker
    from db.create_db import create_db
    from db.tables import mapper_registry

    engine = init_engine()
    SessionMaker = init_session_maker(engine=engine)
    create_db(engine=engine, mapper_registry=mapper_registry)
    customer = Customer(
        first_name="Dave", last_name="Wilson", email_address="D.wilson@this.com"
    )

    with SessionMaker.begin() as session: # type: ignore
        print(add_customer(customer=customer, session=session))
    


if __name__ == "__main__":
    main()
