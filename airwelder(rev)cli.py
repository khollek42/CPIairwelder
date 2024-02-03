from functionscli import get_heat1055, get_speed1055, get_heat1055t, get_speed1055t, get_heat4090, get_speed4090, \
    get_heatvinyl, get_speedvinyl, get_heat955, get_speed955


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

