def fel1():
    tipus: str = input("Kérek egy színkeverési módszert: ")
    kod: str = input("Kérem a kódot: ")
    tipus = tipus.upper()
    if tipus == "HEX":
        if len(kod) == 6:
            print("Megfelelő hossz.")
        else:
            print("Bonyolult kiszámolni.")
    elif tipus == "RGB":
        if 7 <= len(kod) <= 11:
            print("Megfelelő hossz.")
        else:
            print("Bonyolult kiszámolni.")
    elif tipus == "HSL":
        if 7 <= len(kod) <= 13:
            print("Megfelelő hossz.")
        else:
            print("Bonyolult kiszámolni.")
    elif tipus == "RGBA":
        if 7 <= len(kod) <= 11:
            print("Megfelelő hossz.")
        else:
            print("Bonyolult kiszámolni.")


