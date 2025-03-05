def locate_thistles(items):
    indices = []
    for i in range(len(items)):
        if items[i] == "thistle":
            indices.append(i)
    
    return indices

items = ["book", "bouncy ball", "leaf", "red balloon"]
#print(locate_thistles(items))

def batman():
    print("I am vengeance. I am the night. I am Batman!")

#batman()

def madlib(verb):
    print(f"I have one power. I never {verb}. - Batman")

verb = "give up"
#madlib(verb)

verb = "nap"
#madlib(verb)

def trilogy(year):
    if year == 2005:
        print("Batman Begins")
    elif year == 2008:
        print("The Dark Knight")
    elif year == 2012:
        print("The Dark Knight Rises")
    else:
        print(f"Christopher Nolan did not release a Batman movie in {year}.")
    
year = 2008
#trilogy(year)

year = 1998
#trilogy(year)

def get_last(items):
    if len(items) == 0:
        return None
    else:
        return items[len(items) - 1]

items = ["spider man", "batman", "superman", "iron man", "wonder woman", "black adam"]
#print(get_last(items))

items = []
#print(get_last(items))

def concatenate(words):
    result = ""
    for word in words:
        result += word
    
    return result

words = ["vengeance", "darkness", "batman"]
#print(concatenate(words))

words = []
#print(concatenate(words))

def squared(numbers):
    squared = []
    for num in numbers:
        squared.append(num * num)
    return squared

numbers = [1, 2, 3]
#print(squared(numbers))

def find_villain(crowd, villain):
    indices = []
    for i in range(len(crowd)):
        if crowd[i] == villain:
            indices.append(i)
    return indices

crowd = ['Batman', 'The Joker', 'Alfred Pennyworth', 'Robin', 'The Joker', 'Catwoman', 'The Joker']
villain = 'The Joker'
#print(find_villain(crowd, villain))

def get_odds(nums):
    odds = []
    for num in nums:
        if num % 2 != 0:
            odds.append(num)
    return odds

nums = [1, 2, 3, 4]
#print(get_odds(nums))

nums = [2, 4, 6, 8]
#print(get_odds(nums))

def up_and_down(lst):
    num_odds = 0
    num_evens = 0
    for num in lst:
        if num % 2 == 0:
            num_evens += 1
        else:
            num_odds += 1
    return num_odds - num_evens

lst = [1, 2, 3]
print(up_and_down(lst))

lst = [1, 3, 5]
print(up_and_down(lst))

lst = [2, 4, 10, 2]
print(up_and_down(lst))


def running_sum(superhero_stats):
    running = 0
    for i in range(len(superhero_stats)):
        running += superhero_stats[i]
        superhero_stats[i] = running
    print(superhero_stats)

superhero_stats = [1, 2, 3, 4]
running_sum(superhero_stats)

superhero_stats = [1, 1, 1, 1, 1]
running_sum(superhero_stats)

superhero_stats = [3, 1, 2, 10, 1]
running_sum(superhero_stats)

def shuffle(cards):
    x = 0
    y = int(len(cards) / 2)
    
    new_list = []

    while y < len(cards):
        new_list.append(cards[x])
        new_list.append(cards[y])
        x += 1
        y += 1
    
    print(new_list)

cards = ['Joker', 'Queen', 2, 3, 'Ace', 7]
shuffle(cards)

cards = [9, 2, 3, 'Joker', 'Joker', 3, 2, 9]
shuffle(cards)

cards = [10, 10, 2, 2]
shuffle(cards)

def linear_search(lst, target):
    location = - 1

    for i in range(len(lst)):
        if lst[i] == target:
            location = i

    print(location)

items = ['haycorn', 'haycorn', 'haycorn', 'hunny', 'haycorn']
target = 'hunny'
linear_search(items, target)

items = ['bed', 'blue jacket', 'red shirt', 'hunny']
target = 'red balloon'
linear_search(items, target)

def tiggerfy(word):
    word = word.lower()
    tigger = ["t", "i", "gg", "er"]
    for substring in tigger:
        word = word.replace(substring, "")
    print(word)


word = "Trigger"
tiggerfy(word)

word = "eggplant"
tiggerfy(word)

word = "choir"
tiggerfy(word)

def non_decreasing(nums):
    decreasing = 0
    first = 0
    second = 1

    x = 0
    y = 1
    while second < len(nums):
        if nums[first] > nums[second]:
            decreasing += 1
            x = first
            y = second
        first += 1
        second += 1
    
    if decreasing > 1:
        return False
    elif decreasing == 0:
        return True
    else: 
        modifiable = False
        if x - 1 >= 0:
            if nums[x-1] < nums[y]: 
                modifiable = True
        else: 
            modifiable = True
        
        if y + 1 < len(nums):
            if nums[y+1] > nums[x]:
                modifiable = True
        else: 
            modifiable = True
        
        return modifiable



nums = [3, 4, 2, 3]
print(non_decreasing(nums))

nums = [1, 2, 3]
print(non_decreasing(nums))

def find_missing_clues(clues, lower, upper):
    #Create an empty range list
    ranges = []
    missing_values = []
    #Have a current value 
    current_val = lower 
    i = 0
    #Iterate through the clues array
    while current_val < upper + 1:
        while i < len(clues) and clues[i] != current_val:
            missing_values.append(current_val)
            current_val += 1
        
        if i >= len(clues):
            missing_values.append(current_val)
            missing_values.append(upper)
            current_val = upper


        
        if (len(missing_values) >= 1):
            ranges.append([missing_values[0], missing_values[len(missing_values) - 1]])
            missing_values = []
        i += 1
        current_val += 1
    
    print(ranges)

    #If current value = clue[i], increment both of them
    #If current value != clue[i], current value is missing 
    #Set min to current value. Keep incrementing current value until it equals clue[i]
    #Once current value = clue[i], set max to current value - 1. Add range to range list. Set min and max back to 'x'


clues = [0, 1, 3, 50, 75]
lower = 0
upper = 99
find_missing_clues(clues, lower, upper)

clues = [-1]
lower = -1
upper = -1
find_missing_clues(clues, lower, upper)

clues = []
lower = -1
upper = -1
find_missing_clues(clues, lower, upper)

clues = []
lower = 0
upper = 15
find_missing_clues(clues, lower, upper)

def harvest(vegetable_patch):
    num_carrots = 0
    for i in range(len(vegetable_patch)):
        for j in range(len(vegetable_patch[0])):
            if vegetable_patch[i][j] == 'c':
                num_carrots += 1

    print(num_carrots)

vegetable_patch = [
	['x', 'c', 'x'],
	['x', 'x', 'x'],
	['x', 'c', 'c'],
	['c', 'c', 'c']
]
harvest(vegetable_patch)

def local_maximums(grid):
    n = len(grid)
    local_maxes = [[0 for x in range(n-2)] for y in range(n-2)]

    for i in range(n-2):
        for j in range(n-2):
            local_maxes[i][j] = max(grid[i][j], grid[i][j+1], grid[i][j+2],
                                    grid[i+1][j], grid[i+1][j+1], grid[i+1][j+2],
                                    grid[i+2][j], grid[i+2][j+1], grid[i+2][j+2])
        
    print(local_maxes)

grid = [    
    [0,0,0],
    [0,0,0],
    [0,0,0]
]
local_maximums(grid)

grid = [
	[1, 1, 1, 1, 1],
	[1, 1, 1, 1, 1],
	[1, 1, 2, 1, 1],
	[1, 1, 1, 1, 1],
	[1, 1, 1, 1, 1]
]
local_maximums(grid)

def words_with_char(words, x):
    indices = []
    for i in range(len(words)):
        if words[i].find(x) > -1:
            indices.append(i)
    
    print(indices)

words = ["batman", "superman"]
x = "a"
words_with_char(words, x)

words = ["black panther", "hulk", "black widow", "thor"]
x = "a"
words_with_char(words, x)

words = ["star-lord", "gamora", "groot", "rocket"]
x = "z"
words_with_char(words, x)

def hulk_smash(n):
    answer = []
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            answer.append("HulkSmash")
        elif i % 3 == 0:
            answer.append("Hulk")
        elif i % 5 == 0:
            answer.append("Smash")
        else:
            answer.append(i)
    
    print(answer)

n = 3
hulk_smash(n)

n = 5
hulk_smash(n)

n = 15
hulk_smash(n)

def shuffle(message, indices):
    new_message = [0 for x in range(len(message))]

    for i in range(len(message)):
        new_message[indices[i]] = message[i]
    
    print("".join(new_message))

message = "evil"
indices = [3, 1, 2, 0]
shuffle(message, indices)

message = "a"
indices = [0]
shuffle(message, indices)

def minimum_boxes(meals, capacity):
    total_meals = sum(meals)
    total_boxes = 0
    capacity.sort(reverse = True)
    i = 0

    while total_meals > 0:
        total_meals -= capacity[i]
        i += 1
        total_boxes += 1
    
    print(total_boxes)

meals = [1, 3, 2]
capacity = [4, 3, 1, 5, 2]
minimum_boxes(meals, capacity)

meals = [5, 5, 5]
capacity = [2, 4, 2, 7]
minimum_boxes(meals, capacity)

def wealthiest_customer(accounts):
    total_wealth = [0 for customer in range(len(accounts))]
    max_wealth = 0
    customer = 0

    for i in range(len(accounts)):
        for j in range(len(accounts[i])):
            total_wealth[i] += accounts[i][j]
        
        if max_wealth < total_wealth[i]:
            max_wealth = total_wealth[i]
            customer = i
    
    print([customer, max_wealth])

accounts = [
	[1, 2, 3],
	[3, 2, 1]
]
wealthiest_customer(accounts)

accounts = [
	[1, 5],
	[7, 3],
	[3, 5]
]
wealthiest_customer(accounts)

accounts = [
	[2, 8, 7],
	[7, 1, 3],
	[1, 9, 5]
]
wealthiest_customer(accounts)

def smaller_than_current(nums):
    answer = []
    for i in range(len(nums)):
        smaller = 0
        for j in range(len(nums)):
            if j != i:
                if nums[j] < nums[i]:
                    smaller += 1
        
        answer.append(smaller)
    
    print(answer)

nums = [8, 1, 2, 2, 3]
smaller_than_current(nums)

nums = [6, 5, 4, 8]
smaller_than_current(nums)

nums = [7, 7, 7, 7]
smaller_than_current(nums)

def diagonal_sum(grid):
    sum = 0
    n = len(grid)
    for i in range(n):
        j_beg = i
        j_end = n - 1 - i

        if j_beg == j_end:
            sum += grid[i][j_beg]
        else:
            sum += grid[i][j_beg]
            sum += grid[i][j_end]
    print(sum)

grid = [
	[1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
diagonal_sum(grid)

grid = [
	[1, 1, 1, 1],
    [1, 1, 1, 1],
	[1, 1, 1, 1],
    [1, 1, 1, 1]
]
diagonal_sum(grid)

grid = [
	[5]
]
diagonal_sum(grid)

def defuse(code, k):
    if k==0:
        print([0] * len(code))
        return 0
    
    decrypted = []
    count_down = k

    for i in range(len(code)):
        sum = 0
        while count_down != 0:
            sum += code[(i + count_down)%len(code)]
            if count_down < 0:
                count_down += 1
            else:
                count_down -= 1
        
        count_down = k
        decrypted.append(sum)
    
    print(decrypted)

code = [5, 7, 1, 4]
k = 3
defuse(code, k)

code = [1, 2, 3, 4]
k = 0
defuse(code, k)

code = [2, 4, 9, 3]
k = -2
defuse(code, k)