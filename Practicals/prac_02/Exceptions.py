try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator == 0:
        print("Cannot have the denominator as 0!")
        denominator = int(input("Enter the denominator: "))
        fraction = numerator / denominator
        print(fraction)
    else:
        fraction = numerator / denominator
        print(fraction)
except ValueError:
    print("Numerator ad denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by Zero!")
print("Finished.")
