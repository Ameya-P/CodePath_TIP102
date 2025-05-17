# def can_rebook(flights, source, dest):
#     stack = [source]
#     visited = set([source])

#     while stack:
#         current = stack.pop()
#         if current not in visited:
#             visited.add(current)
        
#         for neighbor in range(len(flights[current])):

#             if flights[current][neighbor] == 1:
#                 if neighbor not in visited:
#                     stack.append(neighbor)
    
#     return (dest in visited)

# '''
# - Initialize an empty stack
# - Initialize an empty list to store visited nodes
# - Add the node we would like to start our traversal from to the stack
# - while the stack is not empty:
#     - Pop the topmost node off the stack and store it in a variable, `current`
#     - If the node is not already in the list of visited nodes:
#         - Add `current` to the list of visited nodes
#     - Loop through the current node's neighbors:
#         - If the neighbor has not yet been visited
#             - Push the neighbor onto the stack
# - Return list of visited nodes
# '''

# flights1 = [
#     [0, 1, 0], # Flight 0
#     [0, 0, 1], # Flight 1
#     [0, 0, 0]  # Flight 2
# ]

# flights2 = [
#     [0, 1, 0, 1, 0],
#     [0, 0, 0, 1, 0],
#     [0, 0, 0, 0, 1],
#     [0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0]
# ]

# print(can_rebook(flights1, 0, 2))
# print(can_rebook(flights2, 0, 2)) 

#Time: O()
#Space: O()
from collections import deque

def can_rebook(flights, source, dest):
    #Time: O(V * V): Visit every node, go through 1 row of matrix for every node
    #Space: O(V)
    visited = set([source]) #contains all nodes
    queue = deque([source]) 

    while queue:
        current = queue.popleft()

        for i in range(len(flights)):
            if flights[current][i] == 1:
                if i not in visited:
                    queue.append(i)
                    visited.add(i)
    
    return dest in visited

def can_rebook(flights, source, dest):
    #Time: O(V * V): visiting every node and going through a row of the matrix for every node
    #Space: O(V): set holds all nodes
    visited = set()
    def dfs_helper(source, visited):
        if source not in visited:
            visited.add(source)
            
            for i in range(len(flights)):
                if flights[source][i] == 1:
                    dfs_helper(i, visited)
    dfs_helper(source, visited)
    return dest in visited

flights1 = [
    [0, 1, 0], # Flight 0
    [0, 0, 1], # Flight 1
    [0, 0, 0]  # Flight 2
]

flights2 = [
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

print(can_rebook(flights1, 0, 2))
print(can_rebook(flights2, 0, 2)) 

def counting_flights(flights, i, j):
    #Time: O(V^2)
    #Space: O(V)
    visited = set([i])
    queue = deque([i])
    dist = 0
    while queue:
        level_size = len(queue)
        dist += 1
        for _ in range(level_size):
            curr = queue.popleft()

            for w in range(len(flights)):
                if flights[curr][w] == 1:
                    if w == j:
                        return dist
                    if w not in visited:
                        queue.append(w)
                        visited.add(w)
    
    return -1

# Example usage
flights = [
    [0, 1, 1, 0, 0], # Airport 0
    [0, 0, 1, 0, 0], # Airport 1
    [0, 0, 0, 1, 0], # Airport 2
    [0, 0, 0, 0, 1], # Airport 3
    [0, 0, 0, 0, 0]  # Airport 4
]

print(counting_flights(flights, 0, 2))  
print(counting_flights(flights, 0, 4))
print(counting_flights(flights, 4, 0))

#keep doing bfs or dfs until I accounted for every vertice

def num_airline_regions(is_connected):
    #Time: O(V^2)
    #Space: O(V)
    all_airports = set(range(len(is_connected)))
    visited = set()

    def dfs_helper(source, visited):
        if source not in visited:
            visited.add(source)

            for i in range(len(is_connected)):
                if is_connected[source][i] == 1:
                    dfs_helper(i, visited)
    
    num_regions = 0
    while len(visited) < len(is_connected):
        remaining = all_airports - visited
        start = list(remaining).pop()

        dfs_helper(start, visited)
        num_regions += 1
    
    return num_regions

is_connected1 = [
    [1, 1, 0],
    [1, 1, 0],
    [0, 0, 1]
]

is_connected2 = [
    [1, 0, 0, 1],
    [0, 1, 1, 0],
    [0, 1, 1, 0],
    [1, 0, 0, 1]
]

print(num_airline_regions(is_connected1))
print(num_airline_regions(is_connected2)) 

def calculate_cost(flights, start, dest):
    visited = set()
    def find_path(source, visited):
        if source == dest:
            return [source]
        
        if source not in visited:
            visited.add(source)
            for neighbor, price in flights[source]:
                path = find_path(neighbor, visited)
                if path:
                    return [source] + path
        else:
            return []
    
    return find_path(start, visited)

def calculate_cost(flights, start, dest):
    visited = set()
    def find_cost(source, visited):
        if source[0] == dest:
            return source[1]
        
        if source[0] not in visited:
            visited.add(source[0])
            for neighbor in flights[source[0]]:
                cost = find_cost(neighbor, visited)
                if cost > 0:
                    return source[1] + cost
        return -1
    
    return find_cost((start, 0), visited)

def calculate_cost(flights, start, dest):
    visited = set()
    def dfs_helper(source, total_cost):
        if source == dest:
            return total_cost
        
        visited.add(source)

        for neighbor, cost in flights.get(source, []):
            if neighbor not in visited:
                result = dfs_helper(neighbor, total_cost + cost)
                if result != -1:
                    return result
        
        visited.remove(source)

        return -1
    
    return dfs_helper(start, 0)

flights = { 
    'LAX': [('SFO', 50)],
    'SFO': [('LAX', 50), ('ORD', 100), ('ERW', 210)],
    'ERW': [('SFO', 210), ('ORD', 100)],
    'ORD': [('ERW', 300), ('SFO', 100), ('MIA', 400)],
    'MIA': [('ORD', 400)]
}

print(calculate_cost(flights, 'LAX', 'MIA'))