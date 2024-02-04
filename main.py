from flask import Flask
import functions
import PySimpleGUI as sg

app = Flask(__name__)

@app.route("/")

def index():
    return

speedlabel = sg.Text("Speed: ")
speedinput = sg.InputText(tooltip="Enter the speed", enable_events=True, key="speed", size=(40,15))

heatlabel = sg.Text("Heat: ")
heatinput = sg.InputText(tooltip='Enter a temp', enable_events=True, key="heat", size=(40,15))

machineslabel = sg.Text("Machines: ")
machines = ['Machine 1','Machine 2', 'Machine 3', 'Machine 4']
machine_menu = sg.DropDown(machines, size=(10,15), enable_events=True, auto_size_text=True, key="machine")

materiallabel = sg.Text("Material: ")
material = ['955', '1055', '2051', '4090', 'vinyl']
material_menu = sg.DropDown(material, size=(10,15), enable_events=True, auto_size_text=True, key="material")

toslabel = sg.Text("Tape or Seam: ")
tos = ['Tape', 'Seam']
tos_menu = sg.DropDown(tos, size=(10,15), enable_events=True, auto_size_text=True, key="tos")

window = sg.Window("CPI welding",
                   layout= [[machineslabel], [machine_menu],
                            [materiallabel], [material_menu],
                            [toslabel], [tos_menu],
                            [speedlabel], [speedinput],
                            [heatlabel], [heatinput]],
                   font=("Helvetica", 15))

# Machine 1 4090t formula needs to be updated
# Machine 2 is not calibrated
# Machine 3 is not calibrated only vinyl seam is ok
# Machine 4 is not calibrated
# tip** look at functionscli to see what was calibrated on last program


while True:
    event, values = window.Read()

#Machine 1

#955
    if values["machine"] == "Machine 1" and values["material"] == "955" and values["tos"] == "Seam":

            heat1 = values["heat"]

            speed1 = values["speed"]
            try:
                if event == "speed":
                    speed = float(speed1)
                    getheat = functions.get_heat955_1(speed)
                    values["heat"] = getheat
                    window["heat"].update(value=values["heat"])
                elif event == "heat":
                    heat = float(heat1)
                    getspeed = functions.get_speed955_1(heat)
                    values["speed"] = getspeed
                    window["speed"].update(value=values["speed"])


            except ValueError:
                continue

    elif values["machine"] == "Machine 1" and values["material"] == "955" and values["tos"] == "Tape":

            heat1 = values["heat"]

            speed1 = values["speed"]
            try:
                if event == "speed":
                    speed = float(speed1)
                    getheat = functions.get_heat955t_1(speed)
                    values["heat"] = getheat
                    window["heat"].update(value=values["heat"])
                elif event == "heat":
                    heat = float(heat1)
                    getspeed = functions.get_speed955t_1(heat)
                    values["speed"] = getspeed
                    window["speed"].update(value=values["speed"])
            except ValueError:
                continue
#1055
    if values["machine"] == "Machine 1" and values["material"] == "1055" and values["tos"] == "Seam":

            heat1 = values["heat"]

            speed1 = values["speed"]
            try:
                if event == "speed":
                    speed = float(speed1)
                    getheat = functions.get_heat1055_1(speed)
                    values["heat"] = getheat
                    window["heat"].update(value=values["heat"])
                elif event == "heat":
                    heat = float(heat1)
                    getspeed = functions.get_speed1055_1(heat)
                    values["speed"] = getspeed
                    window["speed"].update(value=values["speed"])
            except ValueError:
                continue

    elif values["machine"] == "Machine 1" and values["material"] == "1055" and values["tos"] == "Tape":

            heat1 = values["heat"]

            speed1 = values["speed"]
            try:
                if event == "speed":
                    speed = float(speed1)
                    getheat = functions.get_heat1055t_1(speed)
                    values["heat"] = getheat
                    window["heat"].update(value=values["heat"])
                elif event == "heat":
                    heat = float(heat1)
                    getspeed = functions.get_speed1055t_1(heat)
                    values["speed"] = getspeed
                    window["speed"].update(value=values["speed"])
            except ValueError:
                continue

#2051
    if values["machine"] == "Machine 1" and values["material"] == "2051" and values["tos"] == "Seam":

            heat1 = values["heat"]

            speed1 = values["speed"]
            try:
                if event == "speed":
                    speed = float(speed1)
                    getheat = functions.get_heat1055_1(speed)
                    values["heat"] = getheat
                    window["heat"].update(value=values["heat"])
                elif event == "heat":
                    heat = float(heat1)
                    getspeed = functions.get_speed1055_1(heat)
                    values["speed"] = getspeed
                    window["speed"].update(value=values["speed"])
            except ValueError:
                continue

    elif values["machine"] == "Machine 1" and values["material"] == "2051" and values["tos"] == "Tape":

            heat1 = values["heat"]

            speed1 = values["speed"]
            try:
                if event == "speed":
                    speed = float(speed1)
                    getheat = functions.get_heat2051t_1(speed)
                    values["heat"] = getheat
                    window["heat"].update(value=values["heat"])
                elif event == "heat":
                    heat = float(heat1)
                    getspeed = functions.get_speed2051t_1(heat)
                    values["speed"] = getspeed
                    window["speed"].update(value=values["speed"])
            except ValueError:
                continue

#4090
    elif values["machine"] == "Machine 1" and values["material"] == "4090" and values["tos"] == "Seam":

            heat1 = values["heat"]

            speed1 = values["speed"]
            try:
                if event == "speed":
                    speed = float(speed1)
                    getheat = functions.get_heat4090_1(speed)
                    values["heat"] = getheat
                    window["heat"].update(value=values["heat"])
                elif event == "heat":
                    heat = float(heat1)
                    getspeed = functions.get_speed4090_1(heat)
                    values["speed"] = getspeed
                    window["speed"].update(value=values["speed"])
            except ValueError:
                continue

    elif values["machine"] == "Machine 1" and values["material"] == "4090" and values["tos"] == "Tape":

        heat1 = values["heat"]

        speed1 = values["speed"]
        try:
            if event == "speed":
                speed = float(speed1)
                getheat = functions.get_heat4090t_1(speed)
                values["heat"] = getheat
                window["heat"].update(value=values["heat"])
            elif event == "heat":
                heat = float(heat1)
                getspeed = functions.get_speed4090t_1(heat)
                values["speed"] = getspeed
                window["speed"].update(value=values["speed"])
        except ValueError:
            continue

#Vinyl
    elif values["machine"] == "Machine 1" and values["material"] == "vinyl" and values["tos"] == "Seam":

            heat1 = values["heat"]

            speed1 = values["speed"]
            try:
                if event == "speed":
                    speed = float(speed1)
                    getheat = functions.get_heatvinyl_1(speed)
                    values["heat"] = getheat
                    window["heat"].update(value=values["heat"])
                elif event == "heat":
                    heat = float(heat1)
                    getspeed = functions.get_speedvinyl_1(heat)
                    values["speed"] = getspeed
                    window["speed"].update(value=values["speed"])
            except ValueError:
                continue

    elif values["machine"] == "Machine 1" and values["material"] == "vinyl" and values["tos"] == "Tape":

            heat1 = values["heat"]

            speed1 = values["speed"]
            try:
                if event == "speed":
                    speed = float(speed1)
                    getheat = functions.get_heatvinylt_1(speed)
                    values["heat"] = getheat
                    window["heat"].update(value=values["heat"])
                elif event == "heat":
                    heat = float(heat1)
                    getspeed = functions.get_speedvinylt_1(heat)
                    values["speed"] = getspeed
                    window["speed"].update(value=values["speed"])
            except ValueError:
                continue

#Machine 2
    # 955
    if values["machine"] == "Machine 2" and values["material"] == "955" and values["tos"] == "Seam":

        heat1 = values["heat"]

        speed1 = values["speed"]
        try:
            if event == "speed":
                speed = float(speed1)
                getheat = functions.get_heat955_1(speed)
                values["heat"] = getheat
                window["heat"].update(value=values["heat"])
            elif event == "heat":
                heat = float(heat1)
                getspeed = functions.get_speed955_1(heat)
                values["speed"] = getspeed
                window["speed"].update(value=values["speed"])
        except ValueError:
            continue

    elif values["machine"] == "Machine 2" and values["material"] == "955" and values["tos"] == "Tape":

        heat1 = values["heat"]

        speed1 = values["speed"]
        try:
            if event == "speed":
                speed = float(speed1)
                getheat = functions.get_heat955t_1(speed)
                values["heat"] = getheat
                window["heat"].update(value=values["heat"])
            elif event == "heat":
                heat = float(heat1)
                getspeed = functions.get_speed955t_1(heat)
                values["speed"] = getspeed
                window["speed"].update(value=values["speed"])
        except ValueError:
            continue
        # 1055
    if values["machine"] == "Machine 2" and values["material"] == "1055" and values["tos"] == "Seam":

        heat1 = values["heat"]

        speed1 = values["speed"]
        try:
            if event == "speed":
                speed = float(speed1)
                getheat = functions.get_heat1055_1(speed)
                values["heat"] = getheat
                window["heat"].update(value=values["heat"])
            elif event == "heat":
                heat = float(heat1)
                getspeed = functions.get_speed1055_1(heat)
                values["speed"] = getspeed
                window["speed"].update(value=values["speed"])
        except ValueError:
            continue

    elif values["machine"] == "Machine 2" and values["material"] == "1055" and values["tos"] == "Tape":

        heat1 = values["heat"]

        speed1 = values["speed"]
        try:
            if event == "speed":
                speed = float(speed1)
                getheat = functions.get_heat1055t_1(speed)
                values["heat"] = getheat
                window["heat"].update(value=values["heat"])
            elif event == "heat":
                heat = float(heat1)
                getspeed = functions.get_speed1055t_1(heat)
                values["speed"] = getspeed
                window["speed"].update(value=values["speed"])
        except ValueError:
            continue

        # 2051
    if values["machine"] == "Machine 2" and values["material"] == "2051" and values["tos"] == "Seam":

        heat1 = values["heat"]

        speed1 = values["speed"]
        try:
            if event == "speed":
                speed = float(speed1)
                getheat = functions.get_heat1055_1(speed)
                values["heat"] = getheat
                window["heat"].update(value=values["heat"])
            elif event == "heat":
                heat = float(heat1)
                getspeed = functions.get_speed1055_1(heat)
                values["speed"] = getspeed
                window["speed"].update(value=values["speed"])
        except ValueError:
            continue

    elif values["machine"] == "Machine 2" and values["material"] == "2051" and values["tos"] == "Tape":

        heat1 = values["heat"]

        speed1 = values["speed"]
        try:
            if event == "speed":
                speed = float(speed1)
                getheat = functions.get_heat2051t_1(speed)
                values["heat"] = getheat
                window["heat"].update(value=values["heat"])
            elif event == "heat":
                heat = float(heat1)
                getspeed = functions.get_speed2051t_1(heat)
                values["speed"] = getspeed
                window["speed"].update(value=values["speed"])
        except ValueError:
            continue

        # 4090
    elif values["machine"] == "Machine 2" and values["material"] == "4090" and values["tos"] == "Seam":

        heat1 = values["heat"]

        speed1 = values["speed"]
        try:
            if event == "speed":
                speed = float(speed1)
                getheat = functions.get_heat4090_1(speed)
                values["heat"] = getheat
                window["heat"].update(value=values["heat"])
            elif event == "heat":
                heat = float(heat1)
                getspeed = functions.get_speed4090_1(heat)
                values["speed"] = getspeed
                window["speed"].update(value=values["speed"])
        except ValueError:
            continue

    elif values["machine"] == "Machine 2" and values["material"] == "4090" and values["tos"] == "Tape":

        heat1 = values["heat"]

        speed1 = values["speed"]
        try:
            if event == "speed":
                speed = float(speed1)
                getheat = functions.get_heat4090t_1(speed)
                values["heat"] = getheat
                window["heat"].update(value=values["heat"])
            elif event == "heat":
                heat = float(heat1)
                getspeed = functions.get_speed4090t_1(heat)
                values["speed"] = getspeed
                window["speed"].update(value=values["speed"])
        except ValueError:
            continue

        # Vinyl
    elif values["machine"] == "Machine 2" and values["material"] == "vinyl" and values["tos"] == "Seam":

        heat1 = values["heat"]

        speed1 = values["speed"]
        try:
            if event == "speed":
                speed = float(speed1)
                getheat = functions.get_heatvinyl_1(speed)
                values["heat"] = getheat
                window["heat"].update(value=values["heat"])
            elif event == "heat":
                heat = float(heat1)
                getspeed = functions.get_speedvinyl_1(heat)
                values["speed"] = getspeed
                window["speed"].update(value=values["speed"])
        except ValueError:
            continue

    elif values["machine"] == "Machine 2" and values["material"] == "vinyl" and values["tos"] == "Tape":

        heat1 = values["heat"]

        speed1 = values["speed"]
        try:
            if event == "speed":
                speed = float(speed1)
                getheat = functions.get_heatvinylt_1(speed)
                values["heat"] = getheat
                window["heat"].update(value=values["heat"])
            elif event == "heat":
                heat = float(heat1)
                getspeed = functions.get_speedvinylt_1(heat)
                values["speed"] = getspeed
                window["speed"].update(value=values["speed"])
        except ValueError:
            continue


#Machine 3
    # 955
    if values["machine"] == "Machine 3" and values["material"] == "955" and values["tos"] == "Seam":

        heat1 = values["heat"]

        speed1 = values["speed"]
        try:
            if event == "speed":
                speed = float(speed1)
                getheat = functions.get_heat955_1(speed)
                values["heat"] = getheat
                window["heat"].update(value=values["heat"])
            elif event == "heat":
                heat = float(heat1)
                getspeed = functions.get_speed955_1(heat)
                values["speed"] = getspeed
                window["speed"].update(value=values["speed"])
        except ValueError:
            continue

    elif values["machine"] == "Machine 3" and values["material"] == "955" and values["tos"] == "Tape":

        heat1 = values["heat"]

        speed1 = values["speed"]
        try:
            if event == "speed":
                speed = float(speed1)
                getheat = functions.get_heat955t_1(speed)
                values["heat"] = getheat
                window["heat"].update(value=values["heat"])
            elif event == "heat":
                heat = float(heat1)
                getspeed = functions.get_speed955t_1(heat)
                values["speed"] = getspeed
                window["speed"].update(value=values["speed"])
        except ValueError:
            continue
    # 1055
    if values["machine"] == "Machine 3" and values["material"] == "1055" and values["tos"] == "Seam":

        heat1 = values["heat"]

        speed1 = values["speed"]
        try:
            if event == "speed":
                speed = float(speed1)
                getheat = functions.get_heat1055_1(speed)
                values["heat"] = getheat
                window["heat"].update(value=values["heat"])
            elif event == "heat":
                heat = float(heat1)
                getspeed = functions.get_speed1055_1(heat)
                values["speed"] = getspeed
                window["speed"].update(value=values["speed"])
        except ValueError:
            continue

    elif values["machine"] == "Machine 3" and values["material"] == "1055" and values["tos"] == "Tape":

        heat1 = values["heat"]

        speed1 = values["speed"]
        try:
            if event == "speed":
                speed = float(speed1)
                getheat = functions.get_heat1055t_1(speed)
                values["heat"] = getheat
                window["heat"].update(value=values["heat"])
            elif event == "heat":
                heat = float(heat1)
                getspeed = functions.get_speed1055t_1(heat)
                values["speed"] = getspeed
                window["speed"].update(value=values["speed"])
        except ValueError:
            continue

    # 2051
    if values["machine"] == "Machine 3" and values["material"] == "2051" and values["tos"] == "Seam":

        heat1 = values["heat"]

        speed1 = values["speed"]
        try:
            if event == "speed":
                speed = float(speed1)
                getheat = functions.get_heat1055_1(speed)
                values["heat"] = getheat
                window["heat"].update(value=values["heat"])
            elif event == "heat":
                heat = float(heat1)
                getspeed = functions.get_speed1055_1(heat)
                values["speed"] = getspeed
                window["speed"].update(value=values["speed"])
        except ValueError:
            continue

    elif values["machine"] == "Machine 3" and values["material"] == "2051" and values["tos"] == "Tape":

        heat1 = values["heat"]

        speed1 = values["speed"]
        try:
            if event == "speed":
                speed = float(speed1)
                getheat = functions.get_heat2051t_1(speed)
                values["heat"] = getheat
                window["heat"].update(value=values["heat"])
            elif event == "heat":
                heat = float(heat1)
                getspeed = functions.get_speed2051t_1(heat)
                values["speed"] = getspeed
                window["speed"].update(value=values["speed"])
        except ValueError:
            continue

    # 4090
    elif values["machine"] == "Machine 3" and values["material"] == "4090" and values["tos"] == "Seam":

        heat1 = values["heat"]

        speed1 = values["speed"]
        try:
            if event == "speed":
                speed = float(speed1)
                getheat = functions.get_heat4090_1(speed)
                values["heat"] = getheat
                window["heat"].update(value=values["heat"])
            elif event == "heat":
                heat = float(heat1)
                getspeed = functions.get_speed4090_1(heat)
                values["speed"] = getspeed
                window["speed"].update(value=values["speed"])
        except ValueError:
            continue

    elif values["machine"] == "Machine 3" and values["material"] == "4090" and values["tos"] == "Tape":

        heat1 = values["heat"]

        speed1 = values["speed"]
        try:
            if event == "speed":
                speed = float(speed1)
                getheat = functions.get_heat4090t_1(speed)
                values["heat"] = getheat
                window["heat"].update(value=values["heat"])
            elif event == "heat":
                heat = float(heat1)
                getspeed = functions.get_speed4090t_1(heat)
                values["speed"] = getspeed
                window["speed"].update(value=values["speed"])
        except ValueError:
            continue

# Vinyl

    elif values["machine"] == "Machine 3" and values["material"] == "vinyl" and values["tos"] == "Seam":

        heat1 = values["heat"]

        speed1 = values["speed"]
        try:
            if event == "speed":
                speed = float(speed1)
                getheat = functions.get_heatvinyl_3(speed)
                values["heat"] = getheat
                window["heat"].update(value=values["heat"])
            elif event == "heat":
                heat = float(heat1)
                getspeed = functions.get_speedvinyl_3(heat)
                values["speed"] = getspeed
                window["speed"].update(value=values["speed"])
        except ValueError:
            continue

    elif values["machine"] == "Machine 3" and values["material"] == "vinyl" and values["tos"] == "Tape":

        heat1 = values["heat"]

        speed1 = values["speed"]
        try:
            if event == "speed":
                speed = float(speed1)
                getheat = functions.get_heatvinylt_1(speed)
                values["heat"] = getheat
                window["heat"].update(value=values["heat"])
            elif event == "heat":
                heat = float(heat1)
                getspeed = functions.get_speedvinylt_1(heat)
                values["speed"] = getspeed
                window["speed"].update(value=values["speed"])
        except ValueError:
            continue



#Machine 4
    # 955
    if values["machine"] == "Machine 4" and values["material"] == "955" and values["tos"] == "Seam":

        heat1 = values["heat"]

        speed1 = values["speed"]
        try:
            if event == "speed":
                speed = float(speed1)
                getheat = functions.get_heat955_1(speed)
                values["heat"] = getheat
                window["heat"].update(value=values["heat"])
            elif event == "heat":
                heat = float(heat1)
                getspeed = functions.get_speed955_1(heat)
                values["speed"] = getspeed
                window["speed"].update(value=values["speed"])
        except ValueError:
            continue

    elif values["machine"] == "Machine 4" and values["material"] == "955" and values["tos"] == "Tape":

        heat1 = values["heat"]

        speed1 = values["speed"]
        try:
            if event == "speed":
                speed = float(speed1)
                getheat = functions.get_heat955t_1(speed)
                values["heat"] = getheat
                window["heat"].update(value=values["heat"])
            elif event == "heat":
                heat = float(heat1)
                getspeed = functions.get_speed955t_1(heat)
                values["speed"] = getspeed
                window["speed"].update(value=values["speed"])
        except ValueError:
            continue
        # 1055
    if values["machine"] == "Machine 4" and values["material"] == "1055" and values["tos"] == "Seam":

        heat1 = values["heat"]

        speed1 = values["speed"]
        try:
            if event == "speed":
                speed = float(speed1)
                getheat = functions.get_heat1055_1(speed)
                values["heat"] = getheat
                window["heat"].update(value=values["heat"])
            elif event == "heat":
                heat = float(heat1)
                getspeed = functions.get_speed1055_1(heat)
                values["speed"] = getspeed
                window["speed"].update(value=values["speed"])
        except ValueError:
            continue

    elif values["machine"] == "Machine 4" and values["material"] == "1055" and values["tos"] == "Tape":

        heat1 = values["heat"]

        speed1 = values["speed"]
        try:
            if event == "speed":
                speed = float(speed1)
                getheat = functions.get_heat1055t_1(speed)
                values["heat"] = getheat
                window["heat"].update(value=values["heat"])
            elif event == "heat":
                heat = float(heat1)
                getspeed = functions.get_speed1055t_1(heat)
                values["speed"] = getspeed
                window["speed"].update(value=values["speed"])
        except ValueError:
            continue

        # 2051
    if values["machine"] == "Machine 4" and values["material"] == "2051" and values["tos"] == "Seam":

        heat1 = values["heat"]

        speed1 = values["speed"]
        try:
            if event == "speed":
                speed = float(speed1)
                getheat = functions.get_heat1055_1(speed)
                values["heat"] = getheat
                window["heat"].update(value=values["heat"])
            elif event == "heat":
                heat = float(heat1)
                getspeed = functions.get_speed1055_1(heat)
                values["speed"] = getspeed
                window["speed"].update(value=values["speed"])
        except ValueError:
            continue

    elif values["machine"] == "Machine 4" and values["material"] == "2051" and values["tos"] == "Tape":

        heat1 = values["heat"]

        speed1 = values["speed"]
        try:
            if event == "speed":
                speed = float(speed1)
                getheat = functions.get_heat2051t_1(speed)
                values["heat"] = getheat
                window["heat"].update(value=values["heat"])
            elif event == "heat":
                heat = float(heat1)
                getspeed = functions.get_speed2051t_1(heat)
                values["speed"] = getspeed
                window["speed"].update(value=values["speed"])
        except ValueError:
            continue

        # 4090
    elif values["machine"] == "Machine 4" and values["material"] == "4090" and values["tos"] == "Seam":

        heat1 = values["heat"]

        speed1 = values["speed"]
        try:
            if event == "speed":
                speed = float(speed1)
                getheat = functions.get_heat4090_1(speed)
                values["heat"] = getheat
                window["heat"].update(value=values["heat"])
            elif event == "heat":
                heat = float(heat1)
                getspeed = functions.get_speed4090_1(heat)
                values["speed"] = getspeed
                window["speed"].update(value=values["speed"])
        except ValueError:
            continue

    elif values["machine"] == "Machine 4" and values["material"] == "4090" and values["tos"] == "Tape":

        heat1 = values["heat"]

        speed1 = values["speed"]
        try:
            if event == "speed":
                speed = float(speed1)
                getheat = functions.get_heat4090t_1(speed)
                values["heat"] = getheat
                window["heat"].update(value=values["heat"])
            elif event == "heat":
                heat = float(heat1)
                getspeed = functions.get_speed4090t_1(heat)
                values["speed"] = getspeed
                window["speed"].update(value=values["speed"])
        except ValueError:
            continue

        # Vinyl
    elif values["machine"] == "Machine 4" and values["material"] == "vinyl" and values["tos"] == "Seam":

        heat1 = values["heat"]

        speed1 = values["speed"]
        try:
            if event == "speed":
                speed = float(speed1)
                getheat = functions.get_heatvinyl_1(speed)
                values["heat"] = getheat
                window["heat"].update(value=values["heat"])
            elif event == "heat":
                heat = float(heat1)
                getspeed = functions.get_speedvinyl_1(heat)
                values["speed"] = getspeed
                window["speed"].update(value=values["speed"])
        except ValueError:
            continue

    elif values["machine"] == "Machine 4" and values["material"] == "vinyl" and values["tos"] == "Tape":

        heat1 = values["heat"]

        speed1 = values["speed"]
        try:
            if event == "speed":
                speed = float(speed1)
                getheat = functions.get_heatvinylt_1(speed)
                values["heat"] = getheat
                window["heat"].update(value=values["heat"])
            elif event == "heat":
                heat = float(heat1)
                getspeed = functions.get_speedvinylt_1(heat)
                values["speed"] = getspeed
                window["speed"].update(value=values["speed"])
        except ValueError:
            continue

#show events and there values
#    print(event)
#    print(values)


window.close()

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)