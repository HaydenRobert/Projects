import random

number_of_picks = int(input("How many quick picks? "))
count = 0
while number_of_picks > count:
    Constants = []
    for i in range(1, 7, 1):
        Random_numb = random.randint(2, 45)
        Constants.append(Random_numb)
    Constants.sort()
    print("{:>3} {:>3} {:>3} {:>3} {:>3} {:>3}".format(*Constants))
    count += 1
