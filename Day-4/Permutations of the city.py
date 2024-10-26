import itertools
import math
cities=[(0,0), (1,3), (4,3), (6,1)]
min_distance=float('inf')
for perm in itertools.permutations(cities[1:]):
    current_path=[cities[0]] + list(perm)
    total_distance=0
    for i in range(len(current_path) - 1):
        total_distance += math.sqrt((current_path[i][0] - current_path[i+1][0]) ** 2 + (current_path[i][1] - current_path[i+1][1]) ** 2)
    if total_distance<min_distance:
        min_distance=total_distance
        best_path=current_path

print("Shortest path:", best_path)
print("Minimum Distance:", min_distance)

Output:
Shortest path: [(0, 0), (1, 3), (4, 3), (6, 1)]
Minimum Distance: 8.99070478491457
