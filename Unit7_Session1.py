# def count_suits_iterative(suits):
#     length = 0
#     for item in suits:
#         length += 1
    
#     return length

# def count_suits_recursive(suits):
#     #Base Case
#     if not suits:
#         return 0

#     #Recursive Case
#     return 1 + count_suits_recursive(suits[:-1])

# print(count_suits_iterative(["Mark I", "Mark II", "Mark III"]))
# print(count_suits_recursive(["Mark I", "Mark I", "Mark III", "Mark IV"]))

# def sum_stones(stones):
#     if not stones:
#         return 0
    
#     return stones.pop() + sum_stones(stones)

# print(sum_stones([5, 10, 15, 20, 25, 30]))
# print(sum_stones([12, 8, 22, 16, 10]))

def count_suits_iterative(suits):
    return len(set(suits))

items = set()
def count_suits_recursive(suits):
    #Base Case
    if not suits:
        return 0
    
    #Recursive Case
    suit = suits.pop()
    if suit not in items:
        items.add(suit)
        return 1 + count_suits_recursive(suits)
    else:
        return count_suits_recursive(suits)
    
#Answer from Resources
def count_suits_recursive(suits):
    if not suits:
        return 0
    first = suits[0]
    rest_unique_count = count_suits_recursive(suits[1:])
    if first in suits[1:]:
        return rest_unique_count
    else:
        return 1 + rest_unique_count

# 1) Base case: If the list `suits` is empty, return 0.
# 2) Recursive case: 
#    a) Extract the first element `first` from `suits`.
#    b) Call the recursive function on the rest of the list `suits[1:]`.
#    c) If `first` is in the rest of the list, return the result of the recursive call.
#    d) If `first` is not in the rest of the list, return 1 plus the result of the recursive call.

print(count_suits_iterative(["Mark I", "Mark II", "Mark III"]))
print(count_suits_recursive(["Mark I", "Mark I", "Mark III"]))


def fibonacci_growth(n):
    #Base Case
    if n <= 1:
        return n
    
    return fibonacci_growth(n-1) + fibonacci_growth(n-2)

print(fibonacci_growth(5))
print(fibonacci_growth(8))

def power_of_four(n):
    #Base Case
    if n == 0: 
        return 1
    
    #Recursive Case
    if n < 0:
        return (1/4) * power_of_four(n+1)
    
    if n > 0:
        return 4 * power_of_four(n-1)
    

print(power_of_four(2))
print(power_of_four(-2))

# maximum = float('-inf')
# def strongest_avenger(strengths):
#     #Base Case:
#     if len(strengths) == 1:
#         return strengths.pop()

#     #Recursive
#     num = strengths.pop()
#     current_strongest = strongest_avenger(strengths)
    
#     if num > current_strongest:
#         return num
#     else:
#         return current_strongest
    

# print(strongest_avenger([88, 92, 95, 99, 97, 100, 94]))
# print(strongest_avenger([50, 75, 85, 60, 90, 200]))

# def count_deposits(resources):
#     #Base Case
#     if not resources:
#         return 0
    
#     char = resources[-1]
#     if char == 'V':
#         return 1 + count_deposits(resources[:-1])
#     else:
#         return count_deposits(resources[:-1])

# print(count_deposits("VVVVV"))
# print(count_deposits("VXVYGA"))

# class Node:
#   def __init__(self, value, next=None):
#       self.value = value
#       self.next = next

# # For testing
# def print_linked_list(head):
#     current = head
#     while current:
#         print(current.value, end=" -> " if current.next else "\n")
#         current = current.next

# def merge_missions(mission1, mission2):
#     temphead = Node("")
#     helper(mission1, mission2, temphead)
#     return temphead.next

# def helper(mission1, mission2, current):
#     #Base Case
#     if not mission1 and not mission2:
#         return 
    
#     #Recursive Cases
#     if mission1 and mission2:
#         if mission1.value < mission2.value:
#             current.next = mission1
#             mission1 = mission1.next
#             current = current.next
#         else:
#             current.next = mission2
#             mission2 = mission2.next
#             current = current.next
#     elif mission1:
#         current.next = mission1
#         mission1 = mission1.next
#         current = current.next
#     elif mission2:
#         current.next = mission2
#         mission2 = mission2.next
#         current = current.next
    
#     return helper(mission1, mission2, current)
    
# mission1 = Node(1, Node(2, Node(4)))
# mission2 = Node(1, Node(3, Node(4, Node(5))))

# print_linked_list(merge_missions(mission1, mission2))

# def get_village_class_iterative(population):
#     num_digits = 0

#     while population:
#         population = population // 10
#         num_digits += 1
    
#     return num_digits
# #t: O(n) where n = num digits, s: O(1)

# def get_village_class_recursive(population):
#     if not population:
#         return 0
    
#     return 1+ get_village_class_recursive(population//10)
#  #t: O(n) where n = num digits, s: O(n)   

# print(get_village_class_iterative(432))
# print(get_village_class_recursive(432))
# print(get_village_class_iterative(9))
# print(get_village_class_recursive(9))

# def count_walls(walls):
#     if not walls:
#         return 1
    
#     return 1 + count_walls(walls[1])
# #T: O(n), where n = number of walls, S: O(n)

# walls = ["outer", ["inner", ["keep", []]]]

# print(count_walls(walls))
# print(count_walls([]))

# def reverse_scroll(scroll):
#     scroll = list(scroll) #O(n)
#     reversed = []
#     return helper(scroll, reversed)

# def helper(scroll, reversed):
#     if not scroll:
#         return "".join(reversed)
    
#     reversed.append(scroll.pop())
#     return helper(scroll, reversed)
# #T: O(n), n = char in string, S: O(n)
    

# print(reverse_scroll("cigam"))
# print(reverse_scroll("lleps"))

# def is_palindrome(name):
#     return helper(name, 0, len(name) - 1)

# def helper(name, left, right):
#     if not name:
#         return False
    
#     if left >= right:
#         return True
    
#     if name[left] != name[right]:
#         return False 
    
#     return helper(name, left+1, right-1)
# #T: O(n), n = char in string, S: O(n)

# print(is_palindrome("eve"))
# print(is_palindrome("ling"))
# print(is_palindrome(""))

# def double_power(initial_power, n):
#     if not n:
#         return initial_power
    
#     return double_power(initial_power * 2, n-1)
# #T: O(n), n = char in string, S: O(n)

# print(double_power(5, 3))
# print(double_power(7, 2))

# def is_increasing_path(path):
#     return helper(path, 0, 1)

# def helper(path, one, two):
#     if two >= len(path):
#         return True
    
#     if path[one] > path[two]:
#         return False
    
#     return helper(path, one + 1, two + 1)
# #T: O(n), n = char in string, S: O(n)

# print(is_increasing_path([1, 2, 3, 4, 5]))
# print(is_increasing_path([3, 5, 2, 8]))

def longest_streak(frames, current_length=0, max_length=0):
    if not frames:
        return max_length
    
    if frames[0] == "S":
        current_length += 1
    else:
        current_length = 0

    if current_length > max_length:
        max_length = current_length
    
    return longest_streak(frames[1:], current_length, max_length)
#T: O(n), n = char in string, S: O(n^2)

print(longest_streak("SSOSSS"))
print(longest_streak("SOSOSOSO"))

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

def weave_spells(spell_a, spell_b):
    tempnode = Node("")
    helper(spell_a, spell_b, tempnode)
    return tempnode.next

def helper(a, b, current):
    if not a and not b:
        return
    
    if a and b: 
        if a.value < b.value:
            current.next = a
            a = a.next
        else:
            current.next = b
            b = b.next
    elif a:
        current.next = a
        a = a.next
    elif b:
        current.next = b
        b = b.next
    
    current = current.next

    return helper(a, b, current)

spell_a = Node('A', Node('C', Node('E')))
spell_b = Node('B', Node('D', Node('F')))

print_linked_list(weave_spells(spell_a, spell_b))