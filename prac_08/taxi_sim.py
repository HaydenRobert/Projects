from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi

user_choice = input("Let's drive!\nq)uit, c)hoose taxi, d)rive\n>>>")
taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
line_count = 0


def main():
    """"""

    if user_choice == "c":
        print("Taxis available:\n{} - {}".format(line_count, taxis[line_count]))
        line_count += 1
