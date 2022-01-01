from hotel.db.init_db import init_engine, init_session_maker
from hotel.db.create_db import create_db
from hotel.db.operations.customer import add_customer
from hotel.db.tables import mapper_registry
import unittest
from hotel.data.classes import Customer


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
            returned_customer = add_customer(customer=customer, session=session)
        customer.id = 1
        self.assertEqual(customer, returned_customer)



if __name__ == "__main__":
    unittest.main()