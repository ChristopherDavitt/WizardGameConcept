import numpy as np
import random
import sys, os, time

# Creating the Items for the game
weight_dict = {
    'Berry': 100, 'Alpine Nightshade': 100, 'Eagle Talon': 200,
    'Goat Horn': 300, 'Firefly': 100, 'Rabbit Foot': 100,
    'Honey': 100, 'Box Jelly': 100, 'Turtle Shell': 100,
    'Fish': 100, 'Snake Skin': 100,'Gator Scales': 100,'Copper': 100,
    'Iron': 100,'Bat Wings': 100,'Coal': 100,'Radioactive Mud': 100, 
    'Turtle Egg': 100
}

item_dict = {
    'Mountains': ['Alpine Nightshade', 'Eagle Talon', 'Goat Horn'],
    'Forest': ['Berry', 'Firefly', 'Rabbit Foot', 'Honey'],
    'Ocean': ['Box Jelly', 'Turtle Shell', 'Fish', 'Turtle Egg'],
    'Swamp': ['Snake Skin', 'Gator Scales'],
    'Caves': ['Copper', 'Iron', 'Bat Wings', 'Coal'],
    'Wasteland': ['Radioactive Mud'],
}

recipe_book = {
    'Potion of Regeneration': ['Berry', 'Root'],
    'Flask of Misfortune': ["Rabbits foot", 'Coal'],
    'Ale of Electricity': ['Copper', 'Firefly'],
    'Potion of Strength': ['Iron', 'Fish'],
    'Unstable Potion of Health': ['Radioactive Mud', 'Butterfly Wings'],
    'Slow Poison': ['Turtle Shell', 'Honey'],
    'Poison of Instant Death': ['Alpine Nightshade', 'Box Jellyfish'],
}

egg_list = (
    'Turtle Egg'
)

k = np.random.choice([2,3,4,5], 1, p=[0.1, 0.3, 0.45, 0.15])[0]
print(k)
sNumbers = random.choices(item_dict['Mountains'], weights=[weight_dict[num] for num in item_dict['Mountains']], k=k)
print(sNumbers)

class User:
    def __init__(self, username, quest_time, items={}, potions={}, pets={}, eggs={}, nursery=[]):
        self.username = username
        self.items = items
        self.eggs = eggs
        self.nursery = nursery
        self.potions = potions
        self.pets= pets
        self.quest_time = quest_time

    def quest(self, loc):
        k = np.random.choice([2,3,4,5], 1, p=[0.1, 0.3, 0.45, 0.15])[0]
        new_items = random.choices(item_dict[loc], weights=[weight_dict[num] for num in item_dict[loc]], k=k)
        print("Items found during quest!")
        for item in new_items:
            time.sleep(1)
            print("  - " + item)
            
            if item not in self.items:
                self.items[item] = 1
            else:
                self.items[item] += 1
    
    def showItems(self):
        print("Items")
        print("-------------")
        for key, value in self.items.items():
            print("  - " + key + ": " + str(value))

    def showPotions(self):
        print("Potions")
        print("-------------")
        for key, value in self.potions.items():
            print("  - " + key + ": " + str(value))

    def showPets(self):
        print("Pets")
        print("-------------")
        for key, value in self.pets.items():
            print("  - " + key + ": " + str(value))

    def showPets(self):
        print("Eggs")
        print("-------------")
        for key, value in self.eggs.items():
            print("  - " + key + ": " + str(value))

    def showNursery(self):
        print("Nursery")
        print("-------------")
        for egg in self.nursery:
            print("  - " + egg)

def show_inventory():
    while True:
        print("""
            Which inventory would you like to see?
            -------------------
            [1] Items
            [2] Potions
            [3] Pets
            [4] Eggs
            [5] EXIT
            --------------------
            """)
        res = input(": ")
        if res.lower().strip() == '1':
            user.showItems()
            exit_await = input("Press [enter] to go back...")
            continue
        if res.lower().strip() == '2':
            user.showPotions()
            exit_await = input("Press [enter] to go back...")
            continue
        if res.lower().strip() == '3':
            user.showPets()
            exit_await = input("Press [enter] to go back...")
            continue
        if res.lower().strip() == '4':
            user.showEggs()
            exit_await = input("Press [enter] to go back...")
        if res.lower().strip() == '5':
            break

def nursery():
    user.showNursery()
    while True:
        
        if len(user.nursery) >= 3:
            print('Nursery Full...')
            time.sleep(2)
            break
        if len(user.nursery) == 0:
            print("No Eggs in Inventory... \nCome back later")
            time.sleep(2)
            break
        else:
            res = input("""
            Would you like to put an egg in the NURSERY? 
            [1] YES
            [2] NO
            : 
            """)
            l1 = []
            i = 0
            if res == '1':
                print('Which EGG Would you like to add')
                for item in user.eggs.keys():
                    l1.append(item)
                    print(f"{[i]} {item}")
                    i += 1
                res2 = input(': ')
                try:
                    if int(res2) >= 0 and int(res2) < len(l1):
                        print(f"{l1[int(res2)]} added successfully!")
                        print('Egg will hatch in approximately 2 minutes')
                        user.nursery.append((l1[int(res2)], time.time_ns + 12000000000))
                        user.eggs[l1[int(res2)]] -= 1
                        if user.eggs[l1[int(res2)]] == 0:
                            del user.eggs[l1[int(res2)]]
                        continue
                    else:
                        print('Not a valid number... Try again')
                        continue

                except:
                        print('Not a valid number... Try again')
                        continue
            elif res == '2':
                print('Come back soon!')
                break
            else:
                print('Not a valid command... Try again')
                continue
                
def make_potion():
    while True:
        print("""
            What potion would you like to brew?
            -------------------
            [1] Coming Soon
            --------------------
            """)
        time.sleep(2)
        # Still need to make this optimal
        break

def quest_option():
    while True:
        if time.time_ns() < user.quest_time:
            print("You need a rest from your last quest...")
            print(f"Time Remaining: {int((user.quest_time - time.time_ns())/1000000000)} seconds")
            break

        else:
            print("""
            Select Location?
            -------------------
            [1] Mountains
            [2] Forest
            [3] Ocean
            [4] Swamp 
            [5] Wasteland
            [6] Caves
            [7] EXIT
            --------------------
            """)
            res = input(": ")
            if res.lower().strip() == '1':
                user.quest_time = time.time_ns() + 60000000000
                user.quest('Mountains')
                break
            if res.lower().strip() == '2':
                user.quest_time = time.time_ns() + 60000000000
                user.quest('Forest')
                break
            if res.lower().strip() == '3':
                user.quest_time = time.time_ns() + 60000000000
                user.quest('Ocean')
                break
            if res.lower().strip() == '4':
                user.quest_time = time.time_ns() + 60000000000
                user.quest('Swamp')
                break
            if res.lower().strip() == '5':
                user.quest_time = time.time_ns() + 60000000000
                user.quest('Wasteland')
                break
            if res.lower().strip() == '6':
                user.quest_time = time.time_ns() + 60000000000
                user.quest('Caves')
                break
            if res.lower().strip() == '7':
                break

running = True
# Initializing The New Player
username = input("What is your name... ")
print(f"Welcome {username} to your new world of adventure.")
user = User(username, time.time_ns())

# Starting Game
while running:
    print(
        """
        [1] Go on a Quest
        [2] Check your Inventory
        [3] Check out the Nursery
        [4] Brew some Potions
        """
    )

    res = input("What would you like to do? ")
    if res == '1':
        quest_option()
    if res == '2':
        show_inventory()
    if res == '3':
        nursery()
    if res == '4 ':
        make_potion()



