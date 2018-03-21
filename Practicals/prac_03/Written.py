user_name = input("Your name: ")

if len(user_name.strip()) == 0:
    print("You have not entered a name.")
else:
    print("{}".format(user_name[0:-1:2]))