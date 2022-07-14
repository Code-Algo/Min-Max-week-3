 
import requests
import colorama
from colorama import Fore, Back, Style
colorama.init()

class Bored():
    def __init__(self):
        self.activity = ['activity']
        self.type = ['type']
        self.participants = ['participants']
        self.price = ['price']
        self.minimum = ''
        self.maximum = ''
    def min_max(self):
        return
    
    def create_activity(self):
        response=requests.get(f'http://www.boredapi.com/api/activity?minprice={self.minimum}.5&maxprice={self.maximum}')
        if not response.ok:
            return False
        self.data = response.json()

        
        self.activity = self.data['activity']
        self.type = self.data['type']
        self.participants = self.data['participants']
        self.price = self.data['price']
        print(self.data)
        

bored = Bored()
def main():
    while True:
        bored.minimum = input("What is your min? ")
        bored.maximum = input("What is your max? ")
        if bored.minimum or bored.maximum >= bored.price:
            bored.create_activity()
        else:
            return
        

print(main())

### I won't lie, been fiddling around for around 5 hours now and I've drafted and redrafted so much I'm not sure what to do.
## Will accept min 0 and max infinity, but if you mess with the min it errors.


    