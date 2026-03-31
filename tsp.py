import numpy as np

distance_matrix = np.array([
    [0,10,15,20,25],
    [10,0,35,25,17],
    [15,35,0,30,28],
    [20,25,30,0,16],
    [25,17,28,16,0]  j 
])

def nnh(distance_matrix):
    n = len(distance_matrix)
    visited = [False] * n
    tour = []
    current_city = 0
    tour.append(current_city)
    visited[current_city] = True

    for _ in range(n - 1):
        nearest_city = None
        min_distance = float('inf')
        for city in range(n):
            if not visited[city] and distance_matrix[current_city][city] < min_distance:
                nearest_city = city
                min_distance = distance_matrix[current_city][city]
        current_city = nearest_city
        tour.append(current_city)
        visited[current_city] = True
    tour.append(tour[0])
    return tour

def ctl(tour , distance_matrix):
    tour_length = 0
    n = len(tour)
    for i in range(n-1):
        tour_length += distance_matrix[tour[i]][tour[i+1]]
    return tour_length

def tsp_n_n(distance_matrix):
    tour = nnh(distance_matrix)
    tour_length = ctl(tour,distance_matrix)
    return tour,tour_length

tour,tour_length = tsp_n_n(distance_matrix)
print("Tour:",tour)
print("Tour length:",tour_length)