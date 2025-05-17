# class Node():
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next

# def find_middle(head):
#     if not head:
#         return None
    
#     slow = head
#     fast = head
    
#     while slow and fast and fast.next:
#         slow = slow.next
#         fast = fast.next.next 
    
#     return slow

# ll = Node(1, Node(2, Node(3, Node(4, Node(5)))))
# ll2 = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6))))))
# ll3 = Node(1, Node(2, Node(3, Node(4))))
# print(find_middle(ll).value)

# def find_cycle(head):
#     slow = fast = head

#     while fast and fast.next:
#         slow = slow.next
#         fast = fast.next.next 

#         if slow == fast:
#             return True
    
#     return False

# node_1 = Node(1)
# node_2 = Node(2)
# node_3 = Node(3)

# node_1.next = node_2
# node_2.next = node_3
# node_3.next = node_1

# print(find_cycle(node_1))

# def delete_middle(head):
#     if not head:
#         return None
    
#     if not head.next:
#         return None
    
#     slow = head
#     fast = head
#     prev = None
    
#     while slow and fast and fast.next:
#         prev = slow
#         slow = slow.next
#         fast = fast.next.next 
    
#     prev.next = slow.next
#     slow.next = None
    
#     return head

# ll2 = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6))))))
# head = delete_middle(ll3)

# def print_linked_list(head):
#     current = head
#     while current:
#         print(current.value, end=" -> " if current.next else "\n")
#         current = current.next

# print_linked_list(head)


# class SongNode:
#     def __init__(self, song, artist, next=None):
#         self.song = song
#         self.artist = artist
#         self.next = next

# # For testing
# def print_linked_list(node):
#     current = node
#     while current:
#         print((current.song, current.artist), end=" -> " if current.next else "")
#         current = current.next
#     print()

#uf = SongNode("Uptown Funk")
#pra = SongNode("Party Rock Anthem")
#br = SongNode("Bad Romance")


#uf.next = pra
#pra.next = br

#print_linked_list(uf)
#Create dictionary of counts
#Iterate through linked list and add to dictionary

# def get_artist_frequency(playlist):
#     results = {}
#     curr = playlist
#     while curr:
#         if curr.artist not in results:
#             results[curr.artist] = 1
#         else:
#             results[curr.artist] += 1
#         curr = curr.next
    
#     return results

# playlist = SongNode("Saturn", "SZA", 
#                 SongNode("Who", "Jimin", 
#                         SongNode("Espresso", "Sabrina Carpenter", 
#                                 SongNode("Snooze", "SZA"))))

# print(get_artist_frequency(playlist))

# class SongNode:
#     def __init__(self, song, artist, next=None):
#         self.song = song
#         self.artist = artist
#         self.next = next

# # For testing
# def print_linked_list(node):
#     current = node
#     while current:
#         print((current.song, current.artist), end=" -> " if current.next else "")
#         current = current.next
#     print()


# # Function with a bug!
# def remove_song(playlist_head, song):
#     if not playlist_head:
#         return None
    
#     if playlist_head.song == song:
#         return playlist_head.next

#     current = playlist_head
#     while current.next:
#         if current.next.song == song:
#             current.next = current.next.next  
#             return playlist_head 
#         current = current.next

#     return playlist_head

# playlist = SongNode("SOS", "ABBA", 
#                 SongNode("Simple Twist of Fate", "Bob Dylan",
#                     SongNode("Dreams", "Fleetwood Mac",
#                         SongNode("Lovely Day", "Bill Withers"))))

# print_linked_list(remove_song(playlist, "Dreams"))
# # My thing just crashed

# def on_repeat(playlist_head):
#     slow = playlist_head
#     fast = playlist_head

#     while fast and fast.next:
#         slow = slow.next
#         fast = fast.next.next

#         if slow == fast:
#             return True
    
#     return False

# song1 = SongNode("GO!", "Common")
# song2 = SongNode("N95", "Kendrick Lamar")
# song3 = SongNode("WIN", "Jay Rock")
# song4 = SongNode("ATM", "J. Cole")
# song1.next = song2
# song2.next = song3
# song3.next = song4
# song4.next = song2

# print(on_repeat(song1))

# class SongNode:
#     def __init__(self, song, artist, next=None):
#         self.song = song
#         self.artist = artist
#         self.next = next

# # For testing
# def print_linked_list(node):
#     current = node
#     while current:
#         print((current.song, current.artist), end=" -> " if current.next else "")
#         current = current.next
#     print()

# def loop_length(playlist_head):
#     #As we iterate through the linked list
#     #We add node to a set 
#     #If a node is already in the set then add it to a second set 
#     #If we start repeating nodes in the second set then exit out of the loop
    
#     #
#     slow = playlist_head
#     visited = set()
#     cycle_nodes = set()
#     while slow:
#         if slow not in visited:
#             visited.add(slow)
#         elif slow not in cycle_nodes:
#             cycle_nodes.add(slow)
#         else:
#             break
        
#         slow = slow.next
    
#     return len(cycle_nodes)
        
        
# song1 = SongNode("Wein", "AL SHAMI")
# song2 = SongNode("Si Ai", "Tayna")
# song3 = SongNode("Qalbi", "Yasser Abd Alwahab")
# song4 = SongNode("La", "DYSTINCT")
# song1.next = song2
# song2.next = song3
# song3.next = song4
# song4.next = song2

# print(loop_length(song1)) 
            
        
# class Node:
# 	def __init__(self, value, next=None):
# 		self.value = value
# 		self.next = next

# # For testing
# def print_linked_list(head):
#     current = head
#     while current:
#         print(current.value, end=" -> " if current.next else "\n")
#         current = current.next
# #One method
# #Have a node one ahead another. Compare the 
# def count_critical_points(song_audio):
#     critical_points =  0
#     prev = current = song_audio
    
#     while current.next and current.next.next:
#         current = current.next
        
#         if current.value > prev.value and current.value > current.next.value:
#             critical_points += 1
#         elif current.value < prev.value and current.value < current.next.value:
#             critical_points += 1
#         else:
#             pass
        
#     return critical_points
        
# song_audio = Node(5, Node(3, Node(1, Node(2, Node(5, Node(1, Node(2)))))))

# print(count_critical_points(song_audio))

# class Node:
# 	def __init__(self, value, next=None):
# 		self.value = value
# 		self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next
    
# head = Node("Harry", Node("Ron", Node("Hermione")))
# print_linked_list(head)

# class Node:
#     def __init__(self, house, score, next=None):
#         self.house = house
#         self.value = score
#         self.next = next

# def count_element(house_points, score):
#     counts = 0
#     curr = house_points
#     while curr:
#         if curr.value == score:
#             counts += 1
#         curr = curr.next
#     return counts
# # Time Complexity = O(n), Space Complexity = O(1)


# house_points = Node("Gryffindor", 600, 
#                 Node("Ravenclaw", 300,
#                     Node("Slytherin", 500,
#                         Node("Hufflepuff", 600))))

# score = 600

# print(count_element(house_points, score))

class Node:
    def __init__(self, potion, next=None):
        self.potion = potion
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.potion, end=" -> " if current.next else "\n")
        current = current.next

def find_middle_potion(potions):
    slow = potions
    fast = potions

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow.potion

potions1 = Node("Poison Antidote", Node("Shrinking Solution", Node("Trollblood Tincture")))
potions2 = Node("Elixir of Life", Node("Sleeping Draught", Node("Babbling Beverage", Node("Aging Potion"))))

print(find_middle_potion(potions1))
print(find_middle_potion(potions2))
#Time Complexity: O(n), Space Complexity: O(1)

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

def reverse(events):
    if not events:
        return events
    
    if not events.next:
        return events
    
    prev = events
    curr = events.next
    events.next = None

    while curr:
        new_next = curr.next
        curr.next = prev
        prev = curr
        curr = new_next
    
    return prev

events = Node("Potion Brewing", 
            Node("Spell Casting", 
                Node("Wand Making", 
                    Node("Dragon Taming", 
                        Node("Broomstick Flying")))))

print_linked_list(reverse(events))
#Time Complexity: O(n), Space Complexity: O(1)

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

def is_mirrored(head):
    stack = []

    current = head

    while current:
        stack.append(current.value)
        current = current.next
    
    current = head
    while current:
        if stack.pop() != current.value:
            return False
        
        current = current.next
    
    return True

list1 = Node("Phoenix", Node("Dragon", Node("Phoenix", Node("Dragon", Node("Phoenix")))))
list2 = Node("Werewolf", Node("Vampire", Node("Griffin", Node("Vampire", Node("Werewolf")))))

print(is_mirrored(list1))
print(is_mirrored(list2))

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

def loop_start(path_start):
    if not path_start:
        return None
    
    if not path_start.next:
        return None

    slow = path_start
    
    visited = set()
    cycle = set()

    while slow:
        if slow not in visited:
            visited.add(slow)
        elif slow not in cycle:
            cycle.add(slow)
        else:
            break

        slow = slow.next
    
    current = path_start

    while current:
        if current in cycle:
            break

        current = current.next
    
    return current.value
    

path_start = Node("Mystic Falls")
waypoint1 = Node("Troll's Bridge")
waypoint2 = Node("Elven Arbor")
waypoint3 = Node("Fairy Glade")

path_start.next = waypoint1
waypoint1.next = waypoint2
waypoint2.next = waypoint3
waypoint3.next = waypoint1

print(loop_start(path_start))
