""""""

from prac_07.playing_guitar import Guitar


def main():
    """"""
    print("My guitars!")
    name = input("Name: ")
    year = int(input("Year: "))
    cost = int(input("Cost: $"))
    first = Guitar(name, year, cost)
    print("{} ({}) : {}".format(first.name, first.year, first.cost))
    main()
