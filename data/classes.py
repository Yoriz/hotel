from dataclasses import dataclass, field
from datetime import date
from typing import Any, Optional
from dataclasses import asdict as asdict_


def asdict(dataclass, omit_id: bool = True) -> dict[str, Any]:
    result = asdict_(dataclass)
    if omit_id:
        del result["id"]
    return result


@dataclass
class Customer:
    first_name: str
    last_name: str
    email_address: str
    bookings: list["Booking"] = field(default_factory=list["Booking"])
    id: Optional[int] = None


@dataclass
class Room:
    number: str
    size: int
    price: int
    bookings: list["Booking"] = field(default_factory=list["Booking"])
    id: Optional[int] = None


@dataclass
class Booking:
    from_date: date
    to_date: date
    customer: Customer
    room: Room
    id: Optional[int] = None
