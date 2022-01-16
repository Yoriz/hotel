from dataclasses import dataclass, field
from enum import Enum, auto

from data.classes import Customer
from hotel.db.operations.customer import db_get_customer
from util.event import Event


class CustomerEvent(Enum):
    CUSTOMER_UPDATED = auto()


def empty_customer() -> Customer:
    return Customer(first_name="", last_name="", email_address="")


@dataclass
class CustomerModel:
    customer: Customer = field(default_factory=empty_customer)
    event: Event = field(default_factory=Event, init=False)

    def set_customer_by_id(self, id: int) -> None:
        self.customer = db_get_customer(id=id)
        self.event.notify(
            event_type=CustomerEvent.CUSTOMER_UPDATED, customer=self.customer
        )


def test_bind(customer: Customer):
    print(f"{customer=}")


test = CustomerModel()
test.event.bind(event_type=CustomerEvent.CUSTOMER_UPDATED, callable=test_bind)
test.set_customer_by_id(1)
