from prac_08.silver_service_taxi import SilverServiceTaxi

s_taxi_one = SilverServiceTaxi("Hummer", 200, 4)
s_taxi_one.drive(0)
print(s_taxi_one)
s_taxi_two = SilverServiceTaxi("Hummer", 40, 2)
s_taxi_two.drive(18)
s_taxi_two.get_fare()

