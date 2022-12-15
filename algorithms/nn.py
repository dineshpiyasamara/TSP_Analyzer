def tsp_nearest_neighbor(cities, distances):
    n = len(cities)
    tour = [0]

    mask = (1 << 0)
    for _ in range(n - 1):
        nearest = None
        for i in range(1, n):
            if mask & (1 << i) == 0:
                if nearest is None or distances[tour[-1]][i] < distances[tour[-1]][nearest]:
                    nearest = i
        tour.append(nearest)
        mask |= (1 << nearest)

    tour.append(0)
    return tour


def compute_tour_distance(tour, distances):
    distance = 0
    for i in range(len(tour) - 1):
        distance += distances[tour[i]][tour[i + 1]]
    return distance


def nn(cities, distances):
    tour = tsp_nearest_neighbor(cities, distances)
    distances = compute_tour_distance(tour, distances)
    return [i+1 for i in tour], distances

