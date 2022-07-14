import requests
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

class Bored():
    def __init__(self):
        self.minimum = []
        self.maximum = []

    def create_activity(self):
        
        x = input("What is your minimum price range from 0-1? ")
        y = input("What is your maximum price range? Must be larger than min. ")
        self.minimum.append(x)
        self.maximum.append(y)
        
        response=requests.get(f'http://www.boredapi.com/api/activity?minprice={self.minimum[0]}.5&maxprice={self.maximum[0]}')
        if not response.ok:
            return False
        data = response.json()
        print("="*40)
        print(Fore.BLUE + Style.BRIGHT + f"Activity: {data['activity']}") 
        print(Fore.RED + Style.BRIGHT + f"\nType of Activity: {data['type']}")
        print(Fore.YELLOW + Style.BRIGHT + f"\nParticipants: {data['participants']}")
        print(Fore.GREEN + Style.BRIGHT + f"\nPrice: {data['price']}")
        print("="*40)




bored = Bored()
def main():
    while True:
        prompt = input("Are you bored? ")
        if prompt[0].lower() == "y":
            bored.create_activity()
        if prompt[0].lower() == "q":
            return ('Have Fun Out There...')

print(main())


    