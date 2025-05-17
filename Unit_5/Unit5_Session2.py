# class Villager:
#     def __init__(self, name, species, catchphrase):
#         self.name = name
#         self.species = species
#         self.catchphrase = catchphrase
#         self.friends = []

#     def get_mutuals(self, new_contact):
#         my_friends = set(self.friends)
#         other_friends = set(new_contact.friends)
#         mutuals = my_friends & other_friends

#         results = []
#         for villager in mutuals:
#             results.append(villager.name)

#         return results
    
# bob = Villager("Bob", "Cat", "pthhhpth")
# marshal = Villager("Marshal", "Squirrel", "sulky")
# ankha = Villager("Ankha", "Cat", "me meow")
# fauna = Villager("Fauna", "Deer", "dearie")
# raymond = Villager("Raymond", "Cat", "crisp")
# stitches = Villager("Stitches", "Cub", "stuffin")

# bob.friends = [stitches, raymond, fauna]
# marshal.friends = [raymond, ankha, fauna]
# print(bob.get_mutuals(marshal))

# ankha.friends = [marshal]
# print(bob.get_mutuals(ankha))

# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next

# # For testing
# def print_linked_list(head):
#     current = head
#     while current:
#         print(current.value, end=" -> " if current.next else "\n")
#         current = current.next

# kk_slider = Node("K.K. Slider")
# harriet = Node("Harriet")
# saharah = Node("Saharah")
# isabelle = Node("Isabelle")

# kk_slider.next = harriet
# harriet.next = saharah
# saharah.next = isabelle

# print_linked_list(kk_slider)

# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next

# # For testing
# def print_linked_list(head):
#     current = head
#     while current:
#         print(current.value, end=" -> " if current.next else "\n")
#         current = current.next

# def add_first(head, task):
#     #Make a node
#     if head:
#         new_head = Node(task, head)
#     else:
#         new_head = Node(task, None)
    
#     return new_head
#     #Point the new node to the head, 

# task_1 = Node("shake tree")
# task_2 = Node("dig fossils")
# task_3 = Node("catch bugs")
# task_1.next = task_2
# task_2.next = task_3

# # Linked List: shake tree -> dig fossils -> catch bugs
# print_linked_list(add_first(task_1, "check turnip prices"))

# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next

# # For testing
# def print_linked_list(head):
#     current = head
#     while current:
#         print(current.value, end=" -> " if current.next else "\n")
#         current = current.next

# def halve_list(head):
    
#     cur = head

#     while cur:
#         cur.value /= 2
#         cur = cur.next 

#     return head

# node_one = Node(5)
# node_two = Node(6)
# node_three = Node(7)
# node_one.next = node_two
# node_two.next = node_three

# # Input List: 5 -> 6 -> 7
# print_linked_list(halve_list(node_one))

# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next

# # For testing
# def print_linked_list(head):
#     current = head
#     while current:
#         print(current.value, end=" -> " if current.next else "\n")
#         current = current.next

# def delete_tail(head):
#     if not head or not head.next:
#         return None

#     cur = head

#     while cur.next.next:
#         cur = cur.next
    
#     cur.next = None

#     return head

# butterfly = Node("Common Butterfly")
# ladybug = Node("Ladybug")
# beetle = Node("Scarab Beetle")
# butterfly.next = ladybug
# ladybug.next = beetle

# # Input List: butterfly -> ladybug -> beetle
# print_linked_list(delete_tail(butterfly))

# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next

# # For testing
# def print_linked_list(head):
#     current = head
#     while current:
#         print(current.value, end=" -> " if current.next else "\n")
#         current = current.next

# def find_min(head):
#     cur = head
#     minval = float('inf')
#     while cur != None:
#         if cur.value < minval:
#             minval = cur.value
#         cur = cur.next
#     return minval

# head1 = Node(5, Node(6, Node(7, Node(8))))
# head2 = Node(8, Node(5, Node(6, Node(7))))

# # Linked List: 5 -> 6 -> 7 -> 8
# print(find_min(head1))

# # Linked List: 8 -> 5 -> 6 -> 7
# print(find_min(head2))

# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next

# # For testing
# def print_linked_list(head):
#     current = head
#     while current:
#         print(current.value, end=" -> " if current.next else "\n")
#         current = current.next

# def delete_item(head, item):
#     curr = head
#     prev = None

#     if not head:
#         return None

#     if head.value == item:
#         return head.next

#     while curr:
        
#         if curr.value == item:
#             prev.next = curr.next
#             break
#         prev = curr 
#         curr = curr.next
    

#     return head

# slingshot = Node("Slingshot")
# peaches = Node("Peaches")
# beetle = Node("Scarab Beetle")
# slingshot.next = peaches
# peaches.next = beetle

# # Linked List: slingshot -> peaches -> beetle
# print_linked_list(delete_item(slingshot, "Peaches"))

# # Linked List: slingshot -> beetle
# print_linked_list(delete_item(slingshot, "Triceratops Torso"))

# def tail_to_head(head):
#     pass

# daisy = Node("Daisy")
# mario = Node("Mario")
# toad = Node("Toad") 
# peach = Node("Peach")
# daisy.next = mario
# mario.next = toad
# toad.next = peach

# # Linked List: Daisy -> Mario -> Toad -> Peach
# print_linked_list(tail_to_head(daisy))

# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next

# # For testing
# def print_linked_list(head):
#     current = head
#     while current:
#         print(current.value, end=" -> " if current.next else "\n")
#         current = current.next

# def tail_to_head(head):
#     #Make a reference to the tail
#     #Tail.next = head
#     #Node before tail: set next to null
    
#     if not head or not head.next: 
#         return head
    
    
#     tail = None
#     curr = head

#     while curr.next.next:
#         curr = curr.next 

#     tail = curr.next 
#     curr.next = None
#     tail.next = head 

#     return tail 

# daisy = Node("Daisy")
# mario = Node("Mario")
# toad = Node("Toad") 
# peach = Node("Peach")
# daisy.next = mario
# mario.next = toad
# toad.next = peach

# # Linked List: Daisy -> Mario -> Toad -> Peach
# print_linked_list(tail_to_head(daisy))

# class Node:
#     def __init__(self, value, next=None, prev=None):
#         self.value = value
#         self.next = next
#         self.prev = prev

# head = Node("Isabelle")
# tail = Node("K.K. Slider")


# head.next = tail
# tail.prev = head

# print(head.value, "<->", head.next.value)
# print(tail.prev.value, "<->", tail.value)

# class Node:
#     def __init__(self, value, next=None, prev=None):
#         self.value = value
#         self.next = next
#         self.prev = prev

# def print_reverse(tail):
#     curr = tail
#     while curr:
#         print(str(curr.value), end=" ")
#         curr = curr.prev

# isabelle = Node("Isabelle")
# kk_slider = Node("K.K. Slider")
# saharah = Node("Saharah")
# isabelle.next = kk_slider
# kk_slider.next = saharah
# saharah.prev = kk_slider
# kk_slider.prev = isabelle

# # Linked List: Isabelle <-> K.K. Slider <-> Saharah
# print_reverse(saharah)

# class Player:
#     def __init__(self, character, kart, outcomes):
#         self.character = character
#         self.kart = kart
#         self.items = []
#         self.race_outcomes = outcomes

#     def get_tournament_place(self, opponents):
#         #O(m)
#         places = {self.character: sum(self.race_outcomes)/len(self.race_outcomes)}
        
#         #O(n * m)
#         for opponent in opponents:
#             places[opponent.character] = sum(opponent.race_outcomes)/len(opponent.race_outcomes)
        
#         #O(nlogn)
#         order = sorted(places, key=lambda key: places[key])
        
#         #O(n)
#         return order.index(self.character) + 1

# player1 = Player("Mario", "Standard", [1, 2, 1, 1, 3])
# player2 = Player("Luigi", "Standard", [2, 1, 3, 2, 2])
# player3 = Player("Peach", "Standard", [3, 3, 2, 3, 1])

# opponents = [player2, player1]
# print(player3.get_tournament_place(opponents))

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

# shy_guy = Node("Shy Guy")
# diddy_kong = Node("Diddy Kong")
# dry_bones = Node("Dry Bones")
# shy_guy.next = diddy_kong
# diddy_kong.next = dry_bones

# link = Node("Link")
# shy_guy.next = link
# link.next = diddy_kong

# toad = Node("Toad")
# diddy_kong.next = toad
# toad.next = dry_bones

# print("Current List:")
# print_linked_list(shy_guy)

# def add_second(head, val):
#     value = Node(val)
#     value.next = head.next
#     head.next = value
#     return head

# original_list_head = Node("banana")
# second = Node("blue shell")
# third = Node("bullet bill")
# original_list_head.next = second
# second.next = third


# # Linked list: "banana" -> "blue shell" -> "bullet bill"
# new_list = add_second(original_list_head, "red shell")
# print_linked_list(new_list)

# def increment_ll(head):
#     curr = head
#     while curr:
#         curr.value += 1
#         curr = curr.next
    
#     return head

# node_one = Node(5)
# node_two = Node(6)
# node_three = Node(7)
# node_one.next = node_two
# node_two.next = node_three

# # Input List: 5 -> 6 -> 7
# print_linked_list(increment_ll(node_one))

# def copy_ll(head):
#     new_head = Node(head.value)
#     prev = new_head
#     curr = head.next

#     while curr:
#         new_node = Node(curr.value)
#         prev.next = new_node
#         prev = new_node
#         curr = curr.next
    
#     return new_head

# mario = Node("Mario")
# daisy = Node("Daisy")
# luigi = Node("Luigi")
# mario.next = daisy
# daisy.next = luigi

# # Linked List: Mario -> Daisy -> Luigi
# copy = copy_ll(mario)

# # Change original list -- should not affect the copy
# mario.value = "Original Mario"

# print_linked_list(mario)
# print_linked_list(copy) 

# def top_n_finishers(head, n):
#     results = []

#     curr = head

#     while n > 0 and curr:
#         results.append(curr.value)
#         curr = curr.next
#         n -= 1
    
#     return results

# head = Node("Daisy", Node("Mario", Node("Toad", Node("Yoshi"))))

# # Linked List: Daisy -> Mario -> Toad -> Yoshi
# print(top_n_finishers(head, 3))

# # Linked List: Daisy -> Mario -> Toad -> Yoshi
# print(top_n_finishers(head, 5))

# def remove_racer(head, racer):
#     if not head:
#         return None
    
#     if head.value == racer:
#         return head.next
    
#     prev = head
#     curr = head.next

#     while curr:
#         if curr.value == racer:
#             prev.next = curr.next 
#             break

#         prev = curr
#         curr = curr.next
    
#     return head

# head = Node("Yoshi", Node("Daisy", Node("Mario", Node("Toad", Node("Mario")))))

# # Linked List: Daisy -> Mario -> Toad -> Mario
# print_linked_list(remove_racer(head, "Mario"))

# # Linked List: Daisy -> Mario -> Toad
# print_linked_list(remove_racer(head, "Yoshi"))

class Player:
    def __init__(self, character, kart):
        self.character = character
        self.kart = kart
        self.items = []

def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def arr_to_ll(arr):
    if not arr:
        return None
    
    head = None
    prev = None

    for player in arr:
        if not head:
            prev = head = Node(player)     
        else:
            node = Node(player)
            prev.next = node
            prev = node
    
    return head

mario = Player("Mario", "Mushmellow")
luigi = Player("Luigi", "Standard LG")
peach = Player("Peach", "Bumble V")

print_linked_list(arr_to_ll([mario, luigi, peach]))
print_linked_list(arr_to_ll([peach]))


class Node:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

koopa_troopa = Node("Koopa Troopa")
toadette = Node("Toadette")
waluigi = Node("Waluigi")
koopa_troopa.next = toadette
toadette.next = waluigi

waluigi.prev = toadette
toadette.prev = koopa_troopa

def print_linked_list_backwards(tail):
    current = tail
    results = []
    while current:
        results.insert(0, current.value)
        if current.prev:
            results.insert(0, " <- ")
        current = current.prev
    
    print("".join(results))

print_linked_list(koopa_troopa)
print_linked_list_backwards(waluigi)

def get_length(node):
    return forward(node.next) + backward(node.prev) + 1

def forward(node):
    if not node:
        return 0
    
    return forward(node.next) + 1

def backward(node):
    if not node:
        return 0
    
    return backward(node.prev) + 1

yoshi_falls = Node("Yoshi Falls")
moo_moo_farm = Node("Moo Moo Farm")
rainbow_road = Node("Rainbow Road")
dk_mountain = Node("DK Mountain")
yoshi_falls.next = moo_moo_farm
moo_moo_farm.next = rainbow_road
rainbow_road.next = dk_mountain
dk_mountain.prev = rainbow_road
rainbow_road.prev = moo_moo_farm
moo_moo_farm.prev = yoshi_falls

# List: Yoshi Falls <-> Moo Moo Farm <-> Rainbow Road <-> DK Mountain
print(get_length(rainbow_road))
