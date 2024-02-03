

import sys
import matplotlib.pyplot as plt
import numpy as np

# get settings for air welder
#still need to adjust 4090 parameters. this is just a the setup for it.

'''Material 1055:
    This is with speed and heat being a good weld at:
speed(m/s): heat(c°)
1 : 430
2 : 480
3 : 530

1 m/s to every 50 degrees c°.

Material 4090:
 This is with speed and heat being a good weld at:
speed(m/s): heat(c°)
1 : 430
2 : 480
3 : 530

1 m/s to every 50 degrees c°.
'''
#Material 1055 seam settings

#function to get the heat setting you want
def get_heat():
    np1 = int(input("Nozzle placement variable, default is 0, + Number is farther away, - is closer to wheel. "))
    speed = float(input("What is the speed? "))
    temp = 260 + np1 + (speed * 90)
        
    print("Heat =",temp, "Celsius")

#function to get the speed setting you want
def get_speed():
    np1 = int(input("Nozzle placement variable, default is 0, + Number is farther away, - is closer to wheel. "))
    heat = float(input("what is the heat? "))
    speed = float((heat - (260 + np1))/90)
    
    print("Speed =",speed, "M/m")

def m1055():
    while True:
        try:
            intro = input("Do you want the Heat or the Speed? ")

            if intro in ["heat", "Heat"]:
                get_heat()
                break
            elif intro in ["speed", "Speed"]:
                get_speed()
                break
            else:
                print("Wrong input, try typing heat or speed")
        except ValueError:
                print("Try typing in a speed from 1-3.5 or heat from 380-600")

#Material 1055 tape settings

# function to get the heat setting you want
def get_heatt():
    np1 = int(input("Nozzle placement variable, default is 0, + Number is farther away, - is closer to wheel. "))
    speed = float(input("What is the speed? "))
    temp = 270 + np1 + (speed * 90)

    print("Heat =", temp, "Celsius")


# function to get the speed setting you want
def get_speedt():
    np1 = int(input("Nozzle placement variable, default is 0, + Number is farther away, - is closer to wheel. "))
    heat = float(input("what is the heat? "))
    speed = float((heat - (270 + np1)) / 90)

    print("Speed =", speed, "M/m")


def m1055t():
    while True:
        try:
            intro = input("Do you want the Heat or the Speed? ")

            if intro in ["heat", "Heat"]:
                get_heatt()
                break
            elif intro in ["speed", "Speed"]:
                get_speedt()
                break
            else:
                print("Wrong input, try typing heat or speed")
        except ValueError:
            print("Try typing in a speed from 1-3.5 or heat from 380-600")

def graph1055():
    xpoints = np.array([350,530])
    ypoints = np.array([1,3])

    plt.plot(xpoints, ypoints)
    plt.show()

#Material 4090 settings

# function to get the heat setting Parameters
def get_heat4090():
    np1 = int(input("Nozzle placement variable, default is 0, + Number is farther away, - is closer to wheel. "))
    speed = float(input("What is the speed? "))
    temp = 345 + np1 + (speed * 90)

    print("Heat =",temp, "Celsius")


# function to get the speed setting Parameters
def get_speed4090():
    np1 = int(input("Nozzle placement variable, default is 0, + Number is farther away, - is closer to wheel. "))
    heat = float(input("what is the heat? "))
    speed = float((heat - (345 + np1)) / 90)

    print("Speed =",speed, "M/m")

#Material 4090 function
def m4090():
    while True:
        try:
            intro = input("Do you want the Heat or the Speed? ")
            if intro in ["heat", "Heat"]:
                get_heat4090()
                break
            elif intro in ["speed", "Speed"]:
                get_speed4090()
                break
            else:
                print("Wrong input, try typing heat or speed")
        except ValueError:
                print("Try typing in a speed from 1-3.5 or heat from 380-600")

def graph4090():
    xpoints = np.array([435,615])
    ypoints = np.array([1,3])

    plt.plot(xpoints, ypoints)
    plt.show()

# 20oz vinyl settings
#function to get the heat settings
def get_heatv():
    np1 = int(input("Nozzle placement variable, default is 0, + Number is farther away, - is closer to wheel. "))
    speed = float(input("What is the speed? "))
    temp = 285 + np1 + (speed * 90)

    print("Heat =", temp, "Celsius")

def get_speedv():
    np2 = int(input("Nozzle placement variable, default is 0, + Number is farther away, - is closer to wheel. "))
    heat = float(input("what is the heat? "))
    speed = float((heat - (285 + np2)) / 90)

    print("Speed =", speed, "M/m")


def vinyl():
    while True:
        try:
            intro = input("Do you want the Heat or the Speed? ")

            if intro in ["heat", "Heat"]:
                get_heatv()
                break
            elif intro in ["speed", "Speed"]:
                get_speedv()
                break
            else:
                print("Wrong input, try typing heat or speed")
        except ValueError:
            print("Try typing in a speed from 1-3.5 or heat from 380-600")


# start of program
def main():
    while True:
        material = input("What material are you using? 1055, 1055t, 4090, vinyl. use xxxxgraph for graph. ")
        if material == "1055":
                m1055()
                break
        elif material == "1055t":
                m1055t()
                break
        elif material == "vinyl":
                vinyl()
                break
        elif material == "1055graph":
                graph1055()
                break
        elif material == "4090":
                m4090()
                break
        elif material == "4090graph":
                graph4090()
                break
        else:
            print("use 1055, 1055t, 4090, vinyl.")


main()

