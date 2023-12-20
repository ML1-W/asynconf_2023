from init_database import Base_asynconf, asynconf
from sqlalchemy import Column, Integer, String


class Kilometres(Base_asynconf):
    """
    A class used to represent the number of kilometres made per year.

    Data come from ASYNCONF Hackathon 2023 - Green Bank, Banque Populaire Val de France.
    """
    __tablename__ = "kilometre"

    name = Column("Name", String, primary_key=True)
    mark = Column("Mark", Integer)

    def __init__(self, name, mark):
        self.name = name
        self.mark = mark


def get_kilometres_score(kilo_km_per_year:int) -> int:
    """
    Retrieves ecological score for the specified number of kilometres per year.

    Args:
        kilo_km_per_year (int): The number of kilo km made by year

    Returns:
        int: The ecological score for the specified number of kilo km per year.
    """
    km_range = select_km_range(kilo_km_per_year=kilo_km_per_year)
    query = asynconf.query(Kilometres).filter(Kilometres.name == km_range)
    element_object = query.first()
    if element_object is None:
        raise ValueError(f"An error occured.")
    return element_object.mark


def select_km_range(kilo_km_per_year) -> str:
    """create the str used in the database according to the number of km"""
    if 5 <= kilo_km_per_year < 10:
        return "5-10"
    elif 10 <= kilo_km_per_year < 15:
        return "10-15"
    elif 15 <= kilo_km_per_year < 20:
        return "15-20"
    elif 20 <= kilo_km_per_year < 25:
        return "20-25"
    elif 25 <= kilo_km_per_year < 30:
        return "25-30"
    else:
        print("Kilometres per year is out of the range [5:30] Kkm/year")
        raise ValueError


if __name__ == "__main__":
    print(get_kilometres_score(kilo_km_per_year=10))
