def find_farthest_orbit(nums_list):
    return max(nums_list, key=lambda x: (x[0] != x[1]) * x[0] * x[1])


orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3), (11, 11)]
print(find_farthest_orbit(orbits))