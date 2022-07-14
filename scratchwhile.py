import requests
import colorama
from colorama import Fore, Back, Style
colorama.init()

url = 'http://www.boredapi.com/api/activity?'

response = requests.get(url)


class Bored():
    def __init__ (self):
        return
    
    def activity(self):
        


bored = Bored()
def main():
    while True:
        prompt = input("Are you bored?")
        if prompt == 'yes':
            return 
