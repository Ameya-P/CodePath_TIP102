# from collections import Counter


# class Villager:
#     def __init__(self, name, species, personality, catchphrase, neighbor=None):
#         self.name = name
#         self.species = species
#         self.personality = personality
#         self.catchphrase = catchphrase
#         self.furniture = []
#         self.neighbor = neighbor
    
#     def set_catchphrase(self, new_catchphrase):
#         valid = "".join(new_catchphrase.split())
#         if len(new_catchphrase) < 20 and valid.isalpha():
#             self.catchphrase = new_catchphrase
#             print("Catchphrase updated")
#         else:
#             print("Invalid catchphrase")
    
#     def greet_player(self, player_name):
#         return f"{self.name}: Hey there, {player_name}! How's it going, {self.catchphrase}!"
    
#     def add_item(self, item_name):
#         valid_items = ["acoustic guitar", "ironwood kitchenette", "rattan armchair", "kotatsu", "cacao tree"]
#         if item_name in valid_items:
#             self.furniture.append(item_name)
    
#     def print_inventory(self):
#         if not self.furniture:
#             print("Inventory empty")
#             return
        
#         counts = Counter(self.furniture)

#         result = ""

#         for key, value in counts.items():
#             result += key + ": " + str(value)  + ", "

#         print(result[:-2])
    
# def of_personality_type(townies, personality_type):
#     results = []

#     for villager in townies:
#         if villager.personality == personality_type:
#             results.append(villager.name)
    
#     return results

# def message_received(start_villager, target_villager):
#     current = start_villager
#     while current:
#         if current == target_villager:
#             return True
#         current = current.neighbor
    
#     return False

    

# apollo = Villager("Apollo", "Eagle", "pah")
# bones = Villager("Bones", "Dog", "yip yip")

# print(apollo.name)  
# print(apollo.species)  
# print(apollo.catchphrase) 
# print(apollo.furniture) 

# print(bones.greet_player("Ameya"))
# print(bones.name)
# print(bones.species)  
# print(bones.catchphrase) 
# print(bones.furniture) 

# bones.catchphrase = "ruff it up"
# print(bones.greet_player("Ameya"))

# alice = Villager("Alice", "Koala", "guvnor")

# alice.set_catchphrase("sweet dreams")
# print(alice.catchphrase)
# alice.set_catchphrase("#?!")
# print(alice.catchphrase)

# alice = Villager("Alice", "Koala", "guvnor")
# print(alice.furniture)

# alice.add_item("acoustic guitar")
# print(alice.furniture)

# alice.add_item("cacao tree")
# print(alice.furniture)

# alice.add_item("nintendo switch")
# print(alice.furniture)

# alice = Villager("Alice", "Koala", "guvnor")

# alice.print_inventory()

# alice.furniture = ["acoustic guitar", "ironwood kitchenette", "kotatsu", "kotatsu"]
# alice.print_inventory()

# isabelle = Villager("Isabelle", "Dog", "Normal", "what's up?")
# bob = Villager("Bob", "Cat", "Lazy", "pthhhpth")
# stitches = Villager("Stitches", "Cub", "Lazy", "stuffin'")

# print(of_personality_type([isabelle, bob, stitches], "Lazy"))
# print(of_personality_type([isabelle, bob, stitches], "Cranky"))

# isabelle = Villager("Isabelle", "Dog", "Normal", "what's up?")
# tom_nook = Villager("Tom Nook", "Raccoon", "Cranky", "yes, yes")
# kk_slider = Villager("K.K. Slider", "Dog", "Lazy", "dig it")
# isabelle.neighbor = tom_nook
# tom_nook.neighbor = kk_slider

# print(message_received(isabelle, kk_slider))
# print(message_received(kk_slider, isabelle))

# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next

# tom_nook = Node("Tom Nook")
# tommy = Node("Tommy")
# tom_nook.next = tommy
# timmy = Node("Timmy")

# tom_nook.next = timmy
# timmy.next = tommy
# saharah = Node("Saharah")

# tom_nook.next = None
# tommy.next = saharah

# print(tom_nook.next) 
# print(timmy.value) 
# print(timmy.next.value)  
# print(tommy.value) 
# print(tommy.next.value)
# print(saharah.value)  
# print(saharah.next) 

# def print_list(head):
#     result = ""

#     if not head:
#         return result
    
#     result += head.value

#     curr = head.next
#     while curr:
#         result += " -> " + curr.value
#         curr = curr.next
    
#     return result

# isabelle = Node("Isabelle")
# saharah = Node("Saharah")
# cj = Node("C.J.")

# isabelle.next = saharah
# saharah.next = cj

# print(print_list(isabelle))

from collections import Counter


class Player():
    def __init__(self, character, kart, opponent=None):
        self.character = character
        self.kart = kart
        self.items = []
        self.ahead = opponent
    
    def get_player(self):
        return f"{self.character} driving the {self.kart}"
    
    def set_character(self, name):
        valid = ["Mario", "Luigi", "Peach", "Yoshi", "Toad", "Wario", "Donkey Kong","Bowser"]
        if name in valid:
            self.character = name
            print("Character updated")
        else: 
            print("Invalid character")
    
    def add_item(self, item_name):
        valid = ["banana", "green shell", "red shell", "bob-omb", "super star", "lightning", "bullet bill"]
        if item_name in valid:
            self.items.append(item_name)
    
    def print_inventory(self):
        if not self.items:
            print("Inventory empty")
            return

        count = Counter(self.items)
        result = "Inventory: "
        for key, value in count.items():
            result += key + ": " + str(value) + ", "
        
        print(result[:-2])
    

def get_rank_iterative(my_player):
    rank = 1

    curr = my_player.ahead

    while curr:
        rank += 1
        curr = curr.ahead

    return rank

def get_rank(my_player):
    if not my_player.ahead:
        return 1

    return 1 + get_rank(my_player.ahead)

def print_results(race_results):
    for index, value in enumerate(race_results):
        print(f"{index + 1}. {value.character}")

# player_one = Player("Yoshi", "Super Blooper")
# player_two = Player("Bowser", "Pirahna Prowler")

# # print(player_one.character)
# # print(player_one.kart)
# # print(player_one.items)

# # player_one.kart = "Dolphin Dasher"

# # print(f"Match: {player_one.get_player()} vs {player_two.get_player()}")

# player_three = Player("Donkey Kong", "Standard Kart")

# player_three.set_character("Peach")
# print(player_three.character)
# player_three.set_character("Baby Peach")
# print(player_three.character)

# player_one = Player("Yoshi", "Dolphin Dasher")

# print(player_one.items)

# player_one.add_item("basketball")
# player_one.add_item("red shell")
# print(player_one.items)

# player_one.add_item("super star")
# print(player_one.items)

# player_one.add_item("super smash")
# print(player_one.items)

# player_one = Player("Yoshi", "Super Blooper")
# player_one.items = ["banana", "bob-omb", "banana", "super star"]
# player_two = Player("Peach", "Dolphin Dasher")

# player_one.print_inventory()
# player_two.print_inventory()

# peach = Player("Peach", "Daytripper")
# mario = Player("Mario", "Standard Kart M")
# luigi = Player("Luigi", "Super Blooper")
# race_one = [peach, mario, luigi]

# print_results(race_one)

peach = Player("Peach", "Daytripper")
mario = Player("Mario", "Standard Kart M", peach)
luigi = Player("Luigi", "Super Blooper", mario)

print(get_rank(luigi))
print(get_rank(peach))
print(get_rank(mario))

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

cat = Node("Tom")
mouse = Node("Jerry")
cat.next = mouse
dog = Node("Spike")
dog.next = cat
dog.next = None
cheese = Node("Gouda")
mouse.next = cheese

print(dog.value)
print(dog.next)
print(dog.next)
print(cat.next)
print(cat.next.value)
print(mouse.next)

def chase_list(head):
    result = head.value

    curr = head.next

    while curr:
        result += " chases " + curr.value
        curr = curr.next
    
    return result

dog = Node("Spike")
cat = Node("Tom")
mouse = Node("Jerry")
cheese = Node("Gouda")

dog.next = cat
cat.next = mouse
mouse.next = cheese

print(chase_list(dog))