from sqlalchemy.orm.session import Session
from hotel.data.classes import Customer, asdict
from hotel.db.tables import DBCustomer
from sqlalchemy import select


def add_customer(customer: Customer, session: Session) -> Customer:
    db_customer = DBCustomer(**asdict(customer))
    session.add(db_customer)
    session.flush()
    customer.id = db_customer.id
    return customer


def get_customer(id: int, session: Session) -> Customer:
    stmt = select(DBCustomer).where(DBCustomer.id == id)
    db_customer: DBCustomer = session.execute(stmt).scalar()
    return Customer(
        first_name=db_customer.first_name,
        last_name=db_customer.last_name,
        email_address=db_customer.email_address,
        id=db_customer.id
    )
