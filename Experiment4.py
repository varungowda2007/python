import heapq
def a_star_search(graph,heuristics,start,goal):
    open_list = []
    heapq.heappush(open_list, (0,start))
    came_from = {}
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0
    f_score = {node: float('inf') for node in graph}
    f_score[start] = heuristics[start]
    while open_list:
        current = heapq.heappop(open_list)[1]

        if current == goal:
            return reconstuct_path(came_from, current)
        for neighbor, cost in graph[current].items():
            tentative_g_score = g_score[current] + cost
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score[neighbor] + heuristics[neighbor]
                if neighbor not in [i[1] for i in open_list]:
                    heapq.heappush(open_list,(f_score[neighbor], neighbor))
    return None

def reconstuct_path(came_from,current):
    total_path = [current]
    while current in came_from:
        current = came_from[current]
        total_path.append(current)
    total_path.reverse()
    return total_path

graph = {
    'S' : {'B': 4, 'C': 3},
    'B' : {'F': 5, 'E': 12},
    'C' : {'D': 7, 'E': 10},
    'D' : {'E': 2},
    'E' : {'G': 5},
    'F' : {'G': 16},
    'G' : {}
}

heuristics = {
    'S' : 14,
    'B' : 12,
    'C' : 11,
    'D' : 6,
    'E' : 4,
    'F' : 11,
    'G' : 0,
}

start_node = 'S'
goal_node = 'G'
path = a_star_search(graph, heuristics, start_node,goal_node)
print(f"Path from {start_node} to {goal_node}: {path}")