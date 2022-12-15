def tsp_held_karp(cities, distances):
    n = len(cities)
    dist = [[float('inf')] * (1 << n) for _ in range(n)]
    
    for i in range(n):
        dist[i][1 << i] = 0
    
    for mask in range(1, 1 << n):
        for i in range(n):
            if mask & (1 << i) == 0:
                continue
            for j in range(n):
                if mask & (1 << j) == 0:
                    continue
                dist[i][mask] = min(dist[i][mask], dist[j][mask ^ (1 << i)] + distances[i][j])
    
    best_distance = float('inf')
    best_tour = None
    for i in range(n):
        if dist[i][(1 << n) - 1] < best_distance:
            best_distance = dist[i][(1 << n) - 1]
            best_tour = i
    
    mask = (1 << n) - 1
    tour = [best_tour]
    while mask != 0:
        mask ^= (1 << best_tour)
        best_tour = min(range(n), key=lambda i: dist[i][mask] + distances[i][best_tour])
        tour.append(best_tour)
    tour.reverse()
    return tour

def find_distances(tour, distances):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += distances[tour[i]][tour[i + 1]]
    return total_distance


def dp(cities, distances):
    tour = tsp_held_karp(cities, distances)
    best_distance = find_distances(tour, distances)
    return [i+1 for i in tour], best_distance