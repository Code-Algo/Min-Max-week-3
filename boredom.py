import requests
import colorama
from colorama import Fore, Back, Style
colorama.init()

print(Fore.RED + 'some red text')

# if price > user input new activity



class Bored:
    def __init__(self):
        
        self.price =''
    
    
    def brian_eno_esque_game(self):
        response=requests.get(f'http://www.boredapi.com/api/activity?')
        if not response.ok:
            return False
        data = response.json()

        self.price = data['price']

        return response.json()



