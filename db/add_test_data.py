from db.tables import DBCustomer, DBRoom, DBBooking
from sqlalchemy.orm.session import Session, sessionmaker
from datetime import date


def add_test_data(session_maker: sessionmaker) -> None:
    with session_maker.begin() as session:
        session: Session
        customer = DBCustomer(first_name="Yor", last_name="iz", email_address="This")
        room = DBRoom(number="1A", size=2, price=1000)
        booking = DBBooking(
            from_date=date.today(),
            to_date=date.today(),
            price=1000,
            customer=customer,
            room=room,
        )
        session.add(booking)

    return None
