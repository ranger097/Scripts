import subprocess
from time import sleep

def main():
    cache = "/home/ranger/Github/Scripts/cache4.txt"
    with open(cache, 'r') as file_cache:
        BoolValue = file_cache.readline().strip()
        if BoolValue == "false":
            
            subprocess.Popen(["pkill" , "waybar"])
            sleep(0.1)
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/side_bar_right.jsonc", "-s", "/home/ranger/.config/waybar/side_bar.css"])
            
            with open(cache, 'r') as file_cache:
                BoolValue = file_cache.readline().strip()
                BoolValue = "true"
            print(BoolValue)
            with open(cache, 'w') as file_cache:
                file_cache.writelines(BoolValue)

        elif BoolValue == "true":
            
            subprocess.Popen(["pkill" , "waybar"])
            sleep(0.1)
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/side_bar.jsonc", "-s", "/home/ranger/.config/waybar/side_bar.css"])
            
            with open(cache, 'r') as file_cache:
                BoolValue = file_cache.readline().strip()
                BoolValue = "false"
            print(BoolValue)
            with open(cache, 'w') as file_cache:
                file_cache.writelines(BoolValue)


main()