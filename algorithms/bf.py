from itertools import permutations

def total_distance(tour, distances):
    distance = 0

    for i in range(len(tour)):
        city1 = tour[i]
        city2 = tour[(i + 1) % len(tour)]
        distance += distances[city1 - 1][city2 - 1]
    return distance


def bf(cities, distances):
    best_distance = float("inf")
    for tour in permutations(cities):
        tour = tour + (tour[0],)
        distance = total_distance(tour, distances)

        if distance < best_distance:
            best_distance = distance
            best_tour = tour
    return [i for i in best_tour], best_distance

