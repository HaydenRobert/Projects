from prac_08.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """"""
    flag_fall = 4.50

    def __init__(self, name, fuel, fanciness):
        """"""
        super().__init__(name, fuel)
        fanciness = float(fanciness)
        self.price_per_km = Taxi.price_per_km * fanciness

    def get_fare(self):
        """"""
        fare_cost = super().get_fare() + self.flag_fall
        print("Fare cost ${:.2f}".format(fare_cost))

    def __str__(self):
        """"""
        return "{} plus flagfall of ${:.2f}".format\
            (super().__str__(), self.flag_fall)
