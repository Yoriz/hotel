from sqlalchemy.orm.session import Session
from hotel.data.classes import Customer, asdict
from hotel.db.tables import DBCustomer


def add_customer(customer: Customer, session: Session) -> Customer:
    db_customer = DBCustomer(**asdict(customer))
    session.add(db_customer)
    session.flush()
    customer.id = db_customer.id
    return customer
