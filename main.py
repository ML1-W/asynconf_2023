from dataclasses import dataclass

from icecream import ic

from car import get_vehicle_score, VehicleType
from energy import get_energy_score, EnergyType
from kilometre import get_kilometres_score
from year import get_year_score
from loan_rate import get_loan_rate
from passenger import get_passenger_bonus


@dataclass
class InfoVehicle:
    vehicle_type: VehicleType
    energy_type: EnergyType
    number_of_kilokm_per_year: int
    manufacture_year_of_vehicle: int


@dataclass
class InfoUsage:
    number_passenger: int


@dataclass
class InfoSimulation:
    info_vehicle: InfoVehicle
    info_usage: InfoUsage

    def __repr__(self):
        return f"  - vehicle type: {self.info_vehicle.vehicle_type},\n" \
               f"  - energy type: {self.info_vehicle.energy_type},\n" \
               f"  - number of Kilokm per year: {self.info_vehicle.number_of_kilokm_per_year},\n" \
               f"  - manufacture year of the vehicle: {self.info_vehicle.manufacture_year_of_vehicle},\n" \
               f"  - number of passenger: {self.info_usage.number_passenger}"


def calculate_score(info_vehicle: InfoVehicle):
    ic(get_vehicle_score(info_vehicle.vehicle_type))
    ic(get_energy_score(info_vehicle.energy_type))
    ic(get_kilometres_score(kilo_km_per_year=info_vehicle.number_of_kilokm_per_year))
    ic(get_year_score(year=info_vehicle.manufacture_year_of_vehicle))
    score = get_vehicle_score(info_vehicle.vehicle_type) + \
            get_energy_score(info_vehicle.energy_type) + \
            get_kilometres_score(kilo_km_per_year=info_vehicle.number_of_kilokm_per_year) + \
            get_year_score(year=info_vehicle.manufacture_year_of_vehicle)
    return score


def calculate_bonus(info_usage: InfoUsage):
    ic(get_passenger_bonus(number_passenger=info_usage.number_passenger))
    return get_passenger_bonus(number_passenger=info_usage.number_passenger)


def calculate_loan_rate(info_simulation: InfoSimulation):
    total_score = calculate_score(info_simulation.info_vehicle)
    ic(total_score)
    ic(get_loan_rate(score=total_score))
    bonus = calculate_bonus(info_simulation.info_usage)
    total_loan_rate = get_loan_rate(score=total_score) + bonus
    return total_loan_rate


def main():
    info_vehicle = InfoVehicle(vehicle_type=VehicleType.Citadine,
                               energy_type=EnergyType.Diesel,
                               number_of_kilokm_per_year=10,
                               manufacture_year_of_vehicle=1990)

    info_usage = InfoUsage(number_passenger=3)

    info_simulation = InfoSimulation(info_vehicle=info_vehicle,
                                     info_usage=info_usage)

    estimated_loan_rate = calculate_loan_rate(info_simulation)

    print(f"According to your information : \n{info_simulation}, \n\nthe estimated loan rate is: {estimated_loan_rate}%")


if __name__ == "__main__":
    main()
