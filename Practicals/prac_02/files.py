user_name = input("Your name? ")
text_file = open('data.txt', 'w')

print("{}".format(user_name), file=text_file)

text_file.close()

read_file = open("data.txt", "r")
user_name_1 = read_file.read()

print("Your name is", user_name_1)

read_file.close()

numbers = open('numbers.txt', 'r')
running_total = 0
for line in numbers:
    line1 = int(line)
    running_total += line1
print(running_total)

numbers.close()
