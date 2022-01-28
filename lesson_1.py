from math import sqrt
import itertools


def all_ways():
    return list(list(itertools.permutations(['2', '3', '4', '5'])))


def distance_btwn_points(point_1, point_2):
    return sqrt((point_2[0] - point_1[0]) ** 2 + (point_2[1] - point_1[1]) ** 2)


def calculate_total_distance(A, B, C, D):
    return distance_btwn_points((0, 2), pt[A]) + distance_btwn_points(pt[A], pt[B]) + distance_btwn_points(pt[B], pt[C]) + distance_btwn_points(pt[C], pt[D]) + distance_btwn_points(pt[D], (0, 2))


pt = {
    '1': (0, 2),
    '2': (2, 5),
    '3': (5, 2),
    '4': (6, 6),
    '5': (8, 3)
}

min_distance = float('inf')
min_path = None
for path in all_ways():
    now_distance = calculate_total_distance(*path)
    if now_distance < min_distance:
        min_path = path
        min_distance = now_distance

count_1 = distance_btwn_points(pt['1'], pt[min_path[0]])
count_2 = distance_btwn_points(pt[min_path[0]], pt[min_path[1]]) + count_1
count_3 = distance_btwn_points(pt[min_path[1]], pt[min_path[2]]) + count_2
count_4 = distance_btwn_points(pt[min_path[2]], pt[min_path[3]]) + count_3

print(f'{pt["1"]} -> {pt[min_path[0]]}[{count_1}] -> '
	f'{pt[min_path[1]]}[{count_2}] -> '
    f'{pt[min_path[2]]}[{count_3}] -> '
    f'{pt[min_path[3]]}[{count_4}] -> '
    f'{pt["1"]}[{min_distance}] = {min_distance}')
