from hotel.data.classes import Customer, asdict
from hotel.db.init_db import SessionMaker
from hotel.db.tables import DBCustomer
from sqlalchemy import select
from sqlalchemy.orm.session import Session


def db_add_customer(customer: Customer) -> Customer:
    with SessionMaker.begin() as session:  # type: ignore
        session: Session
        db_customer = DBCustomer(**asdict(customer))
        session.add(db_customer)
        session.flush()
        customer.id = db_customer.id
        return customer


def db_get_customer(id: int) -> Customer:
    stmt = select(DBCustomer).where(DBCustomer.id == id)  # type: ignore
    with SessionMaker.begin() as session:  # type: ignore
        session: Session
        db_customer: DBCustomer = session.execute(stmt).scalar()
        return Customer(
            first_name=db_customer.first_name,
            last_name=db_customer.last_name,
            email_address=db_customer.email_address,
            id=db_customer.id,
        )
