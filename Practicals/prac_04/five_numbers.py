Numbers = []

for i in range(1, 6, 1):
    Number = int(input("Number: "))
    Numbers.append(Number)

print("The first number is {}".format(Numbers[0]))
print("The Last number is {}".format(Numbers[-1]))
print("The smallest number is {}".format(min(Numbers)))
print("The largest number is {}".format(max(Numbers)))
print("The average number is {}".format(sum(Numbers) / len(Numbers)))

