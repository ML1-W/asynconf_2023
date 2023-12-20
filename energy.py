from icecream import ic
from strenum import StrEnum
from enum import auto

from init_database import Base_asynconf, asynconf
from sqlalchemy import Column, Integer, String


class Energy(Base_asynconf):
    """
    A class used to represent the type of Energy used by a car (diesel,essence...).

    Data come from ASYNCONF Hackathon 2023 - Green Bank, Banque Populaire Val de France.
    """
    __tablename__ = "energy"

    name = Column("Name", String, primary_key=True)
    mark = Column("Mark", Integer)

    def __init__(self, name, mark):
        self.name = name
        self.mark = mark


def get_energy_score(energy_type) -> int:
    """
    Retrieves ecological score for the specified type of energy.

    Args:
        energy_type (EnergyType): The type of energy such as diesel, essence....

    Returns:
        int: The ecological score for the specified energy.
    """
    try:
        energy_type.value
    except AttributeError as e:
        raise AttributeError(f"Use an energy from EnergyType class\n"
                             f"Energy type present: {[e.name for e in EnergyType]}")
    query = asynconf.query(Energy).filter(Energy.name == energy_type)
    element_object = query.first()
    if element_object is None:
        raise ValueError(f"The vehicle type '{energy_type}' is not present in the database.\n"
                         f"Vehicle type present:")
    return element_object.mark


class EnergyType(StrEnum):
    """Enumerate the different energy type defined in the database"""
    Essence = auto()
    Electrique = auto()
    Gaz = auto()
    Diesel = auto()
    Hybride = auto()


if __name__ == "__main__":
    ic(EnergyType.Diesel)
    print(get_energy_score(EnergyType.Diesel))
