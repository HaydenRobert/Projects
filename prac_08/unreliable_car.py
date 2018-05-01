""""""
from prac_08.car import Car
from random import randrange

class UnreliableCar(Car):
    """"""

    def __init__(self, name, fuel, reliability):
        """"""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        random_car_reliable = float(randrange(0, 101, 1))
        if random_car_reliable <= self.reliability:
            return 0
        else:
            distance_driven = super().drive(distance)
            return distance_driven