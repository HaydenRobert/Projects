""""""

from prac_07.Guitar import Guitar


def main():
    """"""
    first_guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)
    print("{} get_age() - Expected 96. Got {}".format(first_guitar.name, first_guitar.get_age()))
    another_guitar = Guitar("Another guitar", 2012, 16035.40)
    print("{} get_age() - Expected 6. Got {}".format(another_guitar.name, another_guitar.get_age()))

main()
