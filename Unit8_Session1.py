# from collections import deque 

# def print_tree(root):
#     if not root:
#         return "Empty"
#     result = []
#     queue = deque([root])
#     while queue:
#         node = queue.popleft()
#         if node:
#             result.append(node.val)
#             queue.append(node.left)
#             queue.append(node.right)
#         else:
#             result.append(None)
#     while result and result[-1] is None:
#         result.pop()
#     print(result)

# class TreeNode:
#     def __init__(self, value, left=None, right=None):
#         self.val = value
#         self.left = left
#         self.right = right

# root = TreeNode("Trunk")

# mcintosh = TreeNode("Mcintosh")
# granny_smith = TreeNode("Granny Smith")

# fuji = TreeNode("Fuji")
# opal = TreeNode("Opal")

# crab = TreeNode("Crab")
# gala= TreeNode("Gala")

# root.right = granny_smith
# root.left = mcintosh

# mcintosh.left = fuji
# mcintosh.right = opal

# granny_smith.right = gala
# granny_smith.left = crab

# #print_tree(root)

# #Problem 2: Calculating Yield
# class TreeNode:
#     def __init__(self, value, left=None, right=None):
#         self.val = value
#         self.left = left
#         self.right = right

# def calculate_yield(root):
#     if root.val == "+":
#         return root.left.val + root.right.val
    
#     if root.val == "*":
#         return root.left.val * root.right.val
    
#     if root.val == "-":
#         return root.left.val - root.right.val


# """
#     +
#   /   \
#  7     5
# """
# # apple_tree = TreeNode("+", TreeNode(7), TreeNode(5))
# # print(calculate_yield(apple_tree))

# # apple_tree = TreeNode("-", TreeNode(7), TreeNode(5))
# # print(calculate_yield(apple_tree))

# # apple_tree = TreeNode("*", TreeNode(7), TreeNode(5))
# # print(calculate_yield(apple_tree))


# #Problem 3: Ivy Cutting
# class TreeNode:
#     def __init__(self, value, left=None, right=None):
#         self.val = value
#         self.left = left
#         self.right = right

# def right_vine_iterative(root):
#     path = []
#     current = root
#     while current: 
#         path.append(current.val)
#         current = current.right

#     return path

# #Problem 4: Ivy Cutting II
# def right_vine_recursive(root):
#     return helper(root, [])

# def helper(current, path):
#     if not current:
#         return path
    
#     path.append(current.val)
#     return helper(current.right, path)

# """
#         Root
#       /      \
#     Node1    Node2
#   /         /    \
# Leaf1    Leaf2  Leaf3
# """
# ivy1 = TreeNode("Root", 
#                 TreeNode("Node1", TreeNode("Leaf1")),
#                 TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))

# """
#       Root
#       /  
#     Node1
#     /
#   Leaf1  
# """
# ivy2 = TreeNode("Root", TreeNode("Node1", TreeNode("Leaf1")))

# # print(right_vine(ivy1))
# # print(right_vine(ivy2))

# # print(right_vine_recursive(ivy1))
# # print(right_vine_recursive(ivy2))


# # Problem 5: Count the Tree Leaves
# class TreeNode:
#     def __init__(self, value, left=None, right=None):
#         self.val = value
#         self.left = left
#         self.right = right

# def count_leaves(root):
#     if not root:
#         return 0 
    
#     if not root.left and not root.right: 
#         return 1
    
#     return count_leaves(root.left) + count_leaves(root.right)
    
# """
#         Root
#       /      \
#     Node1    Node2
#   /         /    \
# Leaf1    Leaf2  Leaf3
# """

# oak1 = TreeNode("Root", 
#                 TreeNode("Node1", TreeNode("Leaf1")),
#                 TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))

# """
#       Root
#       /  
#     Node1
#     /
#   Leaf1  
# """
# oak2 = TreeNode("Root", TreeNode("Node1", TreeNode("Leaf1")))


# # print(count_leaves(oak1))
# # print(count_leaves(oak2))

# # Problem 6: Pruning Plans
# class TreeNode:
#     def __init__(self, value, left=None, right=None):
#         self.val = value
#         self.left = left
#         self.right = right

# def survey_tree(root):
#     path = []
#     survey_helper(root, path)
#     return path

# def survey_helper(current, path):
#     if not current:
#         return 
    
#     survey_helper(current.left, path)
#     survey_helper(current.right, path)
#     path.append(current.val)

# """
#         Root
#       /      \
#     Node1    Node2
#   /         /    \
# Leaf1    Leaf2  Leaf3
# """

# magnolia = TreeNode("Root", 
#                 TreeNode("Node1", TreeNode("Leaf1")),
#                 TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))

# # print(survey_tree(magnolia))



# # Problem 7: Foraging Berries
# class TreeNode:
#     def __init__(self, value, left=None, right=None):
#         self.val = value
#         self.left = left
#         self.right = right

# def harvest_berries(root, threshold):
#     if not root:
#         return 0 
    
#     if root.val > threshold: 
#         return root.val + harvest_berries(root.left, threshold) + harvest_berries(root.right, threshold)
#     else:
#         return harvest_berries(root.left, threshold) + harvest_berries(root.right, threshold)


# """
#        4
#      /   \
#    10     6
#   /  \     \
#  5    8    20
# """
# bush = TreeNode(4, TreeNode(10, TreeNode(5), TreeNode(8)), TreeNode(6, None, TreeNode(20)))

# # print(harvest_berries(bush, 6))
# # print(harvest_berries(bush, 30))

# # Problem 8: Flower Fields
# class TreeNode:
#     def __init__(self, value, left=None, right=None):
#         self.val = value
#         self.left = left
#         self.right = right

# def find_flower(root, flower):
#     return flower_helper(root, flower)

# def flower_helper(current, flower):
#     if not current:
#         return False
    
#     if current.val == flower:
#         return True
    
#     if flower[0] < current.val[0]:
#         return flower_helper(current.left, flower)
#     elif flower[0] > current.val[0]:
#         return flower_helper(current.right, flower)
#     elif flower[0] == current.val[0]:
#         if len(flower) < len(current.val):
#             return flower_helper(current.left, flower)
#         else:
#             return flower_helper(current.right, flower)
        
# class TreeNode:
#     def __init__(self, value, left=None, right=None):
#         self.val = value
#         self.left = left
#         self.right = right

# def find_flower(root, flower):
#     if root is None:
#         return False
    
#     # If the current node matches the target flower, return True
#     if root.val == flower:
#         return True
    
#     # Recursively search in the left and right subtrees
#     return find_flower(root.left, flower) or find_flower(root.right, flower)
    
# print("Lily" < "Rose")  
# print("Lilac" < "Lily")  
# print("------")

# """
#          Rose
#         /    \
#        /      \
#      Lily     Daisy
#     /    \        \
# Orchid  Lilac    Dahlia
# """

# flower_field = TreeNode("Rose", 
#                         TreeNode("Lily", TreeNode("Orchid"), TreeNode("Lilac")),
#                                 TreeNode("Daisy", None, TreeNode("Dahlia")))

# print(find_flower(flower_field, "Lilac"))
# print(find_flower(flower_field, "Hibiscus"))
from collections import deque 

# Tree Node class
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def print_tree(root):
    if not root:
        return "Empty"
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    print(result)


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

# root = TreeNode("Poseidon")
# atlantis = TreeNode("Atlantis")
# oceania = TreeNode("Oceania")
# coral = TreeNode("Coral")
# pearl = TreeNode("Pearl")
# kelp = TreeNode("Kelp")
# reef = TreeNode("Reef")

# root.left = atlantis
# root.right = oceania

# atlantis.left = coral
# atlantis.right = pearl

# oceania.left = kelp
# oceania.right = reef

# print_tree(root)

# def mertwins(root):
#     if not root.left or not root.right:
#         return False
    
#     return root.left.val == root.right.val
    

# """
#       Mermother
#        /    \
#     Coral   Coral
# """
# root1 = TreeNode("Mermother", TreeNode("Coral"), TreeNode("Coral"))

# """
#       Merpapa
#        /    \
#    Calypso  Coral
# """
# root2 = TreeNode("Merpapa", TreeNode("Calypso"), TreeNode("Coral"))

# """
#       Merenby
#            \    
#          Calypso  
# """
# root3 = TreeNode("Merenby", None, TreeNode("Calypso"))

# print(mertwins(root1))
# print(mertwins(root2))
# print(mertwins(root3))

# def get_decision(root):
#     if not root.left and not root.right:
#         return root.val
    
#     match root.val:
#         case "OR":
#             return root.left.val or root.right.val
#         case "AND":
#             return root.left.val and root.right.val

# """
#         OR
#       /    \
#     True  False
# """
# expression1 = TreeNode("OR", TreeNode(True), TreeNode(False))

# """
#        False
# """
# expression2 = TreeNode(False)

# print(get_decision(expression1))
# print(get_decision(expression2))

# def leftmost_path_recursive(root):
#     return helper(root, [])

# def helper(root, path):
#     if not root:
#         return path
    
#     path.append(root.val)

#     return helper(root.left, path) 
# #T: O(logn) for balanced, O(n) for unbalanced

# def leftmost_path_iterative(root):
#     path = []
#     while root:
#         path.append(root.val)
#         root = root.left
    
#     return path


# """
#         CaveA
#        /      \
#     CaveB    CaveC
#     /   \        \
# CaveD CaveE     CaveF  
# """
# system_a = TreeNode("CaveA", 
#                   TreeNode("CaveB", TreeNode("CaveD"), TreeNode("CaveE")), 
#                           TreeNode("CaveC", None, TreeNode("CaveF")))

# """
#   CaveA
#       \
#       CaveB
#         \
#         CaveC  
# """
# system_b = TreeNode("CaveA", None, TreeNode("CaveB", None, TreeNode("CaveC")))

# print(leftmost_path(system_a))
# print(leftmost_path(system_b))

def explore_reef(root):
    return helper(root, [])

def helper(root, path):
    if not root:
        return path
    
    path.append(root.val)
    helper(root.left, path)
    helper(root.right, path)

    return path

"""
         CoralA
        /     \
     CoralB  CoralC
     /   \      
 CoralD CoralE  
"""

reef = TreeNode("CoralA", 
                TreeNode("CoralB", TreeNode("CoralD"), TreeNode("CoralE")), 
                          TreeNode("CoralC"))

print(explore_reef(reef))

def count_coral(root):
    if not root:
        return 0
    
    return 1 + count_coral(root.left) + count_coral(root.right)

"""
          Staghorn
         /        \
        /          \
    Sea Fan      Sea Whip
    /     \       /   
 Bubble  Table  Star
  /
Fire
"""
reef1 = TreeNode("Staghorn", 
                TreeNode("Sea Fan", TreeNode("Bubble", TreeNode("Fire")), TreeNode("Table")),
                        TreeNode("Sea Whip", TreeNode("Star")))

"""
     Fire
    /    \
   /      \ 
Black    Star
        /  
     Lettuce 
           \
        Sea Whip
"""
reef2 = TreeNode("Fire", 
                TreeNode("Black"), 
                        TreeNode("Star", 
                                  TreeNode("Lettuce", None, TreeNode("Sea Whip"))))

print(count_coral(reef1))
print(count_coral(reef2))

def ocean_depth(root):
    if not root:
        return 0
    
    return max(ocean_depth(root.left), ocean_depth(root.right)) + 1

"""
                Sunlight
               /        \
              /          \
          Twilight      Squid
         /       \           \   
      Abyss  Anglerfish    Giant Squid
      /
  Trenches
"""
ocean = TreeNode("Sunlight", 
                TreeNode("Twilight", 
                        TreeNode("Abyss", 
                                TreeNode("Trenches")), TreeNode("Anglerfish")),
                                        TreeNode("Squid", TreeNode("Giant Squid")))

"""
    Spray Zone
    /         \
   /           \ 
Beach       High Tide
            /  
      Middle Tide
              \
            Low Tide
"""
tidal_zones = TreeNode("Spray Zone", 
                      TreeNode("Beach"), 
                              TreeNode("High Tide", 
                                      TreeNode("Middle Tide", None, TreeNode("Low Tide"))))

print(ocean_depth(ocean))
print(ocean_depth(tidal_zones))