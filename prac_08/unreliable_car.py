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
        random_car_distance = randrange(0, 101, 1)
        if random_car_distance <= self.reliability:
            self.odometer += random_car_distance
            return random_car_distance
        else:
            self.odometer += distance
            return distance