from icecream import ic
from strenum import StrEnum
from enum import auto

from init_database import Base_asynconf, asynconf
from sqlalchemy import Column, Integer, String


class Car(Base_asynconf):
    """
    A class used to represent a Car

    Data come from ASYNCONF Hackathon 2023 - Green Bank, Banque Populaire Val de France.
    """
    __tablename__ = "car"

    name = Column("Name", String, primary_key=True)
    weight = Column("Weight", String)
    mark = Column("Mark", Integer)

    def __init__(self, name, weight, mark):
        self.name = name
        self.weight = weight
        self.mark = mark


class VehicleType(StrEnum):
    """Enumerate the different vehicle type defined in the database"""
    Citadine = auto()
    Cabriolet = auto()
    Berline = auto()
    SUV = "SUV/4x4"


def get_vehicle_score(vehicle_type: VehicleType) -> int:
    """
    Retrieves ecological score for the specified vehicle.

    Args:
        vehicle_type (VehicleType): The type of vehicle such as Cabriolet, Berline....

    Returns:
        int: The ecological score for the specified vehicle.
    """
    try:
        vehicle_type.value
    except AttributeError as e:
        raise AttributeError(f"Use a vehicle from VehicleType class\n"
                             f"Vehicle type present: {[vehicle.name for vehicle in VehicleType]}")

    query = asynconf.query(Car).filter(Car.name == vehicle_type.value)
    element_object = query.first()
    if element_object is None:
        raise ValueError(f"The vehicle type '{vehicle_type}' is not present in the database.\n")

    return element_object.mark


if __name__ == "__main__":
    # get_vehicle_score()
    ic(VehicleType.SUV.name)
    print(get_vehicle_score(VehicleType.Citadine))
