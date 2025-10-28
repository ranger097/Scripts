import subprocess

def main():
    cache = "/home/ranger/Scripts/cache2.txt"
    with open(cache, 'r') as file_cache:
        BoolValue = file_cache.readline().strip()
        if BoolValue == "false":
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/config.jsonc", "-s", "/home/ranger/.config/waybar/style.css"])
            with open(cache, 'r') as file_cache:
                BoolValue = file_cache.readline().strip()
                BoolValue = "true"
            print(BoolValue)
            with open(cache, 'w') as file_cache:
                file_cache.writelines(BoolValue)

        elif BoolValue == "true":
            subprocess.Popen(["pkill" , "waybar"])
            with open(cache, 'r') as file_cache:
                BoolValue = file_cache.readline().strip()
                BoolValue = "false"
            print(BoolValue)
            with open(cache, 'w') as file_cache:
                file_cache.writelines(BoolValue)


main()