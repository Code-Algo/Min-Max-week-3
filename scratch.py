import requests
import colorama
from colorama import Fore, Back, Style
colorama.init()
def create_activity(self):
    response=requests.get(f'http://www.boredapi.com/api/activity?minprice={self.minimum}.5&maxprice={self.maximum}')
    if not response.ok:
        return False

    data = response.json()

    activity = self.data['activity']
    type = self.data['type']
    participants = self.data['participants']
    price = self.data['price']
print(data)

    return True

    

    self.minimum = input("What is your min? ")
    self.maximum = input("What is your max? ")
    
    print(self.data['activity'])

