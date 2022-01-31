from math import sqrt
import itertools


def all_ways():
    return list(itertools.permutations(['2', '3', '4', '5']))


def distance_btwn_points(point_1, point_2):
    return sqrt((point_2[0] - point_1[0]) ** 2 + (point_2[1] - point_1[1]) ** 2)


def calculate_total_distance(A, B, C, D):
    return distance_btwn_points((0, 2), pt[A]) + distance_btwn_points(pt[A], pt[B]) + distance_btwn_points(pt[B], pt[C]) + distance_btwn_points(pt[C], pt[D]) + distance_btwn_points(pt[D], (0, 2))


def print_path(point_1, point_2):
    global count
    count += distance_btwn_points(point_1, point_2)
    print(f' -> {point_2}[{count}]', end='')

pt = {
    '1': (0, 2),
    '2': (2, 5),
    '3': (5, 2),
    '4': (6, 6),
    '5': (8, 3)
}

count, min_distance, min_path = 0, float('inf'), None
for path in all_ways():
    now_distance = calculate_total_distance(*path)
    if now_distance < min_distance:
        min_path = path
        min_distance = now_distance
min_path = list(min_path)
min_path.insert(0, '1')
min_path.append('1')

print(f'{pt["1"]}', end='')
for i in range(len(min_path) - 1):
    print_path(pt[min_path[i]], pt[min_path[i + 1]])
print(f' = {min_distance}')
