# def binary_search(lst, value):
#     left = 0
#     right = len(lst) - 1
#     middle = len(lst) // 2

#     while left <= right:
#         if value == lst[middle]:
#             return middle
#         elif value < lst[middle]:
#             right = middle - 1
#         elif value > lst[middle]:
#             left = middle + 1
        
#         middle = left + right // 2
    
#     return -1


# def binary_search_r(lst, value):
#     return bs_recur(lst, value, 0, len(lst) - 1)

# def bs_recur(lst, value, left, right):
#     if left > right:
#         return - 1
    
#     middle = (left + right) // 2

#     if value == lst[middle]:
#         return middle
#     elif value < lst[middle]:
#         right = middle - 1
#         return bs_recur(lst, value, left, right)
#     elif value > lst[middle]:
#         left = middle + 1
#         return bs_recur(lst, value, left, right)

        
# lst = [0,1,2,3,5,5,6,7]
# value = 5
# print(binary_search(lst,value))
# print(binary_search_r(lst,value))



# def find_cruise_length(cruise_lengths, vacation_length):
#     left = 0
#     right = len(cruise_lengths) - 1

#     while left <= right:
#         middle = (left + right) // 2

#         if cruise_lengths[middle] == vacation_length:
#             return True
#         elif vacation_length < cruise_lengths[middle]:
#             right = middle - 1
#         else:
#             left = middle + 1
        
#     return False

# print(find_cruise_length([9, 10, 11, 12, 13, 14, 15], 13))

# print(find_cruise_length([8, 9, 12, 13, 13, 14, 15], 11))

# def find_cabin_index(cabins, preferred_deck):
#     return binary_search(cabins, preferred_deck, 0, len(cabins) - 1)

# def binary_search(cabins, preferred_deck, left, right):
#     if left > right:
#         return left
    
#     middle = (left + right) // 2

#     if cabins[middle] == preferred_deck:
#         return middle
#     elif preferred_deck < cabins[middle]:
#         right = middle - 1
#         return binary_search(cabins, preferred_deck, left, right)
#     else:
#         left = middle + 1
#         return binary_search(cabins, preferred_deck, left, right)
    
# print(find_cabin_index([1, 3, 5, 6], 5))
# print(find_cabin_index([1, 3, 5, 6], 2))
# print(find_cabin_index([1, 3, 5, 6], 7))



# def count_checked_in_passengers(rooms):
#     if not rooms:
#         return 0
    
#     if len(rooms) == 1:
#         return rooms[0]
    
#     middle = len(rooms) // 2
#     return count_checked_in_passengers(rooms[:middle]) + count_checked_in_passengers(rooms[middle:])
        


# rooms1 = [0, 0, 0, 1, 1, 1, 1]
# rooms2 = [0, 0, 0, 0, 0, 1]
# rooms3 = [0, 0, 0, 0, 0, 0]

# print(count_checked_in_passengers(rooms1)) 
# print(count_checked_in_passengers(rooms2))
# print(count_checked_in_passengers(rooms3))

""" def is_profitable(excursion_counts):
    left = 0
    right = len(excursion_counts) - 1

    #value of x should equal length of list - it's index 
    
    while left <= right:
        middle = (left + right) // 2
        x =countns tmiddlest x passengers signed up
        count = 0
middle>x        if excursioxunts[middle] == vacation_length:
            return True
        elif count < middle:
            right = middle - 1
        else:
           -1 = middle + 1
        
    return False
     

print(is_profitable([3, 5]))
print(is_profitable([0, 0])) """

#     x = excursion_counts[0]

#     if x < len(excursion_counts):
#         return - 1
    
#     if x == len(excursion_counts):
#         return x
    
#     if x > len(excursion_counts):
#         return len(excursion_counts)

# #Take a look at the first element, X is not going to be greater than that
# #Keep a count of every item that is greater than or equal to X
# #if count == x, then return count 
# #if count != x, then return -1 

# #Everything in the list is greater than or equal to the first element
# #length of list = num items that are greater/equal to first element
# #if x < len(list) --> return -1 

#  x = excursion_counts[-1]
#     counts = 0
    
#     index = len(excursion_counts) - 1
#     while index >= 0:
#         if x <= excursion_counts[index]:
#             counts += 1
#             index -= 1
#         else:
#             if x == counts:
#                 return x 
            
#             x -= 1
    
#     if x > counts:
#         return counts
    
#     return -1

# def find_perfect_song(playlist, length):
#     return helper(playlist, 0, len(playlist)-1, length)

# def helper(playlist, left, right, length):
#     if left > right:
#         return -1
    
#     middle = left + right // 2
#     if playlist[middle] == length:
#         return middle
#     elif playlist[middle] < length:
#         return helper(playlist, left, middle-1, length)
#     elif playlist[middle] > length:
#         return helper(playlist, middle+1, right, length)

# print(find_perfect_song([101, 102, 103, 104, 105], 103))
# print(find_perfect_song([201, 202, 203, 204, 205], 206))

# def is_profitable(excursion_counts):
#     n = len(excursion_counts)
#     left = 0
#     right = n - 1
#     while left <= right:
#         mid = (left + right) // 2
#         x = n - mid

#         if excursion_counts[mid] >= x:
#             if mid == 0 or excursion_counts[mid-1] < x:
#                 return x
#             right = mid - 1
#         elif excursion_counts[mid] < x:
#             left = mid + 1
    
#     return - 1

# print(is_profitable([3, 5]))
# print(is_profitable([0, 0]))

def mergesort(lst):
    if not lst or len(lst) == 1:
        return lst
    
    middle = len(lst) // 2
    lst1 = mergesort(lst[:middle])
    lst2 = mergesort(lst[middle:])

    one = 0
    two = 0

    new_lst = []
    
    while one < len(lst1) and two < len(lst2):
        if lst1[one] < lst2[two]:
            new_lst.append(lst1[one])
            one += 1
        else:
            new_lst.append(lst2[two])
            two += 1
    
    while one < len(lst1):
        new_lst.append(lst1[one])
        one += 1
    
    while two < len(lst2):
        new_lst.append(lst2[two])
        two += 1
    
    return new_lst

unsorted = [0, 4, 2, 3, 9, 1, 5, 7, 8, 6]

print(mergesort(unsorted))