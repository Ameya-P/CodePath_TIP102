# cereals = ['cheerios', 'fruity pebbles', 'cocoa puffs']

# for index, cereal in enumerate(cereals):
#     print(index, cereal)


# def reverse_sentence(sentence):
#     s_array = sentence.split()
#     new_s = []
    
#     for word in s_array:
#         new_s.insert(0, word)
    
#     print(" ".join(new_s))


# sentence = "tubby little cubby all stuffed with fluff"
# reverse_sentence(sentence)

# sentence = "Pooh"
# reverse_sentence(sentence)

# def goldilocks_approved(nums):
#     min_val = min(nums)
#     max_val = max(nums)

#     for num in nums:
#         if num != min_val and num != max_val:
#             return num
    
#     return -1

# nums = [3, 2, 1, 4]
# print(goldilocks_approved(nums))

# nums = [1, 2]
# print(goldilocks_approved(nums))

# nums = [2, 1, 3]
# print(goldilocks_approved(nums))

# def delete_minimum_elements(hunny_jar_sizes):
#     hunny_jar_sizes.sort()

#     new_jars = []

#     while len(hunny_jar_sizes) > 0:
#         new_jars.append(hunny_jar_sizes.pop(0))
    
#     print(new_jars)


# hunny_jar_sizes = [5, 3, 2, 4, 1]
# delete_minimum_elements(hunny_jar_sizes)

# hunny_jar_sizes = [5, 2, 1, 8, 2]
# delete_minimum_elements(hunny_jar_sizes)


# def sum_of_digits(num):
#     integers = []
#     while num > 0:
#         integer = num % 10
#         num = num // 10
#         integers.append(integer)
    
#     print(sum(integers))


# num = 423
# sum_of_digits(num)

# num = 4
# sum_of_digits(num)

# def final_value_after_operations(operations):
#     tigger = 1

#     for operation in operations:
#         if operation == "bouncy" or operation == "flouncy":
#             tigger += 1
#         elif operation == "trouncy" or operation == "pouncy":
#             tigger -= 1
    
#     print(tigger)

# operations = ["trouncy", "flouncy", "flouncy"]
# final_value_after_operations(operations)

# operations = ["bouncy", "bouncy", "flouncy"]
# final_value_after_operations(operations)

# def is_acronym(words, s):
#     first_letter = []
#     for word in words:
#         first_letter.append(word[0])
    
#     return "".join(first_letter) == s

# words = ["christopher", "robin", "milne", "pee"]
# s = "crmp"
# print(is_acronym(words, s))

# names = ['Alice', 'Bob', 'Charlie', "Pee"]
# ages = [25, 30, 35]

# zipper = zip(names,ages)
# print(list(zipper))

# def make_divisible_by_3(nums):
#     ops = 0
#     for num in nums:
#         if num % 3 != 0:
#             ops += 1

    
#     print(ops)

# nums = [1, 2, 3, 4]
# make_divisible_by_3(nums)

# nums = []
# make_divisible_by_3(nums)

# def exclusive_elemts(lst1, lst2):
#     exclusive = []

#     for item in lst1:
#         if item not in lst2:
#             exclusive.append(item)
    
#     for item in lst2:
#         if item not in lst1:
#             exclusive.append(item)
    
#     print(exclusive)

# lst1 = ["pooh", "roo", "piglet"]
# lst2 = ["piglet", "eeyore", "owl"]
# exclusive_elemts(lst1, lst2)

# lst1 = ["pooh", "roo"]
# lst2 = ["piglet", "eeyore", "owl", "kanga"]
# exclusive_elemts(lst1, lst2)

# lst1 = ["pooh", "roo", "piglet"]
# lst2 = []
# exclusive_elemts(lst1, lst2)

# def merge_alternately(word1, word2):
#     merged = ""
#     pointer = 0
#     while pointer < min(len(word1), len(word2)):
#         merged += word1[pointer]
#         merged += word2[pointer]
#         pointer += 1
    
#     if len(word1) < len(word2):
#         merged += word2[pointer:]
#     else:
#         merged += word1[pointer:]
    
#     print(merged)

# word1 = ""
# word2 = ""
# merge_alternately(word1, word2)

# word1 = "hfa"
# word2 = "eflump"
# merge_alternately(word1, word2)

# word1 = "eyre"
# word2 = "eo"
# merge_alternately(word1, word2)

# def good_pairs(pile1, pile2, k):
#     num_pairs = 0

#     for stick in pile1:
#         for stick2 in pile2:
#             if stick % (stick2 * k) == 0:
#                 num_pairs += 1

#     print(num_pairs)

# pile1 = [1, 3, 4]
# pile2 = [1, 3, 4]
# k = 1
# good_pairs(pile1, pile2, k)

# pile1 = [1, 2, 4, 12]
# pile2 = [2, 4]
# k = 3
# good_pairs(pile1, pile2, k)

# def are_equivalent(word1, word2):
#     print("".join(word1) == "".join(word2))

# word1 = ["bat", "man"]
# word2 = ["b", "atman"]
# are_equivalent(word1, word2)

# word1 = ["alfred", "pennyworth"]
# word2 = ["alfredpenny", "word"]
# are_equivalent(word1, word2)

# word1  = ["cat", "wom", "an"]
# word2 = ["catwoman"]
# are_equivalent(word1, word2)

# def count_evens(lst):
#     num_even = 0
#     for word in lst:
#         if len(word) % 2 == 0:
#             num_even += 1
    
#     print(num_even)

# lst = ["na", "nana", "nanana", "batman", "!"]
# count_evens(lst)

# lst = ["the", "joker", "robin"]
# count_evens(lst)

# lst = ["you", "either", "die", "a", "hero", "or", "you", "live", "long", "enough", "to", "see", "yourself", "become", "the", "villain"]
# count_evens(lst)

# def remove_name(people, secret_identity):
#     i = len(people) - 1
#     while i >= 0:
#         if people[i] == secret_identity:
#             people.pop(i)
#         i -= 1
#     print(people)

# people = ['Bruce Wayne','Batman', 'Superman', 'Bruce Wayne', 'The Riddler', 'Bruce Wayne', 'Bruce Wayne']
# secret_identity = 'Bruce Wayne'
# remove_name(people, secret_identity)

# def count_digits(n):
#     num_digits = 1
#     while n > 10:
#         n = n // 10 #0
#         num_digits += 1
    
#     print(num_digits)

# n = 98649864
# count_digits(n)

# n = 0
# count_digits(n)

# def move_zeroes(lst):
#     new_list = []
#     num_zeros = 0
#     for num in lst:
#         if num != 0:
#             new_list.append(num)
#         else:
#             num_zeros += 1
    
#     while num_zeros > 0:
#         new_list.append(0)
#         num_zeros -= 1
    
#     print(new_list)

# lst = [4, 3, 2]
# move_zeroes(lst)

# def reverse_vowels(s):
#     vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
#     beginning = 0
#     end = len(s) - 1
#     s = list(s)
#     #Turn string into list
#     #Have two pointers, one that points to the beginning and another that points to the end
#     #Check if there is a vowel in at each pointer's current location 
#     #If there is a vowel at both locations, switch the vowels and move the pointers
#     #If there is a a vowel at one location and not the other, increment the pointer that doesn't have a vowel
#     #Keep doing this until pointers pass each other
#     while beginning < end:
#         if s[beginning] in vowels:
#             if s[end] in vowels:
#                 temp = s[beginning]
#                 s[beginning] = s[end]
#                 s[end] = temp
                
#                 beginning += 1
            
#             end -= 1
#         else:
#             beginning += 1

#             if s[end] not in vowels:
#                 end -= 1

#     print("".join(s))
    

# s = ""
# reverse_vowels(s)

# s = "BATgirl"
# reverse_vowels(s)

# s = "batman"
# reverse_vowels(s)

# def highest_altitude(gain):
#     max = 0
#     current = 0
#     for point in gain:
#         current += point
#         if current > max:
#             max = current
    
#     print(max)

# gain = [-5, 1, 5, 0, -7, 10]
# highest_altitude(gain)

# gain = [-4, -3, -2, -1, 4, 3, 2]
# highest_altitude(gain)

# def left_right_difference(nums):
#     i = 1
#     r_sum = sum(nums) - nums[0]
#     l_sum = 0
#     answer = []
#     while i < len(nums):
#         answer.append(r_sum - l_sum)
#         r_sum -= nums[i]
#         l_sum += nums[i-1]
#         i += 1
#     answer.append(r_sum - l_sum)
#     print(answer)

# nums = [10, 4, 8, 3]
# left_right_difference(nums)

# nums = [1, 2, 3, 4, 5]
# left_right_difference(nums)

# def common_elements(lst1, lst2):
#     common = []
#     for item1 in lst1:
#         for item2 in lst2:
#             if item1 == item2 and item1 not in common:
#                 common.append(item1)
    
#     print(common)


# lst1 = ["super strength", "super speed", "x-ray vision"]
# lst2 = ["super speed", "time travel", "dimensional travel"]
# common_elements(lst1, lst2)

# lst1 = ["super strength", "super strength", "super speed", "x-ray vision"]
# lst2 = ["martial arts", "stealth", "master detective", "super strength", "super strength"]
# common_elements(lst1, lst2)

# def expose_superman(trust, n):
#     superman = -1

#     #Create an array of integers, size = number of citizens
#     num_trusts_x = [0] * (n+1)
#     #Create an array of booleans, representing if a citizen trusts at least one person (Trust = True)
#     x_trusts = [False] * (n+1)
#     #Go through trust array. Add 1 to "b" to represent that "a" trusts them. Add true to "a" in the boolean array
#     for relationship in trust:
#         x_trusts[relationship[0]] = True
#         num_trusts_x[relationship[1]] += 1
    

#     #Iterate through array of ints, see if there's a citizen who's trusted by everyone. If so, check the boolean array to see if they trust anyone. If they don't. That's superman. Return n
#     for i in range(1, n+1):
#         if num_trusts_x[i] == n - 1:
#             if x_trusts[i] == False:
#                 superman = i

#     print(superman)
    
# n = 2
# trust = [[1, 2]]
# expose_superman(trust, n)

# n = 3
# trust = [[1, 3], [2, 3]]
# expose_superman(trust, n)

# n = 1
# trust = []
# expose_superman(trust, n)

# def add_matrices(matrix1, matrix2):
#     sum_matrix = []

#     n = len(matrix1)
#     m = len(matrix1[0])

#     for i in range(n):
#         row = []
#         for j in range(m):
#             sum = matrix1[i][j] + matrix2[i][j]
#             row.append(sum)
        
#         sum_matrix.append(row)

#     print(sum_matrix)

# matrix1 = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# matrix2 = [
#     [9, 8, 7],
#     [6, 5, 4],
#     [3, 2, 1]
# ]

# add_matrices(matrix1, matrix2)

# def is_palindrome(s):
#     beginning = 0
#     end = len(s) - 1
    
#     while beginning < end:
#         if s[beginning] != s[end]:
#             return False
        
#         beginning += 1
#         end -= 1

#     return True

# s = "palindrome"
# print(is_palindrome(s))

# s = "racecar"
# print(is_palindrome(s))

# def squash_spaces(s):
#     ns = ""
#     first = 0
#     second = 1

#     while second <= len(s):
#         if s[first] != ' ':
#             ns += s[first]
#         elif second < len(s) and s[second] != ' ':
#             ns += s[first]

#         first += 1
#         second += 1
    
#     print(ns)




# s = "   Up,     up,   and  away!                   "
# squash_spaces(s)

# s = "With great power comes great responsibility."
# squash_spaces(s)



# def two_sum_wrong(nums, target):
#     first = 0
#     second = 1
#     while first < len(nums) - 1:
#         current_sum = nums[first] + nums[second]

#         if current_sum == target:
#             return [first, second]
        
#         if second < len(nums) - 1:
#             second += 1
#         else:
#             first += 1
#             second = first + 1
    
#     return "no solution"

# def two_sum(num, target):
#     left = 0
#     right = len(num) - 1

#     while left < right:
#         sum = num[left] + num[right]
#         if sum == target:
#             return [left, right]
#         elif sum < target:
#             left += 1
#         else:
#             right -= 1

# nums = [2, 7, 11, 15]
# target = 17
# print(two_sum(nums, target))

# nums = [2, 7, 11, 15]
# target = 22
# print(two_sum(nums, target))

# def three_sum(nums):
#     nums.sort()
#     result = []
    
#     for i in range(len(nums) - 2):
#         if i > 0 and nums[i] == nums[i - 1]:  # Skip duplicate values for i
#             continue
#         left, right = i + 1, len(nums) - 1
        
#         while left < right:
#             total = nums[i] + nums[left] + nums[right]
#             if total == 0:
#                 result.append([nums[i], nums[left], nums[right]])
#                 while left < right and nums[left] == nums[left + 1]:  # Skip duplicates for left
#                     left += 1
#                 while left < right and nums[right] == nums[right - 1]:  # Skip duplicates for right
#                     right -= 1
#                 left += 1
#                 right -= 1
#             elif total < 0:
#                 left += 1
#             else:
#                 right -= 1
    
#     print(result)
            

# nums = [-1, 0, 1, 2, -1, -4]
# three_sum(nums)

# nums = [0, 1, 1]
# three_sum(nums)

# nums = [0, 0, 0]
# three_sum(nums)


# def insert_interval(intervals, new_interval):
#     merged = []
#     i = 0
#     n = len(intervals)

#     #Add all intervals
#     while i < n and intervals[i][1] < new_interval[0]:
#         merged.append(intervals[i])
#         i += 1
    
#     #Merge intervals
#     while i < n and intervals[i][0] <= new_interval[1]:
#         new_interval[0] = min(intervals[i][0], new_interval[0])
#         new_interval[0] = max(intervals[i][1], new_interval[1])
#         i += 1
    
#     merged.append(new_interval)

#     while i < n:
#         merged.append(intervals[i])
#         i += 1
    
#     print(merged)

#     print("----------")
#     intervals = [[1, 3], [6, 9]]
#     new_interval = [2, 5]
#     insert_interval(intervals, new_interval)

#     intervals = []
#     new_interval = [5, 7]
#     insert_interval(intervals, new_interval)

# def transpose(matrix):
#     n = len(matrix)
#     m = len(matrix[0])
#     new_matrix = [[0 for x in range(n)] for y in range(m)]

#     for i in range(n):
#         for j in range(m):
#             new_matrix[j][i] = matrix[i][j]
        
#     print(new_matrix)
    
# matrix = [
#         [1, 2, 3],
#         [4, 5, 6],
#         [7, 8, 9]
#     ]
# transpose(matrix)

# matrix = [
#         [1, 2, 3],
#         [4, 5, 6]
#     ]
# transpose(matrix)

# def reverse_list(lst):
#     left = 0
#     right = len(lst) - 1

#     while left < right:
#         lst[right], lst[left] = lst[left], lst[right]
#         left += 1
#         right -= 1
    
#     print(lst)

# lst = ["pooh", "christopher robin", "piglet", "roo", "eeyore"]
# reverse_list(lst)

# def remove_dupes(items):
#     first = 0
#     second = 1

#     while second < len(items):
#         if items[first] == items[second]:
#             items.pop(second)
#         else:
#             first += 1
#             second += 1
    
#     return len(items)

# items = ["extract of malt", "extract of malt", "extract of malt", "haycorns", "haycorns", "honey", "thistle", "thistle"]
# print(remove_dupes(items))
# print(items)

# items = []
# print(remove_dupes(items))
# print(items)

# def sort_by_parity(nums):
#     left = 0
#     right = len(nums) - 1

#     while left < right:
#         if nums[left] % 2 != 0 and nums[right] % 2 == 0:
#             nums[left], nums[right] = nums[right], nums[left]
        
#         if nums[left] % 2 == 0:
#             left += 1
        
#         if nums[right] % 2 != 0:
#             right -= 1
    
#     print(nums)
        

# nums = [6, 4, 2]
# sort_by_parity(nums)

# nums = [1, 3, 5]
# sort_by_parity(nums)

def most_honey(height):
    max_honey = 0
    left = 0
    right = len(height) - 1

    while left < right:
        width = right - left
        current_height = min([height[left], height[right]])
        current_area = width * current_height
         
        max_honey = max(max_honey, current_area)
        
        if height[left] < height[right]:
            left += 1
        else: 
            right -= 1
    
    print(max_honey)
        

height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
most_honey(height)

height = [1, 1]
most_honey(height)

def merge_intervals(intervals):
    if len(intervals) == 0:
        return intervals
    
    intervals.sort(key = lambda interval: interval[0])

    merged = []
    i = 1
    n = len(intervals)
    prev = intervals[0]

    while i < n:
        current = intervals[i]
        if prev[1] < current[0]:
            merged.append(prev)
            prev = current
        else:
            prev[0] = min(prev[0], current[0])
            prev[1] = max(prev[1], current[1])

        i += 1

    merged.append(prev)
    print(merged)

intervals = [[1, 3], [2, 6], [8, 10], [7, 16], [15, 18]]
merge_intervals(intervals)

intervals = []
merge_intervals(intervals)