import subprocess

def main():
    cache = "/home/ranger/Github/Scripts/cache3.txt"
    with open(cache, 'r') as file_cache:
        BoolValue = file_cache.readline().strip()
        if BoolValue == "false":
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/bottom_bar.jsonc", "-s", "/home/ranger/.config/waybar/bottom_bar.css"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/config.jsonc", "-s", "/home/ranger/.config/waybar/style.css"])
            with open(cache, 'r') as file_cache:
                BoolValue = file_cache.readline().strip()
                BoolValue = "true"
            print(BoolValue)
            with open(cache, 'w') as file_cache:
                file_cache.writelines(BoolValue)

        elif BoolValue == "true":
            subprocess.run(["pkill", "waybar"])
            with open(cache, 'r') as file_cache:
                BoolValue = file_cache.readline().strip()
                BoolValue = "false"
            print(BoolValue)
            with open(cache, 'w') as file_cache:
                file_cache.writelines(BoolValue)


main()