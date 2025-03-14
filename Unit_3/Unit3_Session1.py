# def minimum_average_view_count(view_counts):
#     left = 0
#     right = len(view_counts) - 1

#     average_views = []
#     view_counts.sort()

#     while left < right:
#         min = view_counts[left]
#         max = view_counts[right]
#         average_views.append((min + max)/2)
#         left += 1
#         right -= 1
    
#     average_views.sort()
#     return average_views[0]

# print(minimum_average_view_count([7, 8, 3, 4, 15, 13, 4, 1])) 
# print(minimum_average_view_count([1, 9, 8, 3, 10, 5])) 
# print(minimum_average_view_count([1, 2, 3, 7, 8, 9])) 

# def min_remaining_watchlist(watchlist):
#     stack = []

#     for character in watchlist:
#         #If character = B, check if A is on stack (if you pop)
#         #If D, check if C is on stack
#         if character == 'B':
#             top = stack.pop() 
#             if top != 'A':
#                 stack.append(top)
#                 stack.append(character)
#         elif character == 'D':
#             top = stack.pop() 
#             if top != 'C':
#                 stack.append(top)
#                 stack.append(character)
#         else:
#             stack.append(character)
    
#     return len(stack)
    
# print(min_remaining_watchlist("ABFCACDB")) 
# print(min_remaining_watchlist("ACBBD")) 

# a = [1,0,2,0,0,1]
# sorted(a, key = lambda a: 1 if a ==0 else -1)
# print(sorted(a, key = lambda a: 1 if a ==0 else -1))

# def is_valid_post_format(posts):
#     stack = []
#     tag_dict = {'(':')', '{':'}', '[':']'}

#     for tag in posts:
#         if tag in tag_dict:
#             stack.append(tag)
#         else:
#             if len(stack) > 0:
#                 opening_tag = stack.pop()
#             else:
#                 return False
            
#             closing_tag = tag_dict[opening_tag]
#             if closing_tag != tag:
#                 return False
    
#     return len(stack) == 0

# print(is_valid_post_format("()"))
# print(is_valid_post_format("()[]{}")) 
# print(is_valid_post_format("(]"))
# print(is_valid_post_format(""))

from collections import deque


def reverse_comments_queue(comments):
    stack = []
    for comment in comments:
        stack.append(comment)
    
    reversed = []
    while stack:
        reversed.append(stack.pop())
    
    return reversed

print(reverse_comments_queue(["Great post!", "Love it!", "Thanks for sharing."]))

print(reverse_comments_queue(["First!", "Interesting read.", "Well written."]))

def is_symmetrical_title(title):
    left = 0
    right = len(title) - 1

    while left < right:
        while not str(title[left]).isalpha():
            left += 1
        
        while not str(title[right]).isalpha():
            right -= 1

        if title[left].lower() == title[right].lower():
            left += 1
            right -= 1
        else:
            return False
    
    return True

print(is_symmetrical_title("A Santa at NASA"))
print(is_symmetrical_title("Social Media")) 

print(is_symmetrical_title("ABA")) 

def engagement_boost(engagements):
    results = [0] * len(engagements)
    left = 0
    right = len(engagements) - 1
    pos = len(engagements) - 1

    while left <= right:
        left_val = engagements[left]
        right_val = engagements[right]

        if left == right:
            results[pos] = left_val**2
            pos -= 1
            left += 1
            right -= 1
        elif abs(left_val) > abs(right_val):
            results[pos] = left_val**2
            pos -= 1
            left += 1
        else:
            results[pos] = right_val**2
            pos -= 1
            right -= 1
    
    return results


print(engagement_boost([-4, -1, 0, 3, 10]))
print(engagement_boost([-7, -3, 2, 3, 11]))

def clean_post(post):
    #Two pointer approach
    #Keep iterating over the string until I've removed all duplicates. If I hit a duplicate, remove it and reset the pointers to the beginning of the string
    post = list(post)
    first = 0
    second = 1

    while second < len(post):
        first_letter = post[first]
        second_letter = post[second]

        if (first_letter.isupper() and second_letter.islower()) or (second_letter.isupper() and first_letter.islower()):
            if first_letter.lower() == second_letter.lower():
                post.pop(second)
                post.pop(first)
                first = 0
                second = 1
            else:
                first += 1
                second += 1
        else:
            first += 1
            second += 1
    
    return "".join(post)

def clean_post(post):
    #Stack approach
    stack = []

    for current_char in post:
        if stack:
            previous_char = stack[-1]

            if (previous_char.isupper() and current_char.islower()) or (previous_char.islower() and current_char.isupper()):
                if previous_char.lower() == current_char.lower():
                    stack.pop()
                    continue
        
        stack.append(current_char)
    
    return "".join(stack)

print(clean_post("poOost")) 
print(clean_post("abBAcC")) 
print(clean_post("s")) 

# def edit_post(post):
#     results = []
#     post = post.split()

#     for word in post:
#         word = deque(word)
#         reversed = ''
#         while word:
#             reversed += word.pop()
        
#         results.append(reversed)

#     return " ".join(results)

def edit_post(post):
    queue = deque()
    results = []
    for char in post:
        if char.isalpha():
            queue.append(char)
        else:
            reversed = ''
            while queue:
                reversed += queue.pop()
            
            results.append(reversed)

    reversed = ''
    while queue:
        reversed += queue.pop()
            
    results.append(reversed)

    return " ".join(results)

print(edit_post("Boost your engagement with these tips ")) 
print(edit_post("Check out my latest vlog")) 

def post_compare(draft1, draft2):
    final1 = deleter(draft1)
    final2 = deleter(draft2)

    return final1 == final2

def deleter(draft):
    stack = []

    for char in draft:
        if char == '#':
            if stack:
                stack.pop()
        else:
            stack.append(char)

    return stack

print(post_compare("", "ad#c"))
print(post_compare("ab##", "c#d#")) 
print(post_compare("a#c", "b")) 