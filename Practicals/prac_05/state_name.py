"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

# Reformatted this file so the dictionary code follows PEP 8 convention
STATE_NAMES = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
               "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
# print(STATE_NAMES)

state = input("Enter short state: ")
while state != "":
    state = state.upper()
    if state in STATE_NAMES:
        print(state, "is", STATE_NAMES[state])
    else:
        print("Invalid short state")
    state = input("Enter short state: ")

for state in STATE_NAMES:
    print("{:<3} is {:<30}".format(state, STATE_NAMES[state]))
