import requests
import colorama
from colorama import Fore, Back, Style
colorama.init()
        
minimum= []
maximum= []

x = input("What is your min? ")
y = input("What is your max? ")
mi = int(x)/100
ma = int(y)/100
minimum.append(mi)
maximum.append(ma)

print(minimum)
print(maximum)

