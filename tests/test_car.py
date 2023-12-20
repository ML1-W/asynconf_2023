# Created by E. Wilhelm at 31/10/2023
import sys
import unittest

from car import VehicleType, get_vehicle_score
from icecream import ic

sys.path.append("..")


class TestCar(unittest.TestCase):
    def setUp(self):
        """create data used in several places of the test"""
        pass

    def test_car_score(self):
        self.assertEqual(get_vehicle_score(VehicleType.Citadine), 8)
        self.assertEqual(get_vehicle_score(VehicleType.Cabriolet), 6)
        self.assertEqual(get_vehicle_score(VehicleType.Berline), 6.5)
        self.assertEqual(get_vehicle_score(VehicleType.SUV), 4)

    def test_wrong_car(self):
        with self.assertRaises(AttributeError) as cm:
            get_vehicle_score("wrong")
        ic(cm.exception)



if __name__ == "__main__":
    unittest.main()
