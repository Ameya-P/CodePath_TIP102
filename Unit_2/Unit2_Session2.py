# def prioritize_observations(observed_species, priority_species):
#     count = {}

#     for species in observed_species:
#         if count.get(species):
#             count[species] += 1
#         else:
#             count[species] = 1
    
#     organized = []

#     for species in priority_species:
#         organized.extend([species] * count.pop(species))
        
#     organized.extend(sorted(count))
#     return organized

# observed_species1 = ["🐯", "🦁", "🦌", "🦁", "🐯", "🐘", "🐍", "🦑", "🐻", "🐯", "🐼"]
# priority_species1 = ["🐯", "🦌", "🐘", "🦁"]  

# observed_species2 = ["bluejay", "sparrow", "cardinal", "robin", "crow"]
# priority_species2 = ["cardinal", "sparrow", "bluejay"]

# print(prioritize_observations(observed_species1, priority_species1))
# print(prioritize_observations(observed_species2, priority_species2)) 

# def distinct_averages(species_populations):
#     averages = set()
#     species_populations.sort()

#     while len(species_populations) > 0:
#         min = species_populations.pop(0)
#         max = species_populations.pop(-1)
#         averages.add((min + max)/2)
    
#     return len(averages)

# species_populations1 = [4,1,4,0,3,5]
# species_populations2 = [1,100]

# print(distinct_averages(species_populations1))
# print(distinct_averages(species_populations2)) 

# def max_species_copies(raised_species, target_species):
#     raised = {}
#     for species in raised_species:
#         if species in raised.keys():
#             raised[species] += 1
#         else:
#             raised[species] = 1

#     target = {}
#     for species in target_species:
#         if species in target.keys():
#             target[species] += 1
#         else:
#             target[species] = 1
    
#     min = float('inf')
#     for species in target.keys():
#         num_copies = raised[species] // target[species]
#         if min > num_copies:
#             min = num_copies
    
#     return min

# print("-------------")

# raised_species1 = "abcba"
# target_species1 = "abc"
# print(max_species_copies(raised_species1, target_species1))  # Output: 1

# raised_species2 = "aaaaabbbbcc"
# target_species2 = "abc"
# print(max_species_copies(raised_species2, target_species2)) # Output: 2


# def count_unique_species(ecosystem_data):
#     ecosystem_nums = ''

#     for character in ecosystem_data:
#         if str(character).isalpha():
#             ecosystem_nums += ' '
#         else:
#             ecosystem_nums += character
    
#     nums = ecosystem_nums.split()
#     nums_set = set()

#     for num in nums:
#         nums_set.add(float(num))
    
#     return len(nums_set)

# ecosystem_data1 = "f123de34g8hi34"
# ecosystem_data2 = "species1234forest234"
# ecosystem_data3 = "x1y01z001"


# print("-----------------------------------")
# print(count_unique_species(ecosystem_data1))
# print(count_unique_species(ecosystem_data2))
# print(count_unique_species(ecosystem_data3))

# def num_equiv_species_pairs_old(species_pairs):
#     num_pairs = 0
#     pair_dict = {}
#     #Count how many times something shows up 
#     for pair in species_pairs:
#         reverse_pair = pair[::-1]
#         pair = tuple(pair)
#         reverse_pair = tuple(reverse_pair)
#         if pair in pair_dict.keys():
#             pair_dict[pair] += 1
#         elif reverse_pair in pair_dict.keys():
#             pair_dict[reverse_pair] += 1
#         else:
#             pair_dict[pair] = 1
    
#     for n in pair_dict.values():
#         num_pairs += (n * (n-1)) // 2
    
#     return num_pairs

# def num_equiv_species_pairs(species_pairs):
#     num_pairs = 0
#     pair_dict = {}
#     #Count how many times something shows up 
#     for pair in species_pairs:
#         pair.sort()
#         pair = tuple(pair)
#         if pair in pair_dict.keys():
#             pair_dict[pair] += 1
#         else:
#             pair_dict[pair] = 1
    
#     for n in pair_dict.values():
#         num_pairs += (n * (n-1)) // 2
    
#     return num_pairs

# print("-----------------------------------")
# species_pairs1 = [[1,2],[2,1],[3,4],[5,6]]
# species_pairs2 = [[1,2],[1,2],[1,1],[1,2],[2,2]]

# print(num_equiv_species_pairs(species_pairs1))
# print(num_equiv_species_pairs(species_pairs2))

from collections import Counter


# def remove_low_rated_destinations(destinations, rating_threshold):
#     keys_to_remove = []

#     for key, value in destinations.items():
#         if value < rating_threshold:
#             keys_to_remove.append(key)
    
#     for key in keys_to_remove:
#         destinations.pop(key)
    
#     return destinations

# destinations = {"Paris": 4.8, "Berlin": 3.5, "Addis Ababa": 4.9, "Moscow": 2.8}
# destinations2 = {"Bogotá": 4.8, "Kansas City": 3.9, "Tokyo": 4.5, "Sydney": 3.0}

# print(remove_low_rated_destinations(destinations, 4.0))
# print(remove_low_rated_destinations(destinations2, 4.9))

# def unique_souvenir_counts(souvenirs):
#     counts = Counter(souvenirs)
#     unique_counts = set(counts.values())

#     return len(unique_counts) == len(counts.keys())
    
# souvenirs1 = ["keychain", "hat", "hat", "keychain", "keychain", "postcard"]
# souvenirs2 = ["postcard", "postcard", "postcard", "postcard"]
# souvenirs3 = ["keychain", "magnet", "hat", "candy", "postcard", "stuffed bear"]

# print(unique_souvenir_counts(souvenirs1))  
# print(unique_souvenir_counts(souvenirs2)) 
# print(unique_souvenir_counts(souvenirs3))

# def decode_message(key, message):
#     alphabet = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h', 8: 'i', 9: 'j', 10: 'k', 11: 'l', 12: 'm', 13: 'n', 14: 'o', 15: 'p', 16: 'q', 17: 'r', 18: 's', 19: 't', 20: 'u', 21: 'v', 22: 'w', 23: 'x', 24: 'y', 25: 'z'}

#     #Create decoder dictionary
#     decoder = {}
#     key = key.replace(" ", "")
#     key = list(key)

#     current_index = 0
#     for char in key:
#         if char not in decoder:
#             decoder[char] = alphabet[current_index]
#             current_index += 1
    
#     new_message = ""
#     for char in message:
#         if str(char).isalpha():
#             new_message += decoder[char]
#         else:
#             new_message += " "
    
#     return new_message

# key1 = "the quick brown fox jumps over the lazy dog"
# message1 = "vkbs bs t suepuv"

# print(decode_message(key1, message1))

# key2 = "eljuxhpwnyrdgtqkviszcfmabo"
# message2 = "hntu depcte lxejw lxwntu zwx piqfx"

# print(decode_message(key2, message2))

# # alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# # a_dict = {}
# # for number, letter  in zip(range(27), alpha):
# #     a_dict[number] = letter

# # print(a_dict)

# def find_longest_harmonious_travel_sequence(ratings):
#     # Initialize a dictionary to store the frequency of each rating
#     frequency = {}

#     # Count the occurrences of each rating
#     for rating in ratings:
#         if rating in frequency:
#             frequency[rating] += 1 
#         else:
#             frequency[rating] = 1

#     max_length = 0

#     # Find the longest harmonious sequence
#     for rating in frequency:
#         if rating + 1 in frequency:
#             max_length = max(max_length, 
#                         frequency[rating] + frequency[rating + 1])  

#     return max_length

# durations1 = [1, 3, 2, 2, 5, 2, 3, 7]
# durations2 = [1, 2, 3, 4]
# durations3 = [1, 1, 1, 1]

# print(find_longest_harmonious_travel_sequence(durations1))
# print(find_longest_harmonious_travel_sequence(durations2)) 
# print(find_longest_harmonious_travel_sequence(durations3)) 

# def is_route_covered(trips, start_dest, end_dest):
#     destinations = set(range(start_dest, end_dest + 1))

#     for trip in trips:
#         for i in range(trip[0], trip[1] + 1):
#             if i in destinations:
#                 destinations.remove(i)

#     return len(destinations) == 0

# trips1 = [[1, 2], [3, 4], [5, 6]]
# start_dest1, end_dest1 = 2, 5

# trips2 = [[1, 10], [10, 20]]
# start_dest2, end_dest2 = 21, 21

# trips3 = [[1, 2], [3, 5]]
# start_dest3, end_dest3 = 2, 5

# print(is_route_covered(trips1, start_dest1, end_dest1))
# print(is_route_covered(trips2, start_dest2, end_dest2))
# print(is_route_covered(trips3, start_dest3, end_dest3))

# def most_popular_even_destination(destinations):
#     counts = Counter(destinations)
#     counts = sorted(counts, key=lambda x: (-counts[x], x%2 != 0))

#     if counts[0] % 2 == 0:
#         return counts[0]
#     else:
#         return -1


# destinations1 = [0, 1, 2, 2, 4, 4, 1]
# destinations2 = [4, 4, 4, 9, 2, 4]
# destinations3 = [29, 47, 21, 41, 13, 37, 25, 7]

# print(most_popular_even_destination(destinations1))
# print(most_popular_even_destination(destinations2))
# print(most_popular_even_destination(destinations3))

def is_valid_itinerary(itinerary):
    n= len(itinerary) - 1
    unique_cities = set(range(1, n))

    for city in itinerary:
        if city in unique_cities:
            unique_cities.remove(city)
    
    return len(unique_cities) == 0 and itinerary.count(n) == 2

itinerary1 = [2, 1, 3]
itinerary2 = [1, 3, 3, 2]
itinerary3 = [1, 1]

print(is_valid_itinerary(itinerary1))
print(is_valid_itinerary(itinerary2))
print(is_valid_itinerary(itinerary3))

def find_attractions(tourist_list1, tourist_list2):
    common_attractions = set(tourist_list1) & set(tourist_list2)

    names = []
    min_val = float('inf')

    for atttraction in common_attractions:
        travel_time = tourist_list1.index(atttraction) + tourist_list2.index(atttraction)
        if travel_time < min_val:
            names.clear()
            names.append(atttraction)
            min_val = travel_time
        elif travel_time == min_val:
            names.append(atttraction)
    
    return names

tourist_list1 = ["Eiffel Tower","Louvre Museum","Notre-Dame","Disneyland"]
tourist_list2 = ["Colosseum","Trevi Fountain","Pantheon","Eiffel Tower"]

print(find_attractions(tourist_list1, tourist_list2))

tourist_list1 = ["Eiffel Tower","Louvre Museum","Notre-Dame","Disneyland"]
tourist_list2 = ["Disneyland","Eiffel Tower","Notre-Dame"]

print(find_attractions(tourist_list1, tourist_list2))

tourist_list1 = ["beach","mountain","forest"]
tourist_list2 = ["mountain","beach","forest"]

print(find_attractions(tourist_list1, tourist_list2))