
from icecream import ic

from init_database import Base_asynconf, asynconf
from sqlalchemy import Column, Integer, String


class Passenger(Base_asynconf):
    """
    A class used to represent the number of passenger in the car.

    Data come from ASYNCONF Hackathon 2023 - Green Bank, Banque Populaire Val de France.
    """
    __tablename__ = "passenger"

    id = Column("Id", Integer, primary_key=True)
    number = Column("Number", String)
    rate = Column("Rate", Integer)

    def __init__(self, id, number, rate):
        self.id = id
        self.number = number
        self.rate = rate


def get_passenger_bonus(number_passenger: int) -> int:
    """
    Retrieves bonus on loan rate according to the number of passengers in the car.

    Args:
        number_passenger (int): The number of kilo km made by year

    Returns:
        int: The bonus on the loan rate.
    """
    query = asynconf.query(Passenger).filter(Passenger.number == number_passenger)
    element_object = query.first()
    if element_object is None:
        raise ValueError(f"The number of passenger is out of range.\n")
    return element_object.rate


if __name__ == "__main__":
    print(get_passenger_bonus(number_passenger=3))
