import math


def material1055_3(speed):
    x = (0.343376 * speed) + 7.11931
    i = math.log(x)
    n = 2020.91 * i
    result = n - 3513.43
    return result




def material1055_3(heat):

    heat1 = heat * 100
    heat2 = heat1 + 351543
    heat3 = heat2 / 202091
    e = 2.7182818284590452353602874713527
    heat4 = math.pow(e, heat3)
    heat5 = heat4 - 7.11931
    result = heat5 / 0.343376
    print(heat5)
    return result

def hmaterial1055_3test2(speed):
    x = (3.16528 * speed) + 25.1954
    i = math.log(x)
    n = 1077.65 * i
    result = n - 3104.65
    return result




def smaterial1055_3test2(heat):

    heat1 = heat * 100
    heat2 = heat1 + 310465
    heat3 = heat2 / 107765
    e = 2.7182818284590452353602874713527
    heat4 = math.pow(e, heat3)
    heat5 = heat4 - 25.1954
    result = heat5 / 3.16528
    print(heat5)
    return result

if __name__ == "__main__":
    print(material1055_3(heat))
    print(material1055_3(speed))

    speed = float(input("Speed: "))
    heat = float(input("Heat: "))
