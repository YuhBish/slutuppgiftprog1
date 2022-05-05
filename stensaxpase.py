import random

while True:
    val = input("ait nu jävlar ska vi spela... STEN SAX PÅSE: ")
    möjliga = ["sten", "påse", "sax"]
    dator = random.choice(möjliga)
    print(f"\ndu tog {val}, datorn tog {dator}.\n")

    if val == dator:
        print(f"båda tog {val}. pröva igen")
    elif val == "sten":
        if dator == "sax":
            print("sten vinner över sax ggez")
        else:
            print("lmao pappret fucka dig")
    elif val == "påse":
        if dator == "sten":
            print("ha påse funkar alltid(förutom ibland)")
        else:
            print("han klippte till dig på riktigt där")
    elif val == "sax":
        if dator == "påse":
            print("ok du behövde inte lämlästa påsen... men du vann yey antar ja? vafan ska ja säga till påsens familj?")
        else:
            print("försökte du just klippa en sten? tror du behöver tänka till före ")

    spela = input("en till match? ja eller nej?")
    if spela.lower() != "ja":
        break