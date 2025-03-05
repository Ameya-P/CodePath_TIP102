from collections import Counter
# # x = " " + str([1, 2, 3])
# # print(x)

# # positive_infinity = float('inf')
# # print(positive_infinity)

# # x = 3.14159
# # rounded = round(x, 3)
# # print(rounded)

# # print(abs(-10))

# # x = ["a", "b", "c", "d", "e"]

# # for i, val in enumerate(x):
# #     print(i, val)

# # x = ["a", "b", "c", "d", "e"]
# # y = [1, 2, 3, 4, 5]

# # for i in zip(x,y):
# #     print(i)

# d = {}
# d['d'] = 4
# print(d)

# d['d'] = 9
# print(d)
# print(d.get('c', 1))

# d['c'] = 9

# print(d.pop("d"), d)

# fruits = ["apple", "apple", "orange", "orange"]

# counts = {fruit : fruits.count(fruit) for fruit in fruits}

# print("apple" in counts)

# def lineup(artists, set_times):
#     results = {}
#     n = len(artists)

#     for i in range(n):
#         results[artists[i]] = set_times[i]
    
#     print(results)

# artists1 = ["Kendrick Lamar", "Chappell Roan", "Mitski", "Rosalia"]
# set_times1 = ["9:30 PM", "5:00 PM", "2:00 PM", "7:30 PM"]

# artists2 = []
# set_times2 = []

# print(lineup(artists1, set_times1))
# print(lineup(artists2, set_times2))

# def get_artist_info(artist, festival_schedule):

# def lineup(artists, set_times):
#     results = {}
#     n = len(artists)
#     for i in range(n):
#         results[artists[i]] = set_times[i]
    
#     return results

# artists1 = ["Kendrick Lamar", "Chappell Roan", "Mitski", "Rosalia"]
# set_times1 = ["9:30 PM", "5:00 PM", "2:00 PM", "7:30 PM"]

# artists2 = []
# set_times2 = []

# print(lineup(artists1, set_times1))
# print(lineup(artists2, set_times2))


# def get_artist_info(artist, festival_schedule):
#     return festival_schedule.get(artist, {"message": "Artist not found"})

# festival_schedule = {
#     "Blood Orange": {"day": "Friday", "time": "9:00 PM", "stage": "Main Stage"},
#     "Metallica": {"day": "Saturday", "time": "8:00 PM", "stage": "Main Stage"},
#     "Kali Uchis": {"day": "Sunday", "time": "7:00 PM", "stage": "Second Stage"},
#     "Lawrence": {"day": "Friday", "time": "6:00 PM", "stage": "Main Stage"}
# }

# print(get_artist_info("Blood Orange", festival_schedule)) 
# print(get_artist_info("Taylor Swift", festival_schedule)) 


# def total_sales(ticket_sales):
#     return sum(ticket_sales.values())

# ticket_sales = {"Friday": 200, "Saturday": 1000, "Sunday": 800, "3-Day Pass": 2500}

# print(total_sales(ticket_sales))

# def identify_conflicts(venue1_schedule, venue2_schedule):
#     conflicts = {}

#     for artist in venue1_schedule.keys():
#         if venue1_schedule.get(artist) == venue2_schedule.get(artist):
#             conflicts[artist] = venue1_schedule.get(artist)
    
#     return conflicts

# venue1_schedule = {
#     "Stromae": "9:00 PM",
#     "Janelle Monáe": "8:00 PM",
#     "HARDY": "7:00 PM",
#     "Bruce Springsteen": "6:00 PM"
# }

# venue2_schedule = {
#     "Stromae": "9:00 PM",
#     "Janelle Monáe": "10:30 PM",
#     "HARDY": "7:00 PM",
#     "Wizkid": "6:00 PM"
# }

# print(identify_conflicts(venue1_schedule, venue2_schedule))


# def best_set(votes):
#     counts = {}

#     for artist in votes.values():
#         if artist in counts:
#             counts[artist] += 1
#         else:
#             counts[artist] = 1
    
#     lst = list(counts.items())
#     lst.sort(reverse = True, key = lambda pair: pair[1])

#     #[[0,1], [1,2], [2,3]]

#     return lst[0][0]

# votes1 = {
#     1234: "SZA", 
#     1235: "Yo-Yo Ma",
#     1236: "Ethel Cain",
#     1237: "Ethel Cain",
#     1238: "SZA",
#     1239: "SZA"
# }

# votes2 = {
#     1234: "SZA", 
#     1235: "Yo-Yo Ma",
#     1236: "Ethel Cain",
#     1237: "Ethel Cain",
#     1238: "SZA"
# }

# print(best_set(votes1))
# print(best_set(votes2))
    
# def max_audience_performances(audiences):
#     max_audience = max(audiences)
#     return max_audience * audiences.count(max_audience)
#     total = sum(audience for audience in audiences if audience == max_audience)

# audiences1 = [100, 200, 200, 150, 100, 250]
# audiences2 = [120, 180, 220, 150, 220]

# print(max_audience_performances(audiences1))
# print(max_audience_performances(audiences2))

# def max_audience_performances(audiences):
#     max_audience = max(audiences)
#     counts = {}
#     for audience in audiences:
#         if audience in counts:
#             counts[audience] += 1
#         else:
#             counts[audience] = 1
    
#     return max_audience * counts[max_audience]

# audiences1 = [100, 200, 200, 150, 100, 250]
# audiences2 = [120, 180, 220, 150, 220]

# print(max_audience_performances(audiences1))
# print(max_audience_performances(audiences2))

# from collections import defaultdict

# def num_popular_pairs(popularity_scores):
#     songs = {}

#     for song in popularity_scores:
#         if song in songs:
#             songs[song][1] += songs[song][0]
#             songs[song][0] += 1

#         else:
#             songs[song] = [1, 0]
        
#     return sum([x[1] for x in songs.values()])

#     # pairs = 0

#     # for i in range(len(popularity_scores)):
#     #     for j in range(i + 1, len(popularity_scores)):
#     #         if popularity_scores[i] == popularity_scores[j]:
#     #             pairs += 1
    
#     # return pairs

# popularity_scores1 = [1, 2, 3, 1, 1, 3]
# popularity_scores2 = [1, 1, 1, 1]
# popularity_scores3 = [1, 2, 3]

# print(num_popular_pairs(popularity_scores1))
# print(num_popular_pairs(popularity_scores2))
# print(num_popular_pairs(popularity_scores3)) 

# def find_stage_arrangement_difference(s, t):
#     occurences = {}
#     for i in range((len(s))):
#         s_artist = s[i]
#         t_artist = t[i]
#         if s_artist in occurences.keys():
#             current = occurences[s_artist]
#             occurences[s_artist] = abs(current - i)
#         else:
#             occurences[s_artist] = i
        
#         if t_artist in occurences.keys():
#             current = occurences[t_artist]
#             occurences[t_artist] = abs(current - i)
#         else:
#             occurences[t_artist] = i
    
#     return sum(occurences.values())
    
# s1 = ["Alice", "Bob", "Charlie"]
# t1 = ["Bob", "Alice", "Charlie"]
# s2 = ["Alice", "Bob", "Charlie", "David", "Eve"]
# t2 = ["Eve", "David", "Bob", "Alice", "Charlie"]

# print(find_stage_arrangement_difference(s1, t1))
# print(find_stage_arrangement_difference(s2, t2))

# def num_VIP_guests(vip_passes, guests):
#     vip_set = set(vip_passes)
#     vips = 0
    
#     for guest in guests:
#         if guest in vip_set:
#             vips += 1
    
#     return vips

# vip_passes1 = "aA"
# guests1 = "aAAbbbb"

# vip_passes2 = "z"
# guests2 = "ZZ"

# print(num_VIP_guests(vip_passes1, guests1))
# print(num_VIP_guests(vip_passes2, guests2))

# def schedule_pattern(pattern, schedule):
    
#     genres = schedule.split()

#     if len(genres) != len(pattern):
#         return False

#     char_to_genre = {}
#     genre_to_char = {}

#     for char, genre in zip(pattern, genres):
#         if char in char_to_genre:
#             if char_to_genre[char] != genre:
#                 return False
#         else:
#             char_to_genre[char] = genre

#         if genre in genre_to_char:
#             if genre_to_char[genre] != char:
#                 return False
#         else:
#             genre_to_char[genre] = char

#     return True

# pattern1 = "abba"
# schedule1 = "rock jazz jazz rock"

# pattern2 = "abba"
# schedule2 = "rock jazz jazz blues"

# pattern3 = "aaaa"
# schedule3 = "rock jazz jazz rock"

# print(schedule_pattern(pattern1, schedule1))
# print(schedule_pattern(pattern2, schedule2))
# print(schedule_pattern(pattern3, schedule3))

# def two_sum(nums, target):
#     nums.sort()
#     left = 0
#     right = len(nums) - 1

#     while left < right:
#         if nums[left] + nums[right] == target:
#             return [left, right]
#         elif nums[left] + nums[right] < target:
#             left += 1
#         else: 
#             right -= 1

# nums = [2, 7, 11, 15, 20]
# target = 31
# print(two_sum(nums, target))

# nums = [2, 7, 11, 15]
# target = 18
# print(two_sum(nums, target))

# def sort_performers(performer_names, performance_times):
#     performance_dict = {}

#     for name, time in zip(performer_names, performance_times):
#         performance_dict[time] = name

#     return [v for k, v in sorted(performance_dict.items(), key=lambda item: item[0], reverse=True)]

# performer_names1 = ["Mary", "John", "Emma"]
# performance_times1 = [180, 165, 170]

# performer_names2 = ["Alice", "Bob", "Bob"]
# performance_times2 = [155, 185, 150]

# print(sort_performers(performer_names1, performance_times1)) 
# print(sort_performers(performer_names2, performance_times2))

# def space_crew(crew, position):
#     space = {}
#     for name, job in zip(crew, position):
#         space[name] = job
    
#     return space

# exp70_crew = ["Andreas Mogensen", "Jasmin Moghbeli", "Satoshi Furukawa", "Loral O'Hara", "Konstantin Borisov"]
# exp70_positions = ["Commander", "Flight Engineer", "Flight Engineer", " Flight Engineer", "Flight Engineer"] 

# ax3_crew = ["Michael Lopez-Alegria", "Walter Villadei", "Alper Gezeravci", "Marcus Wandt"]
# ax3_positions = ["Commander", "Mission Pilot", "Mission Specialist", "Mission Specialist"]

# print(space_crew(exp70_crew, exp70_positions))
# print(space_crew(ax3_crew, ax3_positions))

# def planet_lookup(planet_name):
#     planets = {
#     "Mercury": {
#         "Moons": 0,
#         "Orbital Period": 88
#     },
#     "Earth": {
#         "Moons": 1,
#         "Orbital Period": 365.25
#     },
#     "Mars": {
#         "Moons": 2,
#         "Orbital Period": 687
#     },
#     "Jupiter": {
#         "Moons": 79,
#         "Orbital Period": 10592
#     }
#     }

#     planet_dict = planets.get(planet_name)

#     if planet_dict:
#         orbital_period = planet_dict["Orbital Period"]
#         moons = planet_dict["Moons"]
#         return(f"Planet {planet_name} has an orbital period of {orbital_period} Earth days and has {moons} moons.")
#     else:
#         return "Sorry, I have no data on that planet."
    

# print(planet_lookup("Earth"))
# print(planet_lookup("Pluto"))

# def check_oxygen_levels(oxygen_levels, min_val, max_val):
#     rooms_with_oxygen = []
#     for room_name, level in oxygen_levels.items():
#         if level >= min_val and level <= max_val:
#             rooms_with_oxygen.append(room_name)
    
#     return room_name

# oxygen_levels = {
#     "Command Module": 21,
#     "Habitation Module": 20,
#     "Laboratory Module": 19,
#     "Airlock": 22,
#     "Storage Bay": 18
# }

# min_val = 19
# max_val = 22

# print(check_oxygen_levels(oxygen_levels, min_val, max_val))

# def data_difference(experiment1, experiment2):
#     results = {}

#     for key, val in experiment1.items():
#         val_2 = experiment2.get(key)
#         if not val_2:
#             results[key] = val
#         else:
#             if val_2 != val:
#                 results[key] = val
    
#     return results

# exp1_data = {'temperature': 22, 'pressure': 101.3, 'humidity': 45}
# exp2_data = {'temperature': 18, 'pressure': 101.3, 'radiation': 0.5}

# print(data_difference(exp1_data, exp2_data))

# def get_winner(votes):
#     vote_counter = Counter(votes)
#     max_val = float('-inf')
#     max_name = ''

#     for name, val in vote_counter.items():
#         if val > max_val:
#             max_val = val
#             max_name = name
    
#     return max_name

# votes1 = ["Colbert", "Serenity", "Serenity", "Tranquility", "Colbert", "Colbert"]
# votes2 = ["Serenity","Colbert", "Serenity", "Serenity", "Tranquility", "Colbert"]

# print(get_winner(votes1))
# print(get_winner(votes2))

# def check_if_complete_transmission(transmission):
#     trans_set = set()
#     for char in transmission:
#         trans_set.add(char)

#     return len(trans_set) == 26

# transmission1 = "thequickbrownfoxjumpsoverthelazydog"
# transmission2 = "spacetravel"

# print(check_if_complete_transmission(transmission1))
# print(check_if_complete_transmission(transmission2))

# def max_number_of_string_pairs(signals):
#     unpaired = set()
#     num_pairs = 0

#     for signal in signals:
#         reversed = signal[::-1]
#         if signal in unpaired:
#             unpaired.remove(signal)
#             num_pairs += 1
#         else:
#             unpaired.add(reversed)
    
#     return num_pairs

# signals1 = ["cd", "ac", "dc", "ca", "zz"]
# signals2 = ["ab", "ba", "cc"]
# signals3 = ["aa", "ab"]

# print(max_number_of_string_pairs(signals1))
# print(max_number_of_string_pairs(signals2))
# print(max_number_of_string_pairs(signals3))

# def find_difference(signals1, signals2):
#     signals1 = set(signals1)
#     signals2 = set(signals2)

#     return [list(signals1 - signals2), list(signals2 - signals1)]

# signals1_example1 = [1, 2, 3]
# signals2_example1 = [2, 4, 6]

# signals1_example2 = [1, 2, 3, 3]
# signals2_example2 = [1, 1, 2, 2]

# print(find_difference(signals1_example1, signals2_example1)) 
# print(find_difference(signals1_example2, signals2_example2))

# def find_common_signals(signals1, signals2):
#     one_freq = Counter(signals1)
#     two_freq = Counter(signals2)

#     i = 0
#     j = 0

#     for key, val in one_freq.items():
#         if key in two_freq:
#             i += val
#             j += two_freq[key]
    
#     return [i, j]
    

# signals1_example1 = [2, 3, 2]
# signals2_example1 = [1, 2]
# print(find_common_signals(signals1_example1, signals2_example1))

# signals1_example2 = [4, 3, 2, 3, 1]
# signals2_example2 = [2, 2, 5, 2, 3, 6]
# print(find_common_signals(signals1_example2, signals2_example2))

# signals1_example3 = [3, 4, 2, 3]
# signals2_example3 = [1, 5]
# print(find_common_signals(signals1_example3, signals2_example3))

def find_common_signals(signals1, signals2):
    set1 = set(signals1)
    set2 = set(signals2)

    common_elements = set1 & set2

    i = 0
    j = 0

    for element in common_elements:
        i += signals1.count(element)
        j += signals2.count(element)
    
    return [i, j]

signals1_example1 = [2, 3, 2]
signals2_example1 = [1, 2]
print(find_common_signals(signals1_example1, signals2_example1))

signals1_example2 = [4, 3, 2, 3, 1]
signals2_example2 = [2, 2, 5, 2, 3, 6]
print(find_common_signals(signals1_example2, signals2_example2))

signals1_example3 = [3, 4, 2, 3]
signals2_example3 = [1, 5]
print(find_common_signals(signals1_example3, signals2_example3))

def frequency_sort(signals):
    freq = {}
    for signal in signals:
        if signal in freq:
            freq[signal] += 1
        else:
            freq[signal] = 1

    sorted_signals = sorted(signals, key=lambda x: (freq[x], -x))

    return sorted_signals

signals1 = [1, 1, 2, 2, 2, 3]
signals2 = [2, 3, 1, 3, 2]
signals3 = [-1, 1, -6, 4, 5, -6, 1, 4, 1]

print(frequency_sort(signals1)) 
print(frequency_sort(signals2)) 
print(frequency_sort(signals3))

def find_final_hub(paths):
    hubA = set()
    hubB = set()

    for path in paths:
        hubA.add(path[0])
        hubB.add(path[1])
    
    return hubB - hubA

paths1 = [["Earth", "Mars"], ["Mars", "Titan"], ["Titan", "Europa"]]
paths2 = [["Alpha", "Beta"], ["Gamma", "Alpha"], ["Beta", "Delta"]]
paths3 = [["StationA", "StationZ"]]

print(find_final_hub(paths1)) 
print(find_final_hub(paths2)) 
print(find_final_hub(paths3))