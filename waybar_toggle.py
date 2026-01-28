import subprocess
toggleFile = "/home/ranger/Github/Scripts/toggle.txt"

with open(toggleFile,"r") as file:
    x = file.readline()
    if x == "1":
        subprocess.run(["pkill","waybar"])
        subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/top.jsonc", "-s", "/home/ranger/.config/waybar/top.css"])
        subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/bottom.jsonc", "-s", "/home/ranger/.config/waybar/bottom.css" ])
        with open(toggleFile,"w") as file:
            file.write("2")
    elif x == "2":
        subprocess.run(["pkill","waybar"])
        subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/left.jsonc", "-s", "/home/ranger/.config/waybar/left.css"])
        with open(toggleFile,"w") as file:
            file.write("3")
    elif x == "3":
        subprocess.run(["pkill","waybar"])
        subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/right.jsonc", "-s", "/home/ranger/.config/waybar/right.css"])
        with open(toggleFile,"w") as file:
            file.write("4")
    else:
        subprocess.run(["pkill","waybar"])
        with open(toggleFile,"w") as file:
            file.write("1")

