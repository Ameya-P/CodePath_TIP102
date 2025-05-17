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

#------------------------------------------------------------------------------------------

# class TreeNode:
#     def __init__(self, value, left=None, right=None):
#         self.val = value
#         self.left = left
#         self.right = right

# def is_balanced(display):
#     if not display:
#         return True
    
#     def height(root):
#         if not root:
#             return 0
        
#         return 1 + max(height(root.left), height(root.right))
    
#     if abs(height(display.left) - height(display.right)) > 1:
#         return False
#     else:
#         return is_balanced(display.left) and is_balanced(display.right)
    
    
# """
#       🎂
#      /  \
#    🥮   🍩
#        /  \  
#      🥖    🧁

# """
# # Using build_tree() function included at top of page
# baked_goods = ["🎂", "🥮", "🍩", "🥖", "🧁"]
# display1 = build_tree(baked_goods)

# """
#           🥖
#          /  \
#        🧁    🧁
#        /       \  
#       🍪       🍪
#      /           \
#     🥐           🥐  

# """
# baked_goods = ["🥖", "🧁", "🧁", "🍪", None, None, "🍪", "🥐", None, None, "🥐"]
# display2 = build_tree(baked_goods)


# print(is_balanced(display1)) 
# print(is_balanced(display2))

# class TreeNode:
#     def __init__(self, value, left=None, right=None):
#         self.val = value
#         self.left = left
#         self.right = right

# from collections import defaultdict

# def sum_each_days_orders(orders):
#     if not orders:
#         return 0
    
#     sums = defaultdict(int)
#     queue = deque([(orders, 0)])

#     while queue:
#         tuple = queue.popleft()
#         node = tuple[0]
#         level = tuple[1]
#         sums[level] += node.val
#         if node.left:
#             queue.append((node.left, level+1))
#         if node.right:
#             queue.append((node.right, level+1))
    
#     return list(sums.values())
        

# #--------------Test Cases--------------
# """
#       4
#      / \
#     2   6
#    / \  
#   1   3
# """

# # Using build_tree() function included at top of page
# order_sizes = [4, 2, 6, 1, 3]
# orders = build_tree(order_sizes)

# print(sum_each_days_orders(orders))


# # class TreeNode:
# #     def __init__(self, value, left=None, right=None):
# #         self.val = value
# #         self.left = left
# #         self.right = right

# def sum_each_days_orders(orders):
#     result = []
#     if not orders:
#         return result

#     queue = deque([orders])
    
#     while queue:
#         level_sum = 0
#         level_size = len(queue)
#         for i in range(level_size):
#             # sum variable += current node value
#             level_sum += orders.val
#             result.append(sum(queue))
#             if orders.left :
#                 queue.append(orders.left) 
#             if orders.right :
#                 queue.append(orders.right)
#             queue.popleft() 
#         # append sum variable to the result list 
#     return result
    
# #--------------Test Cases--------------
# """
#       4
#      / \
#     2   6
#    / \  
#   1   3
# """

# # Using build_tree() function included at top of page
# '''''''''
# order_sizes = [4, 2, 6, 1, 3]
# orders = build_tree(order_sizes)

# print(sum_each_days_orders(orders))
# '''

# class TreeNode:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# def sum_each_days_orders(orders):
#     if not orders:
#         return []
    
#     results = []
#     queue = deque([orders])  # Start with the root
    
#     while queue:
#         level_sum = 0
#         level_size = len(queue)
        
#         for _ in range(level_size):
#             node = queue.popleft()
#             level_sum += node.val
            
#             # Add child nodes to the queue
#             if node.left:
#                 queue.append(node.left)
#             if node.right:
#                 queue.append(node.right)
        
#         # Append the sum of the current level to results
#         results.append(level_sum)
    
#     return results
    
# # Example Usage:
# order_sizes = [4, 2, 6, 1, 3]
# orders = build_tree(order_sizes)

# print(sum_each_days_orders(orders)) 

# class TreeNode:
#     def __init__(self, value, left=None, right=None):
#         self.val = value
#         self.left = left
#         self.right = right

# def sweet_difference(chocolates):
#     if not chocolates:
#         return 0
    
#     results = []
#     queue = deque([chocolates])

#     while queue:
#         level_diff = []
#         level_size = len(queue)

#         if level_size == 1:
#             results.append(0)
#             continue

#         for _ in range(level_size):
#             node = queue.popleft()
#             level_diff.append(node.val)

#             # Add child nodes to the queue
#             if node.left:
#                 queue.append(node.left)
#             if node.right:
#                 queue.append(node.right)
#------------------------------------------------------------------------------------------

# class TreeNode():
#      def __init__(self, quantity, left=None, right=None):
#         self.val = quantity
#         self.left = left
#         self.right = right

# def merge_orders(order1, order2):
#     if not order1 and not order2:
#         return None
    
#     new_root = None

#     if order1 and order2:
#         new_root = TreeNode(order1.val + order2.val)
#         new_root.left = merge_orders(order1.left, order2.left)
#         new_root.right = merge_orders(order1.right, order2.right)
#     if order1 and not order2:
#         new_root = order1
#         new_root.left = merge_orders(order1.left, None)
#         new_root.right = merge_orders(order1.right, None)
#     if order2 and not order1:
#         new_root = order2
#         new_root.left = merge_orders(None, order2.left)
#         new_root.right = merge_orders(None, order2.right)

#     return new_root

# """
#      1             2         
#     /  \         /   \       
#    3    2       1     3   
#  /               \      \   
# 5                 4      7   
# """
# # Using build_tree() function included at top of page
# cookies1 = [1, 3, 2, 5]
# cookies2 = [2, 1, 3, None, 4, None, 7]
# order1 = build_tree(cookies1)
# order2 = build_tree(cookies2)

# # Using print_tree() function included at top of page
# print_tree(merge_orders(order1, order2))

# class Puff():
#      def __init__(self, flavor, left=None, right=None):
#         self.val = flavor
#         self.left = left
#         self.right = right

# def print_design(design):
#     if not design:
#         return
    
#     queue = deque([design])
#     visited = []

#     while queue:
#         curr_flavor = queue.popleft()
#         visited.append(curr_flavor.val)

#         if curr_flavor.left:
#             queue.append(curr_flavor.left)
        
#         if curr_flavor.right:
#             queue.append(curr_flavor.right)
    
#     print(visited)

# """
#             Vanilla
#            /       \
#       Chocolate   Strawberry
#       /     \
#   Vanilla   Matcha  
# """
# croquembouche = Puff("Vanilla", 
#                     Puff("Chocolate", Puff("Vanilla"), Puff("Matcha")), 
#                     Puff("Strawberry"))
# print_design(croquembouche)

# class TreeNode():
#      def __init__(self, value, left=None, right=None):
#         self.val = value
#         self.left = left
#         self.right = right

# def max_tiers_df(cake):
#     if not cake:
#         return 0
    
#     return 1 + max(max_tiers(cake.left), max_tiers(cake.right))

# def max_tiers(cake):
#     if not cake: 
#         return 0
    
#     queue = deque([cake])
#     level_num = 0

#     while queue:
#         level = deque()
#         while queue:
#             level.append(queue.popleft())
        
#         while level:
#             node = level.popleft()
#             if node.left:
#                 queue.append(node.left)
            
#             if node.right:
#                 queue.append(node.right)
        
#         level_num += 1
    
#     return level_num

# """
#         Chocolate
#         /        \
#     Vanilla    Strawberry
#                 /     \
#          Chocolate    Coffee
# """
# # Using build_tree() function included at top of page
# cake_sections = ["Chocolate", "Vanilla", "Strawberry", None, None, "Chocolate", "Coffee"]
# cake = build_tree(cake_sections)

# print(max_tiers(cake))

# class TreeNode():
#      def __init__(self, value, left=None, right=None):
#         self.val = value
#         self.left = left
#         self.right = right

# def can_fulfill_order(inventory, order_size):
#     if not inventory:
#         return order_size == 0
    
#     order_size -= inventory.val
#     return can_fulfill_order(inventory.left, order_size) or can_fulfill_order(inventory.right, order_size)

# """
#              5
#            /   \
#           4     8
#         /      /  \
#        11     13   4
#       /  \          \
#      7   2           1   
# """

# # Using build_tree() function included at top of the page
# quantities = [5,4,8,11,None,13,4,7,2,None,None,None,1]
# baked_goods = build_tree(quantities)

# print(can_fulfill_order(baked_goods, 22))
# print(can_fulfill_order(baked_goods, 2))

# class TreeNode():
#      def __init__(self, flavor, left=None, right=None):
#         self.val = flavor
#         self.left = left
#         self.right = right

# def zigzag_icing_order(cupcakes):
#     cupcake_order = []

#     if not cupcakes:
#         return cupcake_order
    
#     queue = deque([cupcakes])
#     level_num = 1

#     while queue:
#         level_stack  = []
#         level_size = len(queue)

#         for i in range(level_size):
#             node = queue.popleft()
#             level_stack.append(node.val)

#             if node.left:
#                 queue.append(node.left)
            
#             if node.right:
#                 queue.append(node.right)
        
#         if level_num % 2 == 0:
#             while level_stack:
#                 cupcake_order.append(level_stack.pop())
#         else:
#             cupcake_order.extend(level_stack)
        
#         level_num += 1
    
#     return cupcake_order

# """
#             Chocolate
#            /         \
#         Vanilla       Lemon
#        /              /    \
#     Strawberry   Hazelnut   Red Velvet   
# """

# # Using build_tree() function included at top of page
# flavors = ["Chocolate", "Vanilla", "Lemon", "Strawberry", None, "Hazelnut", "Red Velvet"]
# cupcakes = build_tree(flavors)
# print(zigzag_icing_order(cupcakes))

class TreeNode():
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def is_clone(guest1, guest2):
    #pre-order traversal 
    #if both trees are empty, return true
    if not guest1 and not guest2:
        return True

    #if one tree is empty and the other isn't, return false
    if (guest1 and not guest2) or (guest2 and not guest1):
        return False

    #if neither tree is empty, check their values 
    if guest1.val == guest2.val:
        return is_clone(guest1.left, guest2.left) and is_clone(guest1.right, guest2.right)
    else:
        return False

    #if their root nodes aren't equal, return false

    #if their root nodes are equal, check if their sub trees are clones

    #if their subtrees are clones, return true

    """
     John Doe               John Doe
     /      \             /       \
  6 ft    Brown Eyes      6ft      Brown Eyes
"""
guest1 = TreeNode("John Doe", TreeNode("6 ft"), TreeNode("Brown Eyes"))
guest2 = TreeNode("John Doe", TreeNode("6 ft"), TreeNode("Brown Eyes"))

"""
     John Doe         John Doe
     /                       \
   6 ft                     6 ft
"""
guest3 = TreeNode("John Doe", TreeNode("6 ft"))
guest4 = TreeNode("John Doe", None, TreeNode("6 ft"))

print(is_clone(guest1, guest2))
print(is_clone(guest3, guest4))

class Room():
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def map_hotel(hotel):
    visited = []

    if not hotel:
        return visited
    
    queue = deque([hotel])

    while queue:
        current = queue.popleft()

        visited.append(current.val)

        if current.left:
            queue.append(current.left)
        
        if current.right:
            queue.append(current.right)
    
    return visited

"""
         Lobby
        /     \
       /       \
      101      102
     /   \    /   \
   201  202  203  204
   /                \ 
 301                302
"""

hotel = Room("Lobby", 
                Room(101, Room(201, Room(301)), Room(202)),
                Room(102, Room(203), Room(204, None, Room(302))))

print(map_hotel(hotel))


class TreeNode():
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

# def min_depth_depth_first(door):
#     #pre-order traversal 

#     #If there isn't a path, the minimum depth is 0
#     if not door:
#         return 0

#     #If there is a path, add 1 to the smallest path we find in one of the subtrees
#     if door.left and door.right:
#         return 1 + min(min_depth(door.left), min_depth(door.right))
#     elif door.left:
#         return 1 + min_depth(door.left)
#     elif door.right:
#         return 1 + min_depth(door.right)

# """
#      Door
#     /    \
#  Attic    Cursed Room
#          /       \
#       Crypt     Haunted Cellar
# """

# door = Room("Door", Room("Attic"), Room("Cursed Room", Room("Crypt"), Room("Haunted Cellar")))

# print(min_depth(door))


def min_depth(door):
    #Go through nodes level by level
    #If a node doesn't have any children, then we can stop
    if not door:
        return 0
    
    curr_level = 1
    queue = deque([door])

    while queue:
        level_size = len(queue)

        for _ in range(level_size):
            curr = queue.popleft()
            if not curr.left and not curr.right:
                return curr_level
            
            if curr.left:
                queue.append(curr.left)
            
            if curr.right:
                queue.append(curr.right)
        
        curr_level += 1
    
    """
     Door
    /    \
 Attic    Cursed Room
         /       \
      Crypt     Haunted Cellar
"""

door = Room("Door", Room("Attic", Room("Attic2")), Room("Cursed Room", Room("Crypt"), Room("Haunted Cellar")))

print(min_depth(door))


class TreeNode():
     def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def reverse_odd_levels(hotel):
    if not hotel:
        return None
    
    level = 0
    queue = deque([hotel])

    while queue:
        level_size = len(queue)
        level_size_vals = deque()
        level_stack = []

        for _ in range(level_size):
            curr = queue.popleft()

            level_size_vals.append(curr.val)
            level_stack.append(curr)

            if curr.left:
                queue.append(curr.left)

            if curr.right:
                queue.append(curr.right)
        
        if level % 2 != 0:
            for _ in range(len(level_stack)):
                node = level_stack.pop()
                node.val = level_size_vals.popleft()
        
        level += 1
        
    return hotel

"""
        Lobby
      /      \
     102     101
     / \     /  \
   201 202 203 204 
"""
hotel = Room("Lobby", 
            Room(102, Room(201), Room (202)), 
                Room(101, Room(203), Room(204)))

# Using print_tree() function included at the top
print_tree(reverse_odd_levels(hotel))

class TreeNode():
     def __init__(self, value, key, left=None, right=None):
        self.key = key
        self.val = value
        self.left = left
        self.right = right

def kth_spookiest(root, k):
    def inorder(node):
        if not node:
            return None
        
        left_val = inorder(node.left)
        if left_val:
            return left_val
        
        nonlocal count
        count += 1
        if count == k:
            return node.val
        
        return inorder(node.right)
    count = 0
    return inorder(root)

"""
    (3, Lobby) 
   /         \
(1, 101)   (4, 102)
     \
     (2, 201)
"""

# Using build_tree() function at the top of the page
rooms = [(6, "Lobby"), (2, 101), (8, 102), None, (4, 201)]
hotel1 = build_tree(rooms)


"""
            (5, Lobby) 
            /         \
        (3, 101)   (6, 102)
        /      \
    (2, 201)  (4, 202)
    /
(1, 301)
"""
rooms = [(5, 'Lobby'), (3, 101), (6, 102), (2, 201), (4, 202), None, None, (1, 301)]
hotel2 = build_tree(rooms)

print(kth_spookiest(hotel1, 1))
print(kth_spookiest(hotel2, 3))