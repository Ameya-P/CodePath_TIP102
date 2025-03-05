def minimum_average_view_count(view_counts):
    left = 0
    right = len(view_counts) - 1

    average_views = []
    view_counts.sort()

    while left < right:
        min = view_counts[left]
        max = view_counts[right]
        average_views.append((min + max)/2)
        left += 1
        right -= 1
    
    average_views.sort()
    return average_views[0]

print(minimum_average_view_count([7, 8, 3, 4, 15, 13, 4, 1])) 
print(minimum_average_view_count([1, 9, 8, 3, 10, 5])) 
print(minimum_average_view_count([1, 2, 3, 7, 8, 9])) 

def min_remaining_watchlist(watchlist):
    stack = []

    for character in watchlist:
        #If character = B, check if A is on stack (if you pop)
        #If D, check if C is on stack
        if character == 'B':
            top = stack.pop() 
            if top != 'A':
                stack.append(top)
                stack.append(character)
        elif character == 'D':
            top = stack.pop() 
            if top != 'C':
                stack.append(top)
                stack.append(character)
        else:
            stack.append(character)
    
    return len(stack)
    
print(min_remaining_watchlist("ABFCACDB")) 
print(min_remaining_watchlist("ACBBD")) 

a = [1,0,2,0,0,1]
sorted(a, key = lambda a: 1 if a ==0 else -1)
print(sorted(a, key = lambda a: 1 if a ==0 else -1))