COLOUR_NAMES = {"azure1": "#f0ffff", "chocolate1": "#ff7f50", "DarkViolet": "#9400d3",
                "gray1": "#030303", "green1": "#00ff00", "LightSteelBlue2": "#bcd2ee",
                "magenta": "#ff00ff", "MediumSpringGreen": "#00fa9a", "OrangeRed1": "ff4500",
                "red1": "#ff0000"}

colour = input("Colour name: ")
while colour != "":
    if colour in COLOUR_NAMES:
        print(colour, "has the code", COLOUR_NAMES[colour])
    else:
        print("Incorrect Colour name.")
    colour = input("Colour name: ")
