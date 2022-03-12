import time
import os
os.system('clear')
file_name = input("Enter file name")
f = open(file_name,"r")
big_string = f.read()
big_array = big_string.split('==')
for i in big_array:
    print(i)
    time.sleep(0.1)
    print("\033[%d;%dH" % (0, 0))

