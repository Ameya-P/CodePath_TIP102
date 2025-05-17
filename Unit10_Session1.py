# """
# JFK ----- LAX
# |
# |
# DFW ----- ATL
# """
# # No starter code is provided for this problem
# # Add your code here

# from collections import defaultdict, deque


# flights = {
#     "JFK": ["LAX", "DFW"],
#     "LAX": ["JFK"],
#     "DFW": ["JFK", "ATL"], 
#     "ATL": ["DFW"]        
# }

# print(list(flights.keys()))
# print(list(flights.values()))
# print(flights["JFK"])

# def bidirectional_flights(flights):
#     for a in range(len(flights)):
#         for b in flights[a]:
#             if a not in flights[b]:
#                 return False
    
#     return True

#     dict_val = {}
    


  
# flights1 = [[1, 2], [0], [0, 3], [2]]
# flights2 = [[1, 2], [], [0], [2]]

# print(bidirectional_flights(flights1))
# print(bidirectional_flights(flights2))

# def get_direct_flights(flights, source):
#     possible_direct_flights = flights[source]

#     direct_flights = []
#     for i in range(len(possible_direct_flights)):
#         if possible_direct_flights[i] == 1:
#             direct_flights.append(i)
    
#     return direct_flights

# flights = [
#             [0, 1, 1, 0],
#             [1, 0, 0, 0],
#             [1, 1, 0, 1],
#             [0, 0, 0, 0]]

# print(get_direct_flights(flights, 2))
# print(get_direct_flights(flights, 3))


# def get_adj_dict(flights):
#     adj_dict = defaultdict(list)

#     for paired_loc in flights:
#         loc_a = paired_loc[0]
#         loc_b = paired_loc[1]
#         adj_dict[loc_a].append(loc_b)
#         adj_dict[loc_b].append(loc_a)
    
#     return dict(adj_dict)


# flights = [['Cape Town', 'Addis Ababa'], ['Cairo', 'Lagos'], ['Lagos', 'Addis Ababa'], 
#             ['Nairobi', 'Cairo'], ['Cairo', 'Cape Town']]
# print(get_adj_dict(flights))

# def find_center(terminals):
#     adj_dict = defaultdict(int)

#     for paired_loc in terminals:
#         loc_a = paired_loc[0]
#         loc_b = paired_loc[1]
#         adj_dict[loc_a] += 1
#         adj_dict[loc_b] += 1
    
#     n = len(adj_dict)
#     for key in adj_dict.keys():
#         if adj_dict[key] == n - 1:
#             return key
    
#     return -1

# terminals1 = [[1,2],[2,3],[4,2]]
# terminals2 = [[1,2],[5,1],[1,3],[1,4]]

# print(find_center(terminals1))
# print(find_center(terminals2))

# def get_all_destinations(flights, key):
#     visited = set([key])
#     visited_list = [key]
#     queue = deque([key])

#     while queue:
#         current = queue.popleft()

#         if current in flights.keys():
#             for neighbor in flights[current]:
#                 if neighbor not in visited:
#                     queue.append(neighbor)
#                     visited.add(neighbor)
#                     visited_list.append(neighbor)
    
#     return visited_list

# flights = {
#     "Tokyo": ["Sydney"],
#     "Sydney": ["Tokyo", "Beijing"],
#     "Beijing": ["Mexico City", "Helsinki"],
#     "Helsinki": ["Cairo", "New York"],
#     "Cairo": ["Helsinki", "Reykjavik"],
#     "Reykjavik": ["Cairo", "New York"],
#     "Mexico City": ["Sydney"]   
# }

# print(get_all_destinations(flights, "Beijing"))
# print(get_all_destinations(flights, "Helsinki"))

# '''
#     - Initialize an empty list of visited nodes
#     - Initialize an empty queue 
#     - Add the node we would like to start our traversal from to the queue 
#     - Add the node we would like to start our traversal from to visited
#     - While the queue is not empty:
#         - Remove an element from the queue and store it in a variable, `current`
#         - Loop through each of the current node's neighbors:
#             - If the neighbor has not yet been visited:
#                 - Add the neighbor to the queue
#                 - Add the neighbor to the list of visited nodes
#     - Return the list of visited nodes
# '''

# def get_all_destinations(flights, start):
#     stack = [start]
#     visited = [start]

#     while stack:
#         current = stack.pop()
#         if current not in visited:
#             visited.append(current)
        
#         if current in flights.keys():
#             for item in flights[current]:
#                 if item not in visited:
#                     stack.append(item) 
    
#     return visited
                


# flights = {
#     "Tokyo": ["Sydney"],
#     "Sydney": ["Tokyo", "Beijing"],
#     "Beijing": ["Mexico City", "Helsinki"],
#     "Helsinki": ["Cairo", "New York"],
#     "Cairo": ["Helsinki", "Reykjavik"],
#     "Reykjavik": ["Cairo", "New York"],
#     "Mexico City": ["Sydney"]   
# }

# print(get_all_destinations(flights, "Beijing"))
# print(get_all_destinations(flights, "Helsinki"))


# # - Initialize an empty stack
# # - Initialize an empty list to store visited nodes
# # - Add the node we would like to start our traversal from to the stack
# # - while the stack is not empty:
# #     - Pop the topmost node off the stack and store it in a variable, `current`
# #     - If the node is not already in the list of visited nodes:
# #         - Add `current` to the list of visited nodes
# #     - Loop through the current node's neighbors:
# #         - If the neighbor has not yet been visited
# #             - Push the neighbor onto the stack
# # - Return list of visited nodes

# def find_itinerary(boarding_passes):
#     adj_dict = dict()
#     for pairs in boarding_passes:
#         adj_dict[pairs[0]] = pairs[1]
    
#     depart = set(adj_dict.keys())
#     arrivals = set(adj_dict.values())

#     start = depart - arrivals 

#     current = list(start)[0]
#     locations = [current]
#     while current in adj_dict.keys():
#         current = adj_dict[current]
#         locations.append(current)
    
#     return locations

# #yeah! bye!
# # i think that worked? :D
# # byee

# boarding_passes_1 = [
#                     ("JFK", "ATL"),
#                     ("SFO", "JFK"),
#                     ("ATL", "ORD"),
#                     ("LAX", "SFO")]

# boarding_passes_2 = [
#                     ("LAX", "DXB"),
#                     ("DFW", "JFK"),
#                     ("LHR", "DFW"),
#                     ("JFK", "LAX")]

# print(find_itinerary(boarding_passes_1))
# print(find_itinerary(boarding_passes_2))

from collections import defaultdict, deque


hollywood_stars = {
    "Kevin Bacon": ["Laverne Cox", "Sofia Vergara"],
    "Laverne Cox": ["Kevin Bacon", "Idris Elba"],
    "Sofia Vergara": ["Kevin Bacon", "Meryl Streep"],
    "Idris Elba": ["Laverne Cox", "Meryl Streep"],
    "Meryl Streep": ["Sofia Vergaran", "Idris Elba"],
}

print(list(hollywood_stars.keys()))
print(list(hollywood_stars.values()))
print(hollywood_stars["Kevin Bacon"])

def is_mutual(celebrities):
    relationships = set()
    for i in range(len(celebrities)):
        for j in range(len(celebrities[i])):
            if celebrities[i][j] == 1:
                if (i, j) in relationships:
                    relationships.remove((i, j))
                else:
                    relationships.add((j, i))
    
    return len(relationships) == 0

celebrities1 = [
                [0, 1, 1, 0],
                [1, 0, 1, 0],
                [1, 1, 0, 1],
                [0, 0, 1, 0]]

celebrities2 = [
                [0, 1, 1, 0],
                [1, 0, 0, 0],
                [1, 1, 0, 1],
                [0, 0, 0, 0]]

print(is_mutual(celebrities1))
print(is_mutual(celebrities2))

def get_close_friends(contacts, celeb):
    #if n = num of relationships in contacts
    #Space: O(n)
    #Time: O(n)
    friends = defaultdict(list)

    for relationship in contacts:
        celebA = relationship[0]
        celebB = relationship[1]
        friends[celebA].append(celebB)
        friends[celebB].append(celebA)
    
    return friends[celeb]

contacts = [["Lupita Nyong'o", "Jordan Peele"], ["Meryl Streep", "Jordan Peele"], ["Meryl Streep", "Lupita Nyong'o"], 
["Greta Gerwig", "Meryl Streep"], ["Ali Wong", "Greta Gerwig"]]

print(get_close_friends(contacts, "Lupita Nyong'o"))
print(get_close_friends(contacts, "Greta Gerwig"))

def get_adj_matrix(clients):
    curr_id = 0
    id_map = dict()

    for relationship in clients:
        celebA = relationship[0]
        celebB = relationship[1]

        if celebA not in id_map:
            id_map[celebA] = curr_id
            curr_id += 1
        
        if celebB not in id_map:
            id_map[celebB] = curr_id
            curr_id += 1
    
    adj_matrix = [[0 for i in range(len(id_map))] for i in range(len(id_map))]

    for relationship in clients:
        celebA = relationship[0]
        celebB = relationship[1]

        celebA_id = id_map[celebA]
        celebB_id = id_map[celebB]

        adj_matrix[celebA_id][celebB_id] = 1
        adj_matrix[celebB_id][celebA_id] = 1
    
    return id_map, adj_matrix

clients = [
            ["Yalitza Aparicio", "Julio Torres"], 
            ["Julio Torres", "Fred Armisen"], 
            ["Bowen Yang", "Julio Torres"],
            ["Bowen Yang", "Margaret Cho"],
            ["Margaret Cho", "Ali Wong"],
            ["Ali Wong", "Fred Armisen"], 
            ["Ali Wong", "Bowen Yang"]]

id_map, adj_matrix = get_adj_matrix(clients)
print(id_map)
print(adj_matrix)

def identify_celebrity(trust, n):
    #Time: O(E + V)
    #Space: O(V)
    contestant_dict = defaultdict(int) #O(V)
    trusting = set() #O(V)
    all_contestants = set()


    for relationship in trust: #O(E)
        contestantA = relationship[0]
        contestantB = relationship[1]

        trusting.add(contestantA)
        all_contestants.add(contestantA)
        all_contestants.add(contestantB)

        contestant_dict[contestantA] += 0
        contestant_dict[contestantB] += 1 #Increment the num of people who trust this person
    
    if len(all_contestants) - len(trusting) != 1:
        return -1
    
    untrusting_person = list(all_contestants - trusting).pop() #O(V)
    if contestant_dict[untrusting_person] == len(contestant_dict) - 1:
        return untrusting_person
    else:
        return -1
    
    
trust1 = [[1,2]]
trust2 = [[1,3],[2,3]]
trust3 = [[1,3],[2,3],[3,1]]

print(identify_celebrity(trust1, 2))
print(identify_celebrity(trust2, 3))
print(identify_celebrity(trust3, 3))

def have_connection(celebs, start_celeb, target_celeb):
    #Time: O(V)
    #Space: O(V)
    #BFS
    visited = set([start_celeb])
    queue = deque([start_celeb])

    while queue:
        curr = queue.popleft()

        for i in range(len(celebs)):
            if celebs[curr][i] == 1:
                if i not in visited:
                    queue.append(i)
                    visited.add(i)
    
    return target_celeb in visited

celebs = [
            [0, 1, 0, 0, 0, 0, 0, 0], # Celeb 0
            [0, 1, 1, 0, 0, 0, 0, 0], # Celeb 1
            [0, 0, 0, 1, 0, 1, 0, 0], # Celeb 2
            [0, 0, 0, 0, 1, 0, 1, 0], # Celeb 3
            [0, 0, 0, 1, 0, 0, 0, 1], # Celeb 4
            [0, 1, 0, 0, 0, 0, 0, 0], # Celeb 5
            [0, 0, 0, 1, 0, 0, 0, 1], # Celeb 6
            [0, 0, 0, 0, 1, 0, 1, 0]  # Celeb 7
            ]

print(have_connection(celebs, 0, 6))
print(have_connection(celebs, 3, 5))

def have_connection(celebs, start_celeb, target_celeb):
    #Time: O(V^2)
    #Space: O(V)
    stack = [start_celeb]
    visited = set([start_celeb])

    while stack:
        current = stack.pop()

        for i in range(len(celebs)):
            if celebs[current][i] == 1:
                if i not in visited:
                    stack.append(i)
                    visited.add(current)
    
    return target_celeb in visited

def have_connection(celebs, start_celeb, target_celeb):
    visited = set()
    def dfs_helper(start_node, visited):
        if start_node not in visited:
            visited.add(start_node)
            for i in range(len(celebs)):
                if celebs[start_node][i] == 1:
                    dfs_helper(i, visited)
    
    dfs_helper(start_celeb, visited)
    return target_celeb in visited
        
celebs = [
            [0, 1, 0, 0, 0, 0, 0, 0], # Celeb 0
            [0, 1, 1, 0, 0, 0, 0, 0], # Celeb 1
            [0, 0, 0, 1, 0, 1, 0, 0], # Celeb 2
            [0, 0, 0, 0, 1, 0, 1, 0], # Celeb 3
            [0, 0, 0, 1, 0, 0, 0, 1], # Celeb 4
            [0, 1, 0, 0, 0, 0, 0, 0], # Celeb 5
            [0, 0, 0, 1, 0, 0, 0, 1], # Celeb 6
            [0, 0, 0, 0, 1, 0, 1, 0]  # Celeb 7
            ]

print(have_connection(celebs, 0, 6))
print(have_connection(celebs, 3, 5))

class Node():
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

# Function to test if two seating arrangements (graphs) are identical
def compare_graphs(node1, node2, visited=None):
    if visited is None:
        visited = set()
    
    if node1.val != node2.val:
        return False
    
    visited.add(node1)

    if len(node1.neighbors) != len(node2.neighbors):
        return False
    
    for n1, n2 in zip(node1.neighbors, node2.neighbors):
        if n1 not in visited and not compare_graphs(n1, n2, visited):
            return False

    return True

def copy_seating(seat):
    #Time: O(V)
    #Space: O(V)
    visited = dict()

    def dfs_helper(start_node, visited):
        new_node = None

        if start_node not in visited:
            new_node = Node(start_node.val)
            visited[start_node] = new_node

            for neighbor in start_node.neighbors:
                new_node.neighbors.append(dfs_helper(neighbor, visited))
        else:
            new_node = visited[start_node]
        
        return new_node
    
    return dfs_helper(seat, visited)

lily = Node("Lily Gladstone")
mark = Node("Mark Ruffalo")
cillian = Node("Cillian Murphy")
danielle = Node("Danielle Brooks")
lily.neighbors.extend([mark, danielle])
mark.neighbors.extend([lily, cillian])
cillian.neighbors.extend([danielle, mark])
danielle.neighbors.extend([lily, cillian])

copy = copy_seating(lily)
print(compare_graphs(lily, copy))