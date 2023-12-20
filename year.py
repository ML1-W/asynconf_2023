from init_database import Base_asynconf, asynconf
from sqlalchemy import Column, Integer, String


class Year(Base_asynconf):
    """
    A class used to represent the number of year of manufacture of the car.

    Data come from ASYNCONF Hackathon 2023 - Green Bank, Banque Populaire Val de France.
    """
    __tablename__ = "year"

    name = Column("Name", String, primary_key=True)
    mark = Column("Mark", Integer)

    def __init__(self, name, mark):
        self.name = name
        self.mark = mark


def get_year_score(year:int) -> int:
    """
    Retrieves ecological score for the specified year of manufacture of the car.

    Args:
        year (int): The year of manufacture of the car

    Returns:
        int: The ecological score for the specified year.
    """
    year_range = select_year_range(year=year)
    query = asynconf.query(Year).filter(Year.name == year_range)
    element_object = query.first()
    if element_object is None:
        raise ValueError(f"An error occured.")
    return element_object.mark


def select_year_range(year) -> str:
    """create the str used in the database according to the year of manufacture"""
    if 1960 <= year < 1970:
        return "1960-1970"
    elif 1970 <= year < 1980:
        return "1970-1980"
    elif 1980 <= year < 1990:
        return "1980-1990"
    elif 1990 <= year < 2000:
        return "1990-2000"
    elif 2000 <= year < 2010:
        return "2000-2010"
    elif 2010 <= year:
        return ">2010"
    else:
        print("The car is too old")
        raise ValueError


if __name__ == "__main__":
    print(get_year_score(year=1980))
