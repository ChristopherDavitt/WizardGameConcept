import numpy as np
import random
from time import time_ns, time

weight_dict = {
    'Berry': 100, 'Alpine Nightshade': 100, 'Eagle Talon': 200,
    'Goat Horn': 300, 'Firefly': 100, 'Rabbit Foot': 100,
    'Honey': 100, 'Box Jelly': 100, 'Turtle Shell': 100,
    'Fish': 100, 'Snake Skin': 100,'Gator Scales': 100,'Copper': 100,
    'Iron': 100,'Bat Wings': 100,'Coal': 100,'Radioactive Mud': 100,
}

item_dict = {
    'Mountains': ['Alpine Nightshade', 'Eagle Talon', 'Goat Horn'],
    'Forest': ['Berry', 'Firefly', 'Rabbit Foot', 'Honey'],
    'Ocean': ['Box Jelly', 'Turtle Shell', 'Fish'],
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
k = np.random.choice([2,3,4,5], 1, p=[0.1, 0.3, 0.45, 0.15])[0]
print(k)
sNumbers = random.choices(item_dict['Mountains'], weights=[weight_dict[num] for num in item_dict['Mountains']], k=k)
print(sNumbers)

class User:
    def __init__(self, username, quest_time, items={}, potions={}, pets={}, nursery=[],  experience=0):
        self.username = username
        self.items = items
        self.nursery = nursery
        self.potions = potions
        self.pets= pets
        self.quest_time = quest_time
        self.experience = experience

    def quest(self, loc):
        k = np.random.choice([2,3,4,5], 1, p=[0.1, 0.3, 0.45, 0.15])[0]
        new_items = random.choices(item_dict[loc], weights=[weight_dict[num] for num in item_dict[loc]], k=k)
        print("Items found during quest")
        for item in new_items:
            print("  - " + item)
            if item not in self.items:
                self.items[item] = 1
            else:
                self.items[item] += 1
    
    def showItems(self):
        print("Items")
        print("-------------")
        for key, value in self.items.items():
            print("  - " + key + ": " + value)

    def showPotions(self):
        print("Potions")
        print("-------------")
        for key, value in self.potions.items():
            print("  - " + key + ": " + value)

    def showPets(self):
        print("Pets")
        print("-------------")
        for key, value in self.pets.items():
            print("  - " + key + ": " + value)

    def showNursery(self):
        print("Nursery")
        print("-------------")
        for egg in self.nursery:
            print("  - " + egg)

def quest_option():
    while True:
        if time_ns() < user.quest_time:
            print("Still on Quest")
            print(f"Time Remaining: {int((user.quest_time - time_ns())/1000000000)} seconds")
            break
            
        else:
            print("""
            Go on a quest in the Mountains?
            [Y] Go on quest
            [N] Don't go on quest
            """)
            res = input(": ")
            if res.lower() == 'y':
                user.quest_time = time_ns() + 60000000000


running = True
# Initializing the new player
username = input("What is your name... ")
print(f"Welcome {username} to your new world of adventure.")
user = User(username, time_ns())
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
    # User can pick what they want to do
    if res == '1':
        if time_ns() < user.quest_time:
            print("Still on Quest")
            print(f"Time Remaining: {(user.quest_time - time_ns())/1000000000} seconds")
        else:
            print("""
            Go on a quest in the Mountains?
            [Y] Go on quest
            [N] Don't go on quest
            """)
            res = input(": ")
            if res.lower() == 'y':
                user.quest_time = time_ns() + 60000000000
    if res == '2':
        pass
    if res == '3':
        pass
    if res == '4 ':
        pass

