from data.classes import Customer
from db.operations.customer import db_add_customer, db_get_customer
from main import SESSION_MAKER


def add_customer(customer: Customer) -> Customer:
    with SESSION_MAKER.begin() as session:  # type: ignore
        return db_add_customer(customer=customer, session=session)


def get_customer(id: int) -> Customer:
    with SESSION_MAKER.begin() as session:  # type: ignore
        return db_get_customer(id=id, session=session)
