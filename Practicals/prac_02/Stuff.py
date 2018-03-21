user_name = input("Your name is: ")
if user_name is None:
    print("You have not entered a name")
else:
    for char in user_name:
        print("{}".format(user_name))
