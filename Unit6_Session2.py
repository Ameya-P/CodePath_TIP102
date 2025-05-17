# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next

# def is_circular(clues):
#     if clues is None:
#       return False
    
#     curr = clues

#     while curr:
#         if curr.next == clues:
#             return True
#         curr = curr.next
    
#     return False
    
        
# clue1 = Node("The stolen goods are at an abandoned warehouse")
# clue2 = Node("The mayor is accepting bribes")
# clue3 = Node("They dumped their disguise in the lake")
# clue1.next = clue2
# clue2.next = clue3
# clue3.next = clue1

# print(is_circular(clue1))

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

# def partition(suspect_ratings, threshold):
#     temphead = Node("")
#     end = temphead
#     current = suspect_ratings

#     while current:
#         if current.value > threshold:
#             currNode = Node(current.value, temphead.next)
#             temphead.next = currNode
#         else:
#             currNode = Node(current.value)
#             end.next = currNode
#             end = currNode
#         current = current.next
    
#     return temphead.next
# #Time Complexity: O(n), Space Complexity: O(n)
# suspect_ratings = Node(1, Node(4, Node(3, Node(2, Node(5, Node(2))))))

# print_linked_list(partition(suspect_ratings, 2))

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

# def merge_timelines(known_timeline, witness_timeline):
#     temphead = Node("")
#     curr = temphead
#     one = known_timeline
#     two = witness_timeline

#     while one and two:
#         if one.value < two.value:
#             curr.next = one
#             curr = curr.next
#             one = one.next 
#         else:
#             curr.next = two
#             curr = curr.next
#             two = two.next
    
#     while one:
#         curr.next = one
#         curr = curr.next
#         one = one.next 
    
#     while two:
#         curr.next = two
#         curr = curr.next
#         two = two.next

#     return temphead.next
# #Time: O(n), Space: O(n)

# known_timeline = Node(1, Node(2, Node(4)))
# witness_timeline = Node(1, Node(3, Node(4)))

# print_linked_list(merge_timelines(known_timeline, witness_timeline))

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

# def len(head):
#     len = 0
#     curr = head
#     while curr:
#         len += 1
#         curr = curr.next
    
#     return len

# def rotate(head):
#     curr = head

#     while curr.next.next:
#         curr = curr.next
    
#     new_head = curr.next
#     new_head.next = head
#     curr.next = None 

#     return new_head

# def rotate_right(head, k):
#     if not head or not head.next or k == 0:
#         return head
    
#     length = len(head) #T: O(n)
#     num_rotations = k % length

#     while num_rotations > 0:
#         head = rotate(head) #T: O(n)
#         num_rotations -= 1
    
#     return head
# #T: O(n), Space: O(1)

# evidence_list1 = Node(1, Node(2, Node(3, Node(4, Node(5)))))
# evidence_list2 = Node(0, Node(1, Node(2)))

# print_linked_list(rotate_right(evidence_list1, 2))
# print_linked_list(rotate_right(evidence_list2, 4))

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

# def add_two_numbers(head_a, head_b):
#     temphead = Node("")
#     curr = temphead
#     carry = 0 

#     while head_a and head_b:
#         sum = head_a.value + head_b.value + carry

#         if sum < 10: 
#             new_node = Node(sum)
#             curr.next = new_node
#             curr = curr.next 

#             carry = 0
#         else:
#             carry = sum // 10
#             sum = sum % 10

#             new_node = Node(sum)
#             curr.next = new_node
#             curr = curr.next 
        
#         head_a = head_a.next
#         head_b = head_b.next
    
#     while head_a:
#         sum = head_a.value + carry

#         if sum < 10: 
#             new_node = Node(sum)
#             curr.next = new_node
#             curr = curr.next 

#             carry = 0
#         else:
#             carry = sum // 10
#             sum = sum % 10

#             new_node = Node(sum)
#             curr.next = new_node
#             curr = curr.next 

#         head_a = head_a.next
    
#     while head_b:
#         sum = head_b.value + carry

#         if sum < 10: 
#             new_node = Node(sum)
#             curr.next = new_node
#             curr = curr.next 

#             carry = 0
#         else:
#             carry = sum // 10
#             sum = sum % 10

#             new_node = Node(sum)
#             curr.next = new_node
#             curr = curr.next 

#         head_b = head_b.next
    
#     return temphead.next

# head_a = Node(2, Node(4, Node(3))) # 342
# head_b = Node(5, Node(6, Node(4))) # 465

# print_linked_list(add_two_numbers(head_a, head_b))

# head_a = Node(2, Node(4, Node(3, Node(5)))) # 5342
# head_b = Node(5, Node(6, Node(4))) # 465

# print_linked_list(add_two_numbers(head_a, head_b))

# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next

# def trail_length(trailhead):
#     visited = set()
#     curr = trailhead

#     while curr:
#         curr = curr.next
        
#         if curr not in visited:
#             visited.add(curr)
#         else:
#             break
    
#     return len(visited)
# #Time: O(n), Space: O(n)

# marker1 = Node("Marker 1")
# marker2 = Node("Marker 2")
# marker3 = Node("Marker 3")
# marker1.next = marker2
# marker2.next = marker3
# marker3.next = marker1

# print(trail_length(marker1))

# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next

# # For testing - careful this will cause an infinite loop when used on a list w/cycles
# def print_linked_list(head):
#     current = head
#     while current:
#         print(current.value, end=" -> " if current.next else "\n")
#         current = current.next

# def clear_trail(trailhead):
#     #Edge Cases
#     if not trailhead or not trailhead.next:
#         return trailhead
    
#     #Generic Case
#     prev = trailhead
#     visited = set()
#     visited.add(prev)
#     curr = trailhead.next

#     while curr:
#         if curr in visited:
#             break
#         else:
#             visited.add(curr)
        
#         prev = curr
#         curr = curr.next
    
#     prev.next = None
#     return trailhead

# marker1 = Node("Trailhead")
# marker2 = Node("Trail Fork")
# marker3 = Node("The Falls")
# marker4 = Node("Peak")
# marker1.next = marker2
# marker2.next = marker3
# marker3.next = marker4
# marker4.next = marker2

# print_linked_list(clear_trail(marker1))
# #time: O(n), space: O(n)

    
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

# def remove_duplicate_markers(trailhead):
#     if not trailhead or not trailhead.next:
#         return trailhead
    
#     curr = trailhead

#     while curr.next:
#         if curr.value == curr.next.value: 
#             curr.next = curr.next.next 
#         else:
#             curr = curr.next 
    
#     return trailhead

# trailhead = Node(1, Node(1, Node(1, Node(1, Node(1, Node(1, Node(1, Node(1))))))))

# print_linked_list(remove_duplicate_markers(trailhead))

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

def selective_trail_clearing(trailhead, m, n):
    temphead = Node("", trailhead)
    
    previous = curr = trailhead

    while curr:
        for _ in range(m):
            if curr:
                previous = curr
                curr = curr.next
            else:
                break
        
        for _ in range(n):
            if curr:
                curr = curr.next
            else:
                break 
        
        previous.next = curr

    return temphead.next

trailhead = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7, Node(8, Node(9, Node(10, Node(11, Node(12, Node(13)))))))))))))

print_linked_list(selective_trail_clearing(trailhead, 2, 3))


def locate_cache(cache_labels):
    length = len(cache_labels) - 1

    val = 0
    curr = cache_labels

    while curr:
        val += (2 ** length) * curr.value

        length -= 1
        curr = curr.next
    
    return val


def len(head):
    length = 0
    curr = head
    while curr:
        length += 1
        curr = curr.next
    
    return length

cache_labels = Node(1, Node(0, Node(0, Node(0, Node(1, Node(0)))))) # 101 base 2

print(locate_cache(cache_labels))

def merge_trail(trailhead):
    temphead = Node("")
    end = temphead

    curr = trailhead.next
    
    val = 0
    while curr:
        if curr.value == 0:
            end.next = Node(val)
            end = end.next
            val = 0
        else:
            val += curr.value
        
        curr = curr.next
    
    return temphead.next

trail1 = Node(0, Node(3, Node(1, Node(0, Node(4, Node(5, Node(4, Node(2, Node(0)))))))))
trail2 = Node(0, Node(1, Node(0, Node(3, Node(0, Node(2, Node(2, Node(0))))))))

print_linked_list(merge_trail(trail1))
print_linked_list(merge_trail(trail2))