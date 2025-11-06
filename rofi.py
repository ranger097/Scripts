import subprocess
from time import sleep

def main():
    cache = "/home/ranger/Github/Scripts/cache6.txt"
    with open(cache, 'r') as file_cache:
        BoolValue = file_cache.readline().strip()
        if BoolValue == "false":
            sleep(0.1)
            subprocess.Popen(["pkill" , "rofi"])
            
           
            with open(cache, 'r') as file_cache:
                BoolValue = file_cache.readline().strip()
                BoolValue = "true"
            print(BoolValue)
            with open(cache, 'w') as file_cache:
                file_cache.writelines(BoolValue)

        elif BoolValue == "true":
            
            sleep(0.1)
            subprocess.Popen(["rofi","-show","drun"])
            with open(cache, 'r') as file_cache:
                BoolValue = file_cache.readline().strip()
                BoolValue = "false"
            print(BoolValue)
            with open(cache, 'w') as file_cache:
                file_cache.writelines(BoolValue)


main()