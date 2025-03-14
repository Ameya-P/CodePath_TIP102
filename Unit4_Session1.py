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

def find_closest_nft_values(nft_values, budget):
    left = 0
    right = len(nft_values) - 1

    if nft_values[left] > budget:
        return (None, nft_values[left])
    
    if nft_values[right] < budget:
        return (nft_values[right], None)
    
    while right - left > 1:
        middle = (right + left) // 2

        if nft_values[middle] < budget:
            left = middle 
        elif nft_values[middle] > budget:
            right = middle
        else: 
            left, right = middle, middle 
    
    return (nft_values[left],nft_values[right])

nft_values = [3.5, 5.4, 8.0, 8.0, 8.9]
nft_values_2 = [2.0, 4.5, 6.3, 7.8, 12.1]
nft_values_3 = [1.0, 2.5, 4.0, 6.0, 9.0]

print(find_closest_nft_values(nft_values, 3.4))
print(find_closest_nft_values(nft_values_2, 6.5))
print(find_closest_nft_values(nft_values_3, 3.0))