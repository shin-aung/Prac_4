COLOUR_NAMES = {"ABSOLUTE ZERO": "#0048ba", "ACID GREEN": "#b0bf1a", "ALICEBLUE": "f0f8ff", "AMBER": "#ffbf00",
                "BABY PINK": "f4c2c2", "BRONZE": "#cd7f32", "CAMEL": "#c19a6b", "EMINENCE": "#6c3082",
                "GRANNY SMITH APPLE": "#a8e4a0", "ZAFFRE": "#0014a8"}
print(COLOUR_NAMES)
colour_name = input("Enter a name of colour: ").upper()
while colour_name != "":
    if colour_name in COLOUR_NAMES:
        print(f"The code of {colour_name} is {COLOUR_NAMES[colour_name]}.")
    else:
        print("There is no such colour.")
    colour_name = input("Enter a name of colour: ").upper()