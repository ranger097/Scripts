import subprocess
toggleFile = "/home/ranger/Github/Scripts/toggle.txt"

with open(toggleFile,"r") as file:
    x = file.readline()
    if x == "True":
        subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/top.jsonc", "-s", "/home/ranger/.config/waybar/top.css"])
        subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/bottom.jsonc", "-s", "/home/ranger/.config/waybar/bottom.css" ])
        with open(toggleFile,"w") as file:
            file.write("False")
    else:
        subprocess.run(["pkill","waybar"])
        with open(toggleFile,"w") as file:
            file.write("True")

