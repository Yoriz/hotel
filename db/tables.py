from typing import Optional
from sqlalchemy.orm.decl_api import registry
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from datetime import date


mapper_registry = registry()


@mapper_registry.mapped
class DBCustomer:
    __tablename__ = "customer"
    id = Column(Integer, primary_key=True)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    email_address = Column(String(250), nullable=False)

    bookings = relationship("DBBooking", back_populates="customer")

    def __init__(
        self,
        first_name: str,
        last_name: str,
        email_address: str,
        bookings: Optional[list["DBBooking"]] = None,
    ) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email_address
        self.bookings = bookings or []


@mapper_registry.mapped
class DBRoom:
    __tablename__ = "room"
    id = Column(Integer, primary_key=True)
    number = Column(String(250), nullable=False)
    size = Column(Integer, nullable=False)
    price = Column(Integer, nullable=False)

    bookings = relationship("DBBooking", back_populates="room")

    def __init__(
        self,
        number: str,
        size: int,
        price: int,
        bookings: Optional[list["DBBooking"]] = None,
    ) -> None:
        self.number = number
        self.size = size
        self.price = price
        self.bookings = bookings or []


@mapper_registry.mapped
class DBBooking:
    __tablename__ = "booking"
    id = Column(Integer, primary_key=True)
    from_date = Column(Date, nullable=False)
    to_date = Column(Date, nullable=False)
    price = Column(Integer, nullable=False)

    customer_id = Column(Integer, ForeignKey("customer.id"))
    customer = relationship(DBCustomer, back_populates="bookings")
    room_id = Column(Integer, ForeignKey("room.id"))
    room = relationship(DBRoom, back_populates="bookings")

    def __init__(
        self,
        from_date: date,
        to_date: date,
        price: int,
        customer: DBCustomer,
        room: DBRoom,
    ) -> None:
        self.from_date = from_date
        self.to_date = to_date
        self.price = price
        self.customer = customer
        self.room = room
