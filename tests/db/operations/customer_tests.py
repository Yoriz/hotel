import unittest

from hotel.data.classes import Customer
from hotel.db.create_db import create_db
from hotel.db.init_db import init_engine, init_session_maker
from hotel.db.operations.customer import db_add_customer, db_get_customer
from hotel.db.tables import mapper_registry


class CustomerTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.engine = init_engine()
        self.SessionMaker = init_session_maker(engine=self.engine)
        create_db(engine=self.engine, mapper_registry=mapper_registry)
        return None

    def test_add_customer(self):
        customer = Customer(
            first_name="Firstname", last_name="Lastname", email_address="EmailAddress"
        )
        with self.SessionMaker.begin() as session:  # type: ignore
            returned_customer = db_add_customer(customer=customer, session=session)
        customer.id = 1
        self.assertEqual(customer, returned_customer)

    def test_get_customer(self):
        customer = Customer(
            first_name="Firstname", last_name="Lastname", email_address="EmailAddress"
        )
        with self.SessionMaker.begin() as session:  # type: ignore
            returned_customer = db_add_customer(customer=customer, session=session)
        db_customer = db_get_customer(id=1, session=session)
        self.assertEqual(returned_customer, db_customer)


if __name__ == "__main__":
    unittest.main()
