from collections import deque


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = left

class BST:
    def __init__(self, root=None):
        self.root = root
        self.size = 0

    def print_tree(self):
        queue = deque()
        queue.append(self.root)

        while queue:
            node = queue.popleft()
            print(node.value)
            queue.append(node.left)
            queue.append(node.right)

root = TreeNode(2)
left = TreeNode(1)
right = TreeNode(3)
righter = TreeNode(5)
root.left = left
root.right = right
right.right = righter

max_v = float("-inf")
def find_max(root):
    if not root:
        return float("-inf")

    max_val = root.val    
    left_max = find_max(root.left)
    right_max = find_max(root.right)

    if left_max > max_val:
        max_val = left_max
    
    if right_max > max_val:
        max_val = right_max

    return max_val

print(find_max(root))   

# if not root:
#             return True
        
#         if root.left and root.left.val >= root.val:
#             return False
        
#         if root.right and root.right.val <= root.val:
#             return False
        
#         return self.isValidBST(root.left) and self.isValidBST(root.right)
# -> bool

from collections import deque 

# Tree Node class
class TreeNode:
  def __init__(self, value, key=None, left=None, right=None):
      self.key = key
      self.val = value
      self.left = left
      self.right = right

def build_tree(values):
  if not values:
      return None

  def get_key_value(item):
      if isinstance(item, tuple):
          return item[0], item[1]
      else:
          return None, item

  key, value = get_key_value(values[0])
  root = TreeNode(value, key)
  queue = deque([root])
  index = 1

  while queue:
      node = queue.popleft()
      if index < len(values) and values[index] is not None:
          left_key, left_value = get_key_value(values[index])
          node.left = TreeNode(left_value, left_key)
          queue.append(node.left)
      index += 1
      if index < len(values) and values[index] is not None:
          right_key, right_value = get_key_value(values[index])
          node.right = TreeNode(right_value, right_key)
          queue.append(node.right)
      index += 1

  return root

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

# class TreeNode():
#      def __init__(self, value, left=None, right=None):
#          self.val = value
#          self.left = left
#          self.right = right
         
# def count_odd_splits(root):
#     #if no root, then return 0 - base case
#     if not root:
#         return 0
    
#     #recursivle go through
#     if root.val % 2 == 1:
#         return 1 + count_odd_splits(root.left) + count_odd_splits(root.right) 
#     else:
#         return count_odd_splits(root.left) + count_odd_splits(root.right)
    
# values = [2, 3, 5, 6, 7, None, 12]
# monstera = build_tree(values)

# print(count_odd_splits(monstera))
# print(count_odd_splits(None))
#---------------
#problem 2

# class TreeNode():
#      def __init__(self, value, left=None, right=None):
#          self.val = value
#          self.left = left
#          self.right = right
         
# def find_flower(inventory, name):
#     #Base Case
#     if not inventory:
#         return False

#     if inventory.val == name:
#         return True
    
#     #Recursive Case
#     if name < inventory.val:
#         return find_flower(inventory.left, name)
#     else:
#         return find_flower(inventory.right, name)
    
# values = ["Rose", "Lilac", "Tulip", "Daisy", "Lily", None, "Violet"]
# garden = build_tree(values)

# print(find_flower(garden, "Lilac"))  
# print(find_flower(garden, "Sunflower")) 
#-------------
#problem 3
# class TreeNode:
#     def __init__(self, value, left=None, right=None):
#         self.val = value
#         self.left = left
#         self.right = right

# def non_bst_find_flower(root, name):
#     if root is None:
#         return False
    
#     if root.val == name:
#         return True

#     return non_bst_find_flower(root.left, name) or non_bst_find_flower(root.right, name)

# values = ["Rose", "Lily", "Tulip", "Daisy", "Lilac", None, "Violet"]
# garden = build_tree(values)

# print(non_bst_find_flower(garden, "Lilac"))  
# print(non_bst_find_flower(garden, "Sunflower")) 
#------------------
#prob 4


# class TreeNode:
#     def __init__(self, value, left=None, right=None):
#         self.val = value
#         self.left = left
#         self.right = right

# def add_plant(collection, name):
#     #Base Case
#     if collection is None:
#         return TreeNode(name)
    
#     if name < collection.val:
#         collection.left = add_plant(collection.left, name)
#     elif name > collection.val:
#         collection.right = add_plant(collection.right, name)
#     else:
#         collection.right = TreeNode(name)

#     #Recursive Case
#     return collection
    
# values = ["Money Tree", "Fiddle Leaf Fig", "Snake Plant", "Aloe"]
# values = ["Money Tree", "Fiddle Leaf Fig"]
# collection = build_tree(values)

# # Using print_tree() function at the top of page
# print_tree(add_plant(collection, "Fiddle Leaf Fig"))
#--------------
    #problem 5

# class TreeNode:
#     def __init__(self, key, value, left=None, right=None):
#         self.key = key      # Plant price
#         self.val = value      # Plant name
#         self.left = left
#         self.right = right


# def sort_plants(collection):
#     plant_list = []
#     plant_helper(collection, plant_list)
#     return plant_list

# def plant_helper(collection, plant_list):
#     if not collection:
#         return 
    
#     plant_helper(collection.left, plant_list)
#     plant_list.append((collection.key, collection.val))
#     plant_helper(collection.right, plant_list)

#     return plant_list
    
# values = [(3, "Monstera"), (1, "Pothos"), (5, "Witchcraft Orchid"), None, (2, "Spider Plant"), (4, "Hoya Motoskei")]
# collection = build_tree(values)

# print(sort_plants(collection))
#problem 6
# class TreeNode:
#     def __init__(self, key, val, left=None, right=None):
#         self.key = key      # Plant price
#         self.val = val      # Plant name
#         self.left = left
#         self.right = right

# def pick_plant(root, budget):
#     return helper(root, budget, None)


# def helper(root, budget, pred):
#     if not root:
#         return None
    
#     if root.val > budget:
#         return helper(root.left, budget, pred)
    
#     if root.val == budget:
#         if root.left:
#             return find_max(root.left)
#         else:
#             return pred
    
#     if root.val < budget:
#         return helper(root.right, budget, root)
     

# def findmax(root):
#     if not root.right:
#         return root
    
#     if not root:
#         return None
    
#     return find_max(root.right)
    
    
    
# values = [(50, "Fiddle Leaf Fig"), (25, "Monstera"), (70, "Snake Plant"), (15, "Aloe"), 
#             (40, "Pothos"), (60, "Fern"), (80, "ZZ Plant")]
# inventory = build_tree(values)

# print(pick_plant(inventory, 50)) 
# print(pick_plant(inventory, 25)) 
# print(pick_plant(inventory, 15)) 

# print(find_max(inventory))

# class TreeNode:
#     def __init__(self, value, left=None, right=None):
#         self.val = value
#         self.left = left
#         self.right = right

# def remove_plant(collection, name):
#     if collection.val == name:
#         return None

#     prev = None
#     dir = None
#     current = collection

#     while current:
#         if current.val == name:
#             break

#         prev = current
#         if name < current.val:
#             current = current.left
#             dir = "l"
#         elif name > current.val:
#             current = current.right
#             dir = "r"
    
#     if not current.left and not current.right:
#         match dir:
#             case "l":
#                 prev.left = None
#             case "r":
#                 prev.right = None
    
#     if not current.left:
#         match dir:
#             case "l":
#                 prev.left = current.right
#             case "r":
#                 prev.right = current.right
    
#     if not current.right:
#         match dir:
#             case "l":
#                 prev.left = current.left
#             case "r":
#                 prev.right = current.left
    
#     if current.left and current.right:
#         prev_left = None
#         max_left = current.left

#         while max_left.right:
#             prev_left = max_left
#             max_left = max_left.right
        
#         if prev_left:
#             prev_left.right = None
        
#         match dir:
#             case "l":
#                 prev.left = max_left
#             case "r":
#                 prev.right = max_left
        
#         max_left.right = current.right
    
#     return collection

# """
#               Money Tree
#              /         \
#            Hoya        Pilea
#               \        /   \
#              Ivy    Orchid  ZZ Plant
# """

# # Using build_tree() function at the top of page
# values = ["Money Tree", "Hoya", "Pilea", None, "Ivy", "Orchid", "ZZ Plant"]
# collection = build_tree(values)

# # Using print_tree() function at the top of page
# print_tree(remove_plant(collection, "Pilea"))

# class TreeNode:
#     def __init__(self, value, left=None, right=None):
#         self.val = value
#         self.left = left
#         self.right = right

# def same_width(root):
#     return helper(root, root.val)

# def helper(root, val):
#     if not root:
#         return True
    
#     if root.val != val:
#         return False
    
#     return helper(root.left, val) and helper(root.right, val)

# root = TreeNode(7)
# root.left = TreeNode(7)
# root.right = TreeNode(3)
# print(same_width(root))

class Cichlid:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def find_lonely_cichlids(root):
    
    def helper(root, lonely_list):
        if not root:
            return
        
        if root.left and root.right:
            pass
        elif root.left and not root.right:
            lonely_list.append(root.left.val)
        elif root.right and not root.left:
            lonely_list.append(root.right.val)
        
        helper(root.left, lonely_list)
        helper(root.right, lonely_list)
        
        return 
    list = []
    helper(root, list)
    return list
    

"""
    A
   / \
  B   C
   \
    D
"""

# Using build_tree() function at the top of page
values = ['A', 'B', 'C', None, 'D']
family_1 = build_tree(values)

"""
     A
    / \
   B   C
  /   / \ 
 D   E   F
          \
           G
"""

values = ['A', 'B', 'C', None, 'D', None, 'E', 'F', None, None, None, None, None, 'G']
family_2 = build_tree(values)

"""
                 A
                / \
               B   C
              /     \ 
             D       E
            /         \
           F           G
          /             \
         H               I  
"""

values = ["A", "B", "C", "D", None, None, "E", "F", None, None, "G", "H", None, None, "I"]
family_3 = build_tree(values)

print(find_lonely_cichlids(family_1))
"""
     A
    / \
   B   C
  /   / \ 
 D   E   F
          \
           G
"""
a = TreeNode("A")
b = TreeNode("B")
c = TreeNode("C")
d = TreeNode("D")
e = TreeNode("E")
f = TreeNode("F")
g = TreeNode("G")

a.left = b
a.right = c
b.left = d
c.left = e
c.right = f
f.right = g
print(find_lonely_cichlids(a))
print(find_lonely_cichlids(family_3))

class TreeNode():
     def __init__(self, value, left=None, right=None):
         self.val = value
         self.left = left
         self.right = right
         
def locate_treasure(grotto, treasure):
    if not grotto:
        return False
    
    if treasure == grotto.val:
        return True
    elif treasure < grotto.val:
        return locate_treasure(grotto.left, treasure)
    elif treasure > grotto.val:
        return locate_treasure(grotto.right, treasure)
    

"""
             Snarfblat
            /        \
        Gadget       Whatzit
       /     \           \
Dinglehopper Gizmo       Whozit
"""


# Using build_tree() function at the top of page
values = ["Snarfblat", "Gadget", "Whatzit", "Dinglehopper", "Gizmo", None, "Whozit"]
grotto = build_tree(values)

print(locate_treasure(grotto, "Dinglehopper"))  
print(locate_treasure(grotto, "Thingamabob")) 

class TreeNode():
     def __init__(self, value, left=None, right=None):
         self.val = value
         self.left = left
         self.right = right
         
def add_treasure(grotto, new_item):
    if not grotto:
        return TreeNode(new_item)
    
    if new_item == grotto.val:
        pass
    elif new_item < grotto.val:
        grotto.left = add_treasure(grotto.left, new_item)
    elif new_item > grotto.val:
        grotto.right = add_treasure(grotto.right, new_item)
    
    return grotto

"""
             Snarfblat
            /        \
        Gadget       Whatzit
       /     \           \
Dinglehopper Gizmo       Whozit
"""

# Using build_tree() function at the top of page
values = ["Snarfblat", "Gadget", "Whatzit", "Dinglehopper", "Gizmo", None, "Whozit"]
grotto = build_tree(values)

# Using print_tree() function included at top of page
print_tree(add_treasure(grotto, "Thingamabob")) 

class Pearl:
    def __init__(self, size, left=None, right=None):
        self.val = size
        self.left = left
        self.right = right

def smallest_to_largest_recursive(pearls):
    sorted_list = []
    
    def inorder_traversal(node):
        if node:
            inorder_traversal(node.left)   
            sorted_list.append(node.val) 
            inorder_traversal(node.right)  
    
    inorder_traversal(pearls)
    return sorted_list

def smallest_to_largest_iterative(pearls):
    sorted_list = []
    stack = []

    curr = pearls

    while stack or curr:
        if curr:
            stack.append(curr)
            curr = curr.left
        else:
            curr = stack.pop()
            sorted_list.append(curr.val)
            curr = curr.right
    
    return sorted_list
    
values = [3, 1, 5, None, 2, 4, 8]

pearls = build_tree(values)

print(smallest_to_largest_recursive(pearls))
print(smallest_to_largest_iterative(pearls))

class Pearl:
    def __init__(self, size=0, left=None, right=None):
        self.val = size
        self.left = left
        self.right = right

def min_diff_in_pearl_sizes(pearls):
    if not pearls:
        return float("inf")
    
    min_diff = float("inf")
    if pearls.left and pearls.right:
        min_diff = min(pearls.val - pearls.left.val, pearls.right.val - pearls.val)
    elif pearls.left:
        min_diff = pearls.val - pearls.left.val
    elif pearls.right:
        min_diff = pearls.right.val - pearls.val

    min_dif_left = min_diff_in_pearl_sizes(pearls.left)
    min_dif_right = min_diff_in_pearl_sizes(pearls.right)

    return min(min_diff, min_dif_left, min_dif_right)

"""
        4
       / \
      2   6
     / \   \
    1   3   8
"""
# Use build_tree() function at top of page
values = [4, 2, 6, 0, 5, None, 9]
pearls = build_tree(values)

print(min_diff_in_pearl_sizes(pearls))  

class Pearl:
    def __init__(self, size, left=None, right=None):
        self.val = size
        self.left = left
        self.right = right

def pick_pearl(pearls, min_size):
    
    def helper(pearls, min_size, pred):
        if not pearls:
            return None
        
        if min_size == pearls:
            if node.
        if min_size < pearls:
            return helper(pearls.left, min_size, pearls)
        if min_size > pearls:
            return helper(pearls.right, min_size, pred)
    
    def min_node(pearls):
        if not pearls:
            return None
        
        min_left = min_node(pearls.left)
        min_right = min_node(pearls.right)

        if min_left and min_right:
            

    
    