# def common_strings(list1, list2):
#     common_strings = {}
#     for index, string in enumerate(list1):
#         common_strings[string] = index
    
#     min_string = []
#     min_index_sum = float('inf')

#     for index, string in enumerate(list2):
#         if string in common_strings:
#             index_sum = index + common_strings[string]
#             if index_sum < min_index_sum:
#                 min_string.clear()
#                 min_string.append(string)
#                 min_index_sum = index_sum
#             elif index_sum == min_index_sum:
#                 min_string.append(string)
    
#     return min_string


# '''
# Problem 3: Collecting Points at Festival Booths
# At the festival, there are various booths where visitors can collect points. Each booth has a specific number of points available. Use a stack to simulate the process of collecting points and return the total points collected after visiting all booths.

# def collect_festival_points(points):
#     pass
# Example Usage:

# print(collect_festival_points([5, 8, 3, 10])) 
# print(collect_festival_points([2, 7, 4, 6])) 
# print(collect_festival_points([1, 5, 9, 2, 8])) 

# Example Output:

# 26
# 19
# 25
# '''

# def collect_festival_points(points):
#     #U - Add everything in the list to a stack, Sum up values in stack and return
#     visited_booths = []
#     for booth in points:
#         visited_booths.append(booth)
    
#     return sum(visited_booths)

# print(collect_festival_points([5, 8, 3, 10])) 
# print(collect_festival_points([2, 7, 4, 6])) 
# print(collect_festival_points([1, 5, 9, 2, 8])) 

# '''
# Problem 4: Festival Booth Navigation
# At the cultural festival, you are managing a treasure hunt where participants need to visit booths in a specific order. The order in which they should visit the booths is defined by a series of clues. However, some clues lead to dead ends, and participants must backtrack to previous booths to continue their journey.

# You are given a list of clues, where each clue is either a booth number (an integer) to visit or the word "back" indicating that the participant should backtrack to the previous booth.

# Write a function to simulate the participant's journey and return the final sequence of booths visited, in the order they were visited.

# def booth_navigation(clues):
#     pass
# Example Usage:

# clues = [1, 2, "back", 3, 4]
# print(booth_navigation(clues)) 

# clues = [5, 3, 2, "back", "back", 7]
# print(booth_navigation(clues)) 

# clues = [1, "back", 2, "back", "back", 3]
# print(booth_navigation(clues)) 
# Example Output:

# [1, 3, 4]
# [5, 7]
# [3]
# '''

# def booth_navigation(clues):
#     #U - Use a stack to hold information about which booths we visited, Check if stack is empty when we're going back
#     #M - Stacks
#     #P/I

#     visited_booths = []

#     for clue in clues:
#         if clue == "back":
#             if len(visited_booths) > 0:
#                 visited_booths.pop()
#         else: 
#             visited_booths.append(clue)
    
#     return visited_booths

# clues = [1, 2, "back", 3, 4]
# print(booth_navigation(clues)) 

# clues = [5, 3, 2, "back", "back", 7]
# print(booth_navigation(clues)) 

# clues = [1, "back", 2, "back", "back", 3]
# print(booth_navigation(clues)) 

'''
Problem 1: Final Costs After a Supply Discount
You are managing the budget for a global expedition, where the cost of supplies is represented by an integer array costs, where costs[i] is the cost of the ith supply item.

There is a special discount available during the expedition. If you purchase the ith item, you will receive a discount equivalent to costs[j], where j is the minimum index such that j > i and costs[j] <= costs[i]. If no such j exists, you will not receive any discount.

Return an integer array final_costs where final_costs[i] is the final cost you will pay for the ith supply item, considering the special discount.

def final_supply_costs(costs):
  pass
Example Usage:

print(final_supply_costs([8, 4, 6, 2, 3])) 
print(final_supply_costs([1, 2, 3, 4, 5])) 
print(final_supply_costs([10, 1, 1, 6])) 
Example Output:

[4, 2, 4, 2, 3]
[1, 2, 3, 4, 5]
[9, 0, 1, 6]
'''

#U-Understand
#Input = Array of integers, Output = Array of integers of the same size, with discount subtracted 

from collections import deque


def final_supply_costs(costs):
    stack = []

    for index, value in enumerate(costs):
        while stack and value <= costs[stack[-1]]:
            prev = stack.pop()
            costs[prev] -= value
        stack.append(index)
    
    return costs
        
print(final_supply_costs([8, 1, 6, 2, 3])) 
print(final_supply_costs([1, 2, 3, 4, 5])) 
print(final_supply_costs([10, 1, 1, 6])) 

# def booth_navigation(clues):
#     stack = []
#     for clue in clues:
#         if clue == 'back':
#             if stack:
#                 stack.pop()
#         else:
#             stack.append(clue)
#     return stack

# clues = [1, 2, "back", 3, 4]
# print(booth_navigation(clues)) 

# clues = [5, 3, 2, "back", "back", 7]
# print(booth_navigation(clues)) 

# clues = [1, "back", 2, "back", "back", 3]
# print(booth_navigation(clues)) 

def merge_schedules(schedule1, schedule2):
    one = 0
    two = 0
    merged = ''

    while one < len(schedule1) and two < len(schedule2):
        merged += schedule1[one]
        merged += schedule2[two]

        one += 1
        two += 1
    
    if one < len(schedule1):
        merged += schedule1[one:]
    
    if two < len(schedule2):
        merged += schedule2[two:]
    
    return merged

print(merge_schedules("abc", "pqr")) 
print(merge_schedules("ab", "pqrs")) 
print(merge_schedules("abcd", "pq")) 

def next_greater_event(schedule1, schedule2):
    dict = {}
    stack = []

    for item in schedule2:
        dict[item] = -1
        while stack and stack[-1] < item:
            dict[stack.pop()] = item
        
        stack.append(item)
    
    return [dict[item] for item in schedule1]

print(next_greater_event([4, 1, 2], [1, 3, 4, 2])) 
print(next_greater_event([2, 4], [1, 2, 3, 4])) 

def sort_performances_by_type(performances):
    left = 0
    right = len(performances) - 1
    while left < right:

        #Find odd
        while performances[left] % 2 == 0:
            left += 1
        
        #Find even
        while performances[right] % 2 != 0:
            right -= 1
        
        performances[left], performances[right] = performances[right], performances[left]
        left += 1
        right -= 1
    
    return performances

print(sort_performances_by_type([3, 1, 2, 4]))  
print(sort_performances_by_type([0]))  

def first_symmetrical_landmark(landmarks):
    for landmark in landmarks:
        if is_symmetric(landmark):
            return landmark

    return ""

def is_symmetric(landmark):
    left = 0
    right = len(landmark) - 1

    while left < right:
        if landmark[left] != landmark[right]:
            return False
        
        left += 1
        right -= 1

    return True

print(first_symmetrical_landmark(["canyon","forest","rotor","mountain"])) 
print(first_symmetrical_landmark(["plateau","valley","cliff", "racecar"])) 

def terrain_elevation_match(terrain):
    queue = deque(range(len(terrain) + 1))
    results = []

    for char in terrain:
        if char == "I":
            results.append(queue.popleft())
        else:
            results.append(queue.pop())
    
    results.append(queue.pop())

    return results

print(terrain_elevation_match("DDDDI")) 
print(terrain_elevation_match("III")) 
print(terrain_elevation_match("DDI")) 

def find_the_log_conc_val(logs):
    left = 0
    right = len(logs) - 1
    concat = 0

    while left < right:
        num = str(logs[left]) + str(logs[right])
        concat += int(num)
        left += 1
        right -= 1
    
    if left == right:
        concat += logs[left]
    
    return concat

print(find_the_log_conc_val([7, 52, 2, 4])) 
print(find_the_log_conc_val([5, 14, 13, 8, 12])) 

def count_explorers(explorers, supplies):
    queue = deque(explorers)
    stack = deque(supplies)

    skipped = 0

    while len(queue) != skipped:
        explorer = queue.popleft()
        supply = stack[0]
        if explorer == supply:
            stack.popleft()
            skipped = 0
        else:
            queue.append(explorer)
            skipped += 1
    
    return skipped

print(count_explorers([1, 1, 0, 0], [0, 1, 0, 1]))  
print(count_explorers([1, 1, 1, 0, 0, 1], [1, 0, 0, 0, 1, 1])) 

def count_balanced_terrain_subsections(terrain):
    #Go through terrain list. If there's nothing in the stack, add item. 
    #If there's an item, then add an item if it's equal to the item in
    queue = deque()
    subsections = 0

    for item in terrain:
        if queue and item != queue[-1]:
            queue.pop()
            subsections += 1
            queue.appendleft(item)
        else:
            queue.append(item)
    
    return subsections

print(count_balanced_terrain_subsections("11001")) 
print(count_balanced_terrain_subsections("10101"))

def reverse_string(s):
    if len(s) <= 1:
        return s
    
    return reverse_string(s[1:]) + s[0]
    
print(reverse_string("abcdefg"))


def is_prefix_of_signal(transmission, searchSignal):

    def is_prefix(word):
            n = len(searchSignal)
            if len(word) < n:
                return False
            
            return word[:n] == searchSignal
    
    transmission = transmission.split()

    for index, word in enumerate(transmission):
        if is_prefix(word):
            return index + 1
    
    return -1


print(is_prefix_of_signal("i love eating burger", "burg")) 
print(is_prefix_of_signal("this problem is an easy problem", "pro")) 
print(is_prefix_of_signal("i am tired", "you")) 