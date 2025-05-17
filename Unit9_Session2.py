# class TreeNode():
#      def __init__(self, value, left=None, right=None):
#         self.val = value
#         self.left = left
#         self.right = right

# def paths(root):
    
#     paths = []
#     def helper(root, curr_path):
#         if not root:
#             return

#         curr_path.append(str(root.val))

#         if not root.left and not root.right:
#             paths.append("->".join(curr_path))
#         else:
#             helper(root.left, curr_path)
#             helper(root.right, curr_path)
        
#         curr_path.pop()

#     helper(root, [])
    
#     return paths

# root = TreeNode(14)
# a = TreeNode(8)
# b = TreeNode(28)
# c = TreeNode(3)
# d = TreeNode(2)
# e = TreeNode(6)
# f = TreeNode(15)

# root.left = a
# root.right = b

# a.left = c
# c.left = d
# c.right = e

# b.left = f

# print(paths(root))

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

#-----------------------------------------------------------
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def treeheight(root):
    #time complexity: o(n)
    #space complexity: o(h)
    if not root:
        return 0
        
    return 1 + max(treeheight(root.left), treeheight(root.right))

def is_balanced_old(display):
    #time complexity: o(n2)
    #space complexity: o(h)
    if not display:
        return True
    
    if abs(treeheight(display.left) - treeheight(display.right)) <= 1:
        return is_balanced(display.left) and is_balanced(display.right)
    else:
        return False
    
def is_balanced(display):
    def checkbalance(display):
        if not display:
            return True, 0
        
        balanced_left, height_left = checkbalance(display.left)
        balanced_right, height_right = checkbalance(display.right)

        curr_height = max(height_right, height_left) + 1

        if balanced_right and balanced_left:
            return abs(height_left - height_right) <= 1, curr_height
        else:
            return False, curr_height
    
    balanced, _ = checkbalance(display)
    return balanced

"""
      🎂
     /  \
   🥮   🍩
       /  \  
     🥖    🧁

"""
# Using build_tree() function included at top of page
baked_goods = ["🎂", "🥮", "🍩", "🥖", "🧁"]
display1 = build_tree(baked_goods)

"""
          🥖
         /  \
       🧁    🧁
       /       \  
      🍪       🍪
     /           \
    🥐           🥐  

"""
baked_goods = ["🥖", "🧁", "🧁", "🍪", None, None, "🍪", "🥐", None, None, "🥐"]
display2 = build_tree(baked_goods)


print(is_balanced(display1)) 
print(is_balanced(display2))  
    

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def sum_each_days_orders(orders):
    #time complexity: O(n) - I'm visiting every node
    #space complexity O(w) - w = widest width of tree
    if not orders:
        return 0
    
    sums = []
    queue = deque([orders])

    while queue:
        level_size = len(queue)

        level_sum = 0
        for _ in range(level_size):
            curr = queue.popleft()
            level_sum += curr.val

            if curr.left:
                queue.append(curr.left)
            
            if curr.right:
                queue.append(curr.right)
        
        sums.append(level_sum)
    
    return sums
        
"""
      4
     / \
    2   6
   / \  
  1   3
"""

# Using build_tree() function included at top of page
order_sizes = [4, 2, 6, 1, 3]
orders = build_tree(order_sizes)

print(sum_each_days_orders(orders))


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def sweet_difference(chocolates):
    #time complexity: O(n) --> looping through every node
    #space complexity: O(w) --> widest level in tree
    if not chocolates:
        return []
    
    sweetness_diffs = []
    queue = deque([chocolates])
    while queue:
        level_size = len(queue)
        min = float("inf")
        max = float("-inf")
        for _ in range(level_size):
            curr = queue.popleft()

            if curr.val < min:
                min = curr.val
            
            if curr.val > max:
                max = curr.val

            if curr.left:
                queue.append(curr.left)
            
            if curr.right:
                queue.append(curr.right)
        sweetness_diffs.append(max - min)
    
    return sweetness_diffs

"""
  3
 / \
9  20
   / \
  15  7
"""
# Using build_tree() function included at top of page
sweetness_levels1 = [3, 9, 20, None, None, 15, 7]
chocolate_box1 = build_tree(sweetness_levels1)

"""
    1
   / \
  2   3
 / \   \
4   5   6

"""
sweetness_levels2 = [1, 2, 3, 4, 5, None, 6]
chocolate_box2 = build_tree(sweetness_levels2)

print(sweet_difference(chocolate_box1))  
print(sweet_difference(chocolate_box2))  


class TreeNode():
     def __init__(self, flavor, left=None, right=None):
        self.val = flavor
        self.left = left
        self.right = right

def can_rearrange_orders(order1, order2):
    #n = nodes in order1, m = nodes in order2
    #Time complexity: O(n) or O(m), whichever is smaller 
    #Space complexity: O(h), height of the smaller tree
    if not order1 and not order2:
        return True
    
    if (order1 and not order2) or (order2 and not order1):
        return False
    
    if order1.val == order2.val:
        original_l_r = can_rearrange_orders(order1.left, order2.left) and can_rearrange_orders(order1.right, order2.right)

        if original_l_r:
            return True
        else:
            swapped_l_r = can_rearrange_orders(order1.right, order2.left) and can_rearrange_orders(order1.left, order2.right)
            return swapped_l_r
    else:
        return False
    #Recursively check if trees are equal
    #If their root nodes are equal, check if their left and right subtrees are equal
    #if their left and right subtrees aren't equal then check if the swapped versions are equal
    #If neither are equal, return false

"""
              Red Velvet                             Red Velvet
             /          \                           /           \
        Vanilla         Lemon                   Lemon            Vanilla
        /      \        /   \                  /     \           /      \
      Ube    Almond  Chai   Carrot       Carrot      Chai    Almond    Ube 
                     /   \        \       /          /   \      
                 Chai   Maple   Smore   Smore    Maple   Chai
"""

# Using build_tree() function included at top of page
flavors1 = ["Red Velvet", "Vanilla", "Lemon", "Ube", "Almond", "Chai", "Carrot", 
            None, None, None, None, "Chai", "Maple", None, "Smore"]
flavors2 = ["Red Velvet", "Lemon", "Vanilla", "Carrot", "Chai", "Almond", "Ube", "Smore", None, "Maple", "Chai"]
order1 = build_tree(flavors1)
order2 = build_tree(flavors2)

print(can_rearrange_orders(order1, order2))

class TreeNode():
     def __init__(self, order_size, left=None, right=None):
        self.val = order_size
        self.left = left
        self.right = right

def larger_order_tree(orders):
    #time complexity: O(n) --> visit every node
    #space complexity: O(h) --> max height of recursion call stack = height of tree
    #backwards inorder traversal
    def backwards_inorder(orders, size):
        if not orders:
            return orders, size
        
        orders.right, size = backwards_inorder(orders.right, size)

        size += orders.val
        orders.val = size 

        orders.left, size = backwards_inorder(orders.left, size)

        return orders, size
    
    orders, _ = backwards_inorder(orders, 0)
    return orders


"""
         4
       /   \
      /     \
     1       6
    / \     / \
   0   2   5   7
        \       \
         3       8   
"""
# using build_tree() function included at top of page
order_sizes = [4,1,6,0,2,5,7,None,None,None,3,None,None,None,8]
orders = build_tree(order_sizes)

# using print_tree() function included at top of page
print_tree(larger_order_tree(orders))

class TreeNode():
     def __init__(self, order, left=None, right=None):
        self.val = order
        self.left = left
        self.right = right

def find_next_order(order_tree, order):
    #BFS
    #Time complexity: O(n) (visit every node in the worst case)
    #Space complexity: O(w) (width of the tree at the widest point)
    if not order_tree:
        return None
    
    queue = deque([order_tree])
    while queue:
        level_size = len(queue)
        for i in range(level_size):
            curr = queue.popleft()

            if curr.val == order.val:
                if i == level_size - 1:
                    return TreeNode(None)
                else:
                    return queue.popleft()

            if curr.left:
                queue.append(curr.left)
            
            if curr.right:
                queue.append(curr.right)

"""
        Cupcakes
       /       \ 
   Macaron     Cookies      
        \      /      \
      Cake   Eclair   Croissant
"""
cupcakes = TreeNode("Cupcakes")
macaron = TreeNode("Macaron")
cookies = TreeNode("Cookies")
cake = TreeNode("Cake")
eclair = TreeNode("Eclair")
croissant = TreeNode("Croissant")

cupcakes.left, cupcakes.right = macaron, cookies
macaron.right = cake
cookies.left, cookies.right = eclair, croissant

next_order1 = find_next_order(cupcakes, cake)
next_order2 = find_next_order(cupcakes, cookies)
print(next_order1.val)
print(next_order2.val)

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def mirror_tree(root):
    #Time: O(n) ---> visiting every node
    #Space: Preorder DFS traversal, O(h) --> max height of call stack
    if not root:
        return root
    
    root.left, root.right = root.right, root.left

    root.left = mirror_tree(root.left)
    root.right = mirror_tree(root.right)

    return root

"""
      🧛‍♂️
     /   \
    💪🏼    🤳
    /      \
   👟       👞
"""
# Using build_tree() function included at the top of the page
body_parts = ["🧛‍♂️", "💪🏼", "🤳", "👟", None, None, "👞"]
vampire = build_tree(body_parts)


"""
      🎃
     /   \
    😈    🕸️
         /  \
       🧟‍♂️    👻
"""
spooky_objects = ["🎃", "😈", "🕸️", None, None, "🧟‍♂️", "👻"]
spooky_tree = build_tree(spooky_objects)

# Using print_tree() function included at the top of the page
print_tree(mirror_tree(vampire))
print_tree(mirror_tree(spooky_tree)) 

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def max_pumpkins_path(root):
    #Post-Order DFS
    def postorder(root):
        #Time complexity = O(n) visiting every node once
        #Space complexity = O(h * n) --> height of callstack * queues I keep making
        if not root:
            return deque(), 0
        
        queue = None
        curr_max = 0

        queueL, left_max = postorder(root.left)
        queueR, right_max = postorder(root.right)

        if left_max > right_max:
            queue = queueL
            curr_max = left_max
        else:
            queue = queueR
            curr_max = right_max
        
        queue.appendleft(root.val)
        return queue, curr_max + root.val
    
    node_list, _ = postorder(root)
    return list(node_list)

"""
    7
   / \
  3   10
 /   /  \
1   5    15
"""
# Using build_tree() function includedd at the top of the page
pumpkin_quantities = [7, 3, 10, 1, None, 5, 15]
root1 = build_tree(pumpkin_quantities)

"""
    12
   /  \
  3     8
 / \     \
4   50    10
"""
pumpkin_quantities = [12,3, 8, 4, 50, None, 10]
root2 = build_tree(pumpkin_quantities)

print(max_pumpkins_path(root1)) 
print(max_pumpkins_path(root2)) 

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def largest_pumpkins(pumpkin_patch):
    #Time Complexity: O(n)
    #Space Complexity: O(w)
    if not pumpkin_patch:
        return []
    
    max_pumps = []
    queue = deque([pumpkin_patch])
    while queue:
        level_size = len(queue)
        max_pump = float("-inf")
        for _ in range(level_size):
            curr = queue.popleft()

            if curr.val > max_pump:
                max_pump = curr.val

            if curr.left:
                queue.append(curr.left)

            if curr.right:
                queue.append(curr.right)
        
        max_pumps.append(max_pump)
    
    return max_pumps

"""
    1
   /  \
  3    2
 / \    \   
5   3    9
"""
# Using build_tree() function included at the top of the page
pumpkin_sizes = [1, 3, 2, 5, 3, None, 9]
pumpkin_patch = build_tree(pumpkin_sizes)

print(largest_pumpkins(pumpkin_patch))

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def count_clusters(hotel):
    #Time: O(n)
    #Space: O(h)
    #Post-Order DFS
    if not hotel:
        return 0
    
    #Count clusters in left subtree and right subtree
    clustersL = count_clusters(hotel.left)
    clustersR = count_clusters(hotel.right)

    left_val = None
    right_val = None

    if hotel.left:
        left_val = hotel.left.val
    if hotel.right:
        right_val = hotel.right.val

    #See if any of those clusters continue into the current tree
    if hotel.left or hotel.right:
        if (hotel.val == left_val) and (hotel.val == right_val):
            return clustersL + clustersR - 1
        elif (hotel.val == left_val) or (hotel.val == right_val):
            return clustersL + clustersR
        else:
            return clustersL + clustersR + 1
        #Root val == left and right vals --> clusters = (left + right - 2)
        #Root val != keft and right vals --> clusters = (left + right + 1)
        #Root val == left or right clustesr --> clusters = (left + right)
    else:
        return 1


"""
     👻
   /    \
  👻     🧛🏾
 /  \      
👻  🧛🏾      
"""
# Using build_tree() function included at the top of the page
themes = ["👻", "👻", "🧛🏾", "👻", "🧛🏾"]
hotel = build_tree(themes)

print(count_clusters(hotel))

class TreeNode():
     def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def purge_hotel(hotel):
    #Time complexity: O(n * h), h = height of tree, performing DFS (O(n)) multiple times in the while loop
    #Space Complexity: O(n) = all nodes in tree appended to list
    #DFS Post-Order
    def delete_leaves(hotel, list):
        #Return the root of the tree with the leaves deleted 
        if not hotel:
            return None, list
        
        if not hotel.left and not hotel.right:
            list.append(hotel.val)
            return None, list
        
        hotel.left, _ = delete_leaves(hotel.left, list)
        hotel.right, _ = delete_leaves(hotel.right, list)

        return hotel, list
    
    delete_list = []

    while hotel:
        deleted = []
        hotel, deleted = delete_leaves(hotel, deleted)

        delete_list.append(deleted)
    
    return delete_list
        
"""
      👻
     /  \
   😱   🧛🏾‍♀️
  /  \
 💀  😈
"""

# Using build_tree() function included at the top of the page
guests = ["👻", "😱", "🧛🏾‍♀️", "💀", "😈"]
hotel = build_tree(guests)

# Using print_tree() function included at the top of the page
print_tree(hotel)
print(purge_hotel(hotel))

class TreeNode():
     def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def smallest_subtree_with_deepest_rooms(hotel):
    #DFS post-order
    #Time complexity: O(n) (visting most childre)
    #Space complexity: O(h) (depth of recursion stack)
    #Depth of children
    #Get depth of each subtree
    #If depth is the same, return the root 
    #If depth of one subtree is greater than the other, go into that subtree
    def find_node(root):
        if not root:
            return None, 0
        
        left, l_size = find_node(root.left)
        right, r_size = find_node(root.right)

        if l_size == r_size:
            return root, l_size + 1
        elif l_size > r_size:
            return left, l_size + 1
        else:
            return right, r_size + 1
    
    remove_subtree, _ = find_node(hotel)
    return remove_subtree
   

"""
         Lobby
        /     \
       /       \
      101      102
     /   \    /   \
   201  202  203  204
        /  \ 
      😱   👻
"""
# Using build_tree() included at top of page
rooms = ["Lobby", 101, 102, 201, 202, 203, 204, None, None, "😱", "👻"]
hotel1 = build_tree(rooms)

"""
      Lobby
     /     \
   101     102
     \
     💀
"""
rooms = ["Lobby", 101, 102, None, "💀"]
hotel2 = build_tree(rooms)

# Using print_tree() function included at top of page
print_tree(smallest_subtree_with_deepest_rooms(hotel1))
print_tree(smallest_subtree_with_deepest_rooms(hotel2))