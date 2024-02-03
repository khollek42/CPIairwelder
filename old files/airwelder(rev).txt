

def heat():
    heat = float(input("what is the heat? "))
    return heat

def speed():
    speed = float(input("What is the speed? "))
    return speed

# This is the 1055 Functions
def get_heat1055(np1):
    temp = 260 + np1 + (speed() * 90)
    return f"Heat = {temp} Celsius"

def get_speed1055(np1):
    speed = float((heat() - (260 + np1)) / 90)
    return f"Speed = {speed} M/m"


# 1055 Tape Functions
def get_heat1055t(np1):
    temp = 270 + np1 + (speed() * 90)
    return f"Heat = {temp} Celsius"

def get_speed1055t(np1):
    speed = float((heat() - (270 + np1)) / 90)
    return f"Speed = {speed} M/m"


# 4090 Functions
def get_heat4090(np1):
    temp = 345 + np1 + (speed() * 90)
    return f"Heat = {temp} Celsius"

def get_speed4090(np1):
    speed = float((heat() - (345 + np1)) / 90)
    return f"Speed = {speed} M/m"


# Vinyl Functions
def get_heatvinyl(np1):
    temp = 285 + np1 + (speed() * 90)
    return f"Heat = {temp} Celsius"

def get_speedvinyl(np1):
    speed = float((heat() - (285 + np1)) / 90)
    return f"Speed = {speed} M/m"


# 955 Functions
def get_heat955(np1):
    temp = 315 + np1 + (speed() * 70)
    return f"Heat = {temp} Celsius"

def get_speed955(np1):
    speed = float((heat() - (315 + np1)) / 70)
    return f"Speed = {speed} M/m"

def main():
    while True:
        try:
            material = input("What material are you using? 1055, 1055t, 4090, 955, vinyl. ")
            intro = input("Do you want the Heat or the Speed? ")
            np1 = int(input("Nozzle placement variable, default is 0, + Number is farther away, - is closer to wheel. "))

            if intro in ["heat", "Heat"] and material in ["1055"]:
                print(get_heat1055(np1))
                break

            elif intro in ["speed", "Speed"] and material in ["1055"]:
                print(get_speed1055(np1))
                break

            elif intro in ["heat", "Heat"] and material in ["1055t"]:
                print(get_heat1055t(np1))
                break

            elif intro in ["speed", "Speed"] and material in ["1055t"]:
                print(get_speed1055t(np1))
                break

            elif intro in ["heat", "Heat"] and material in ["4090"]:
                print(get_heat4090(np1))
                break

            elif intro in ["speed", "Speed"] and material in ["4090"]:
                print(get_speed4090(np1))
                break

            elif intro in ["heat", "Heat"] and material in ["vinyl", "Vinyl"]:
                print(get_heatvinyl(np1))
                break

            elif intro in ["speed", "Speed"] and material in ["vinyl", "Vinyl"]:
                print(get_speedvinyl(np1))
                break

            elif intro in ["heat", "Heat"] and material in ["955"]:
                print(get_heat955(np1))
                break

            elif intro in ["speed", "Speed"] and material in ["955"]:
                print(get_speed955(np1))
                break

            else:
                print("Wrong input, try typing heat or speed")
        except ValueError:
            print("Try typing in a speed from 1-3.5 or heat from 380-600")

main()

