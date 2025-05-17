# '''
# You want to provide an overview of the NFT collection to potential buyers. One key statistic is the average value of the NFTs in the collection. However, if the collection is empty, the average value should be reported as 0.

# Write the average_nft_value function, which calculates and returns the average value of the NFTs in the collection.

# Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

# def average_nft_value(nft_collection):
#     pass
# Example Usage:

# nft_collection = [
#     {"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
#     {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2},
#     {"name": "Urban Jungle", "creator": "ArtByAlex", "value": 4.5}
# ]
# print(average_nft_value(nft_collection))

# nft_collection_2 = [
#     {"name": "Golden Hour", "creator": "SunsetArtist", "value": 8.9},
#     {"name": "Sunset Serenade", "creator": "SunsetArtist", "value": 9.4}
# ]
# print(average_nft_value(nft_collection_2))

# nft_collection_3 = []
# print(average_nft_value(nft_collection_3))
# '''

# def average_nft_value(nft_collection):
#     average = 0

#     if not nft_collection:
#         return 0
    
#     for nft in nft_collection:
#         average += nft["value"]
    
#     return average/len(nft_collection)

# nft_collection = [
#     {"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
#     {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2},
#     {"name": "Urban Jungle", "creator": "ArtByAlex", "value": 4.5}
# ]
# print(average_nft_value(nft_collection))

# nft_collection_2 = [
#     {"name": "Golden Hour", "creator": "SunsetArtist", "value": 8.9},
#     {"name": "Sunset Serenade", "creator": "SunsetArtist", "value": 9.4}
# ]
# print(average_nft_value(nft_collection_2))

# nft_collection_3 = []
# print(average_nft_value(nft_collection_3))

# '''
# Problem 5: NFT Tag Search
# Some NFTs are grouped into collections, and each collection might contain multiple NFTs. Additionally, each NFT can have a list of tags describing its style or theme (e.g., "abstract", "landscape", "modern"). You need to search through these nested collections to find all NFTs that contain a specific tag.

# Write the search_nft_by_tag() function, which takes in a nested list of NFT collections and a tag to search for. The function should return a list of NFT names that have the specified tag.

# Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

# def search_nft_by_tag(nft_collections, tag):
#     pass
# Example Usage:

# nft_collections = [
#     [
#         {"name": "Abstract Horizon", "tags": ["abstract", "modern"]},
#         {"name": "Pixel Dreams", "tags": ["pixel", "retro"]}
#     ],
#     [
#         {"name": "Urban Jungle", "tags": ["urban", "landscape"]},
#         {"name": "City Lights", "tags": ["modern", "landscape"]}
#     ]
# ]

# nft_collections_2 = [
#     [
#         {"name": "Golden Hour", "tags": ["sunset", "landscape"]},
#         {"name": "Sunset Serenade", "tags": ["sunset", "serene"]}
#     ],
#     [
#         {"name": "Pixel Odyssey", "tags": ["pixel", "adventure"]}
#     ]
# ]

# nft_collections_3 = [
#     [
#         {"name": "The Last Piece", "tags": ["finale", "abstract"]}
#     ],
#     [
#         {"name": "Ocean Waves", "tags": ["seascape", "calm"]},
#         {"name": "Mountain Peak", "tags": ["landscape", "adventure"]}
#     ]
# ]

# print(search_nft_by_tag(nft_collections, "landscape"))
# print(search_nft_by_tag(nft_collections_2, "sunset"))
# print(search_nft_by_tag(nft_collections_3, "modern"))
# '''

# def search_nft_by_tag(nft_collections, tag):
#     result = []

#     for collection in nft_collections:
#         for nft in collection:

#             if tag in nft["tags"]:
#                 result.append(nft["name"])
    
#     return result

# nft_collections = [
#     [
#         {"name": "Abstract Horizon", "tags": ["abstract", "modern"]},
#         {"name": "Pixel Dreams", "tags": ["pixel", "retro"]}
#     ],
#     [
#         {"name": "Urban Jungle", "tags": ["urban", "landscape"]},
#         {"name": "City Lights", "tags": ["modern", "landscape"]}
#     ]
# ]

# nft_collections_2 = [
#     [
#         {"name": "Golden Hour", "tags": ["sunset", "landscape"]},
#         {"name": "Sunset Serenade", "tags": ["sunset", "serene"]}
#     ],
#     [
#         {"name": "Pixel Odyssey", "tags": ["pixel", "adventure"]}
#     ]
# ]

# nft_collections_3 = [
#     [
#         {"name": "The Last Piece", "tags": ["finale", "abstract"]}
#     ],
#     [
#         {"name": "Ocean Waves", "tags": ["seascape", "calm"]},
#         {"name": "Mountain Peak", "tags": ["landscape", "adventure"]}
#     ]
# ]

# print(search_nft_by_tag(nft_collections, "landscape"))
# print(search_nft_by_tag(nft_collections_2, "sunset"))
# print(search_nft_by_tag(nft_collections_3, "modern"))

# '''
# Problem 6: NFT Queue Processing
# NFTs are added to a processing queue before they are displayed. The queue processes NFTs in a First-In, First-Out (FIFO) manner. Each NFT has a processing time, and you need to determine the order in which NFTs should be processed based on their initial position in the queue.

# Write the process_nft_queue() function, which takes a list of NFTs. The function should return a list of NFT names in the order they were processed.

# Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

# def process_nft_queue(nft_queue):
#     pass
# Example Usage:

# nft_queue = [
#     {"name": "Abstract Horizon", "processing_time": 2},
#     {"name": "Pixel Dreams", "processing_time": 3},
#     {"name": "Urban Jungle", "processing_time": 1}
# ]
# print(process_nft_queue(nft_queue))

# nft_queue_2 = [
#     {"name": "Golden Hour", "processing_time": 4},
#     {"name": "Sunset Serenade", "processing_time": 2},
#     {"name": "Ocean Waves", "processing_time": 3}
# ]
# print(process_nft_queue(nft_queue_2))

# nft_queue_3 = [
#     {"name": "Crypto Kitty", "processing_time": 5},
#     {"name": "Galactic Voyage", "processing_time": 6}
# ]
# print(process_nft_queue(nft_queue_3))
# '''

# def process_nft_queue(nft_queue):
#     result = []

#     for nft in nft_queue:
#         result.append(nft["name"])
    
#     return result

# nft_queue = [
#     {"name": "Abstract Horizon", "processing_time": 2},
#     {"name": "Pixel Dreams", "processing_time": 3},
#     {"name": "Urban Jungle", "processing_time": 1}
# ]
# print(process_nft_queue(nft_queue))

# nft_queue_2 = [
#     {"name": "Golden Hour", "processing_time": 4},
#     {"name": "Sunset Serenade", "processing_time": 2},
#     {"name": "Ocean Waves", "processing_time": 3}
# ]
# print(process_nft_queue(nft_queue_2))

# nft_queue_3 = [
#     {"name": "Crypto Kitty", "processing_time": 5},
#     {"name": "Galactic Voyage", "processing_time": 6}
# ]
# print(process_nft_queue(nft_queue_3))

# def find_closest_nft_values(nft_values, budget):
#     left = 0
#     right = len(nft_values) - 1

#     #Initialize a left pointer (starts at index 0) and a right pointer (starts at the last index)
#     #Increment the left pointer until you find a value that's greater than budget
#     #Increment the right pointer until you find a value that's less than budget

#     n = len(nft_values)
#     #Lands on a value that's less than or equal to budget
#     while left < n - 1 and nft_values[left + 1] <= budget:
#         left += 1
    
#     #Lands on a value that's greater than or equal to budget
#     while right > 0 and nft_values[right - 1] >= budget:
#         right -= 1

#     if left == right:
#         left_difference = budget - nft_values[left - 1]
#         right_difference = nft_values[right + 1] - budget

#         if left_difference < right_difference:
#             left = left - 1
#         else:
#             right = right + 1

#     return (nft_values[left],nft_values[right] )

# def find_closest_nft_values(nft_values, budget):
#     left = 0
#     right = len(nft_values) - 1

#     if nft_values[left] > budget:
#         return (None, nft_values[left])
    
#     if nft_values[right] < budget:
#         return (nft_values[right], None)
    
#     while right - left > 1:
#         middle = (right + left) // 2

#         if nft_values[middle] < budget:
#             left = middle 
#         elif nft_values[middle] > budget:
#             right = middle
#         else: 
#             left, right = middle, middle 
    
#     return (nft_values[left],nft_values[right])

# def find_closest_nft_values_old(nft_values, budget):
#     left = 0
#     right = len(nft_values) - 1

#     if nft_values[left] > budget:
#         return (None, nft_values[left])
    
#     if nft_values[right] < budget:
#         return (nft_values[right], None)
    
#     while right - left > 1:
#         middle = (right + left) // 2

#         if nft_values[middle] < budget:
#             left = middle 
#         elif nft_values[middle] > budget:
#             right = middle
#         else: 
#             left, right = middle, middle 
    
#     return (nft_values[left],nft_values[right])

# def find_closest_nft_values(nft_values, budget):
#     left = 0
#     right = len(nft_values) - 1
#     closest_below = None
#     closest_above = None
    
#     while left < right:
#         middle = (right + left) // 2

#         if nft_values[middle] == budget:
#             closest_below = closest_above = budget
#             left = right = middle
#         elif nft_values[middle] < budget:
#             closest_below = nft_values[middle]
#             left = middle + 1
#         elif nft_values[middle] > budget:
#             closest_above = nft_values[middle]
#             right = middle - 1
    
#     return (closest_below, closest_above)

# nft_values = [3.5, 5.4, 8.0, 8.0, 8.9]
# nft_values_2 = [2.0, 4.5, 6.3, 7.8, 12.1]
# nft_values_3 = [1.0, 2.5, 4.0, 6.0, 9.0]

# print(find_closest_nft_values(nft_values, 8))
# print(find_closest_nft_values(nft_values_2, 6.5))
# print(find_closest_nft_values(nft_values_3, 3.0))

# def filter_meme_lengths(memes, max_length):
#     #Time: O(n), Space: O(n)
#     result = []
#     for meme in memes:
#         if len(meme) <= max_length:
#             result.append(meme)
    
#     return result

# memes = ["This is hilarious!", "A very long meme that goes on and on and on...", "Short and sweet", "Too long! Way too long!"]
# memes_2 = ["Just right", "This one's too long though, sadly", "Perfect length", "A bit too wordy for a meme"]
# memes_3 = ["Short", "Tiny meme", "Small but impactful", "Extremely lengthy meme that no one will read"]

# print(filter_meme_lengths(memes, 20))
# print(filter_meme_lengths(memes_2, 15))
# print(filter_meme_lengths(memes_3, 10))

# def count_meme_creators(memes):
#     #Time: O(n), Space: O(n)
#     counts = {}
#     for meme in memes:
#         creator = meme["creator"]
#         if creator not in counts:
#             counts[creator] = 1
#         else:
#             counts[creator] += 1
    
#     return counts

# memes = [
#     {"creator": "Alex", "text": "Meme 1"},
#     {"creator": "Jordan", "text": "Meme 2"},
#     {"creator": "Alex", "text": "Meme 3"},
#     {"creator": "Chris", "text": "Meme 4"},
#     {"creator": "Jordan", "text": "Meme 5"}
# ]

# memes_2 = [
#     {"creator": "Sam", "text": "Meme 1"},
#     {"creator": "Sam", "text": "Meme 2"},
#     {"creator": "Sam", "text": "Meme 3"},
#     {"creator": "Taylor", "text": "Meme 4"}
# ]

# memes_3 = [
#     {"creator": "Blake", "text": "Meme 1"},
#     {"creator": "Blake", "text": "Meme 2"}
# ]

# print(count_meme_creators(memes))
# print(count_meme_creators(memes_2))
# print(count_meme_creators(memes_3))

# def find_trending_memes(memes):
#     #Time: O(n), Space: O(n)
#     meme_set = set()
#     result_set = set()
#     for meme in memes:
#         if meme in meme_set:
#             result_set.add(meme)
#         else:
#             meme_set.add(meme)
    
#     return list(result_set)

# memes = ["Dogecoin to the moon!", "One does not simply walk into Mordor", "Dogecoin to the moon!", "Distracted boyfriend", "One does not simply walk into Mordor"]
# memes_2 = ["Surprised Pikachu", "Expanding brain", "This is fine", "Surprised Pikachu", "Surprised Pikachu"]
# memes_3 = ["Y U No?", "First world problems", "Philosoraptor", "Bad Luck Brian"]

# print(find_trending_memes(memes))
# print(find_trending_memes(memes_2))
# print(find_trending_memes(memes_3))

# def reverse_memes(memes):
#     #Time: O(n), Space: O(1)
#     left = 0
#     right = len(memes) - 1

#     while left < right:
#         memes[left], memes[right] = memes[right], memes[left]
#         left += 1
#         right -= 1

#     return memes

# memes = ["Dogecoin to the moon!", "Distracted boyfriend", "One does not simply walk into Mordor"]
# memes_2 = ["Surprised Pikachu", "Expanding brain", "This is fine"]
# memes_3 = ["Y U No?", "First world problems", "Philosoraptor", "Bad Luck Brian"]

# print(reverse_memes(memes))
# print(reverse_memes(memes_2))
# print(reverse_memes(memes_3))

# def find_trending_meme_pairs(meme_posts):
#     pair_count = {}

#     for post in meme_posts:
#         for i in range(len(post)):
#             for j in range(len(post)):
#                 if i != j:
#                     meme1 = post[i]
#                     meme2 = post[j]

#                     if meme1 < meme2:
#                         meme1, meme2 = meme2, meme1
#                     pair = (meme1, meme2)
#                     if pair in pair_count:
#                         pair_count[pair] += 1
#                     else:
#                         pair_count[pair] = 1

#     trending_pairs = []
#     for pair in pair_count:
#         if pair_count[pair] >= 2:
#             trending_pairs.append(pair)

#     return trending_pairs

# def my_find_trending_meme_pairs(meme_posts):
#     if not meme_posts:
#         return []
    
#     pair_counts = {}

#     for post in meme_posts:
#         for i in range(len(post)):
#             for j in range(i+1, len(post)):
#                 tuple_a = (post[i], post[j])
#                 tuple_b = (post[j], post[i])
#                 if tuple_a in pair_counts:
#                     pair_counts[tuple_a] += 1
#                 elif tuple_b in pair_counts:
#                     pair_counts[tuple_b] += 1
#                 else:
#                     pair_counts[tuple_a] = 1

#     results = []
#     max_val = max(list(pair_counts.values()))

#     for key, val in pair_counts.items():
#         if val == max_val:
#             results.append(key)

#     return results

# def find_trending_meme_pairs(meme_posts):
#     pair_count = {}

#     for post in meme_posts:
#         for i in range(len(post)):
#             for j in range(i+ 1, len(post)):
#                 if i != j:
#                     meme1 = post[i]
#                     meme2 = post[j]

#                     if meme1 > meme2:
#                         meme1, meme2 = meme2, meme1
#                     pair = (meme1, meme2)
#                     if pair in pair_count:
#                         pair_count[pair] += 1
#                     else:
#                         pair_count[pair] = 1

#     trending_pairs = []
#     for pair, count in pair_count.items():
#         if count > 1:
#             trending_pairs.append(pair)

#     return trending_pairs

# meme_posts_1 = [

#     ["Dogecoin to the moon!", "Distracted boyfriend"],
#     ["One does not simply walk into Mordor", "Dogecoin to the moon!"],
#     ["Dogecoin to the moon!", "Distracted boyfriend", "One does not simply walk into Mordor"],
#     ["Distracted boyfriend", "One does not simply walk into Mordor"]
   
# ]

# meme_posts_2 = [
#     ["Surprised Pikachu", "This is fine"],
#     ["Expanding brain", "Surprised Pikachu"],
#     ["This is fine", "Expanding brain"],
#     ["Surprised Pikachu", "This is fine"]
# ]

# meme_posts_3 = [
#     ["Y U No?", "First world problems"],
#     ["Philosoraptor", "Bad Luck Brian"],
#     ["First world problems", "Philosoraptor"],
#     ["Y U No?", "First world problems"]
# ]

# print(find_trending_meme_pairs(meme_posts_1))
# print(find_trending_meme_pairs(meme_posts_2))
# print(find_trending_meme_pairs(meme_posts_3))

# from collections import deque


# def simulate_meme_reposts(memes, reposts):
#     #Time: O(R), Space O(R), r = total number of reposts
#     meme_queue = deque(memes)
#     repost_queue = deque(reposts)
#     final_order = []

#     while meme_queue:
#         current_meme = meme_queue.popleft()
#         reposts_left = repost_queue.popleft()

#         if reposts_left > 0:
#             final_order.append(current_meme)
#             meme_queue.append(current_meme)
#             repost_queue.append(reposts_left - 1)
        
#         print(current_meme, reposts_left)
    
#     return final_order


# memes = ["Distracted boyfriend", "Dogecoin to the moon!", "One does not simply walk into Mordor"]
# reposts_1 = [2, 1, 3]

# memes_2 = ["Surprised Pikachu", "This is fine", "Expanding brain"]
# reposts_2 = [1, 2, 2]

# memes_3 = ["Y U No?", "Philosoraptor"]
# reposts_3 = [3, 1]

# print(simulate_meme_reposts(memes, reposts_1))
# print(simulate_meme_reposts(memes_2, reposts_2))
# print(simulate_meme_reposts(memes_3, reposts_3))

def find_closest_meme_pair(memes, target):
    prev_l = left = 0
    prev_r = right = len(memes) - 1
    previous = None

    while left + 1 < right:
        current = memes[left][1] + memes[right][1]

        if current == target:
            break
        elif current < target:
            previous = current
            prev_r = right
            prev_l = left
            left += 1
        elif current > target:
            previous = current
            prev_r = right
            prev_l = left
            right -= 1
    
    return (memes[left][0], memes[right][0])

memes_1 = [("Distracted boyfriend", 5), ("Dogecoin to the moon!", 7), ("One does not simply walk into Mordor", 12)]
memes_2 = [("Surprised Pikachu", 2), ("This is fine", 6), ("Expanding brain", 9), ("Y U No?", 15)]
memes_3 = [("Philosoraptor", 1), ("Bad Luck Brian", 4), ("First world problems", 8), ("Y U No?", 13)]

#print(find_closest_meme_pair(memes_1, 13))
print(find_closest_meme_pair(memes_2, 10))
print(find_closest_meme_pair(memes_3, 12))

def subarray_sum(nums, k):
    #Dynamic Sliding Windows Technique 
    num_sub_arrays = 0
    left = 0
    right = 1
    current_sum = None
    while right < len(nums):
        current_sum = nums[left] if left == right else nums[left] + nums[right]

        if current_sum == k:
            num_sub_arrays += 1
            left += 1
            right += 1
        elif current_sum < k:
            right += 1
        elif current_sum > k:
            left += 1
        

    
    return num_sub_arrays

print(subarray_sum([1, 1, 1], 2))


def subarray_sum(nums, k):
    #Dynamic Sliding Windows Technique 
    print(nums, k)
    
    num_sub_arrays = 0
    left = 0
    right = 1
    current_sum = None

    while right < len(nums):
        current_sum = nums[left] if left == right else nums[left] + nums[right]
        
        if current_sum == k:
            num_sub_arrays += 1
            left += 1
            right += 1
        elif current_sum < k:
            right += 1
        elif current_sum > k:
            left += 1
    
    return num_sub_arrays
        
    #If subarray is less than k, add element to front.
    #If subarray is greater than k, remove element from back

    def subarray_sum(nums, k):
    num_subarrays = 0
    
    for i in range(len(nums)):
        current_sum = 0
        for j in range(i, len(nums)):
            
            if i == j:
                current_sum = nums[i]
            else: 
                current_sum += nums[j]
            
            if current_sum == k:
                num_subarrays += 1
    
    return num_subarrays