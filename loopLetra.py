# string letra por letra

import time as t
import os

string = input('\tInsira uma palavra\n\t-> ')
x = 0

for i in string:
    x += 1
    os.system('clear')
    print('\n\n\t',string[0:x])
    t.sleep(0.2)

print('\n\n')