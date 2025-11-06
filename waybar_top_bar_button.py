import subprocess
from time import sleep
def main():
    cache = "/home/ranger/Github/Scripts/cache2.txt"
    with open(cache, 'r') as file_cache:
        BoolValue = file_cache.readline().strip()
        if BoolValue == "false":
            subprocess.Popen(["pkill" , "waybar"])
            sleep(0.1)
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/config.jsonc", "-s", "/home/ranger/.config/waybar/style.css"])
            with open(cache, 'r') as file_cache:
                BoolValue = file_cache.readline().strip()
                BoolValue = "true"
            print(BoolValue)
            with open(cache, 'w') as file_cache:
                file_cache.writelines(BoolValue)

        elif BoolValue == "true":
            subprocess.Popen(["pkill" , "waybar"])
            sleep(0.1)
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/bottom_bar.jsonc", "-s", "/home/ranger/.config/waybar/bottom_bar.css"])
            with open(cache, 'r') as file_cache:
                BoolValue = file_cache.readline().strip()
                BoolValue = "false"
            print(BoolValue)
            with open(cache, 'w') as file_cache:
                file_cache.writelines(BoolValue)


main()