# File: graph.py

import math

def make_coordinates(line):
    global list_of_coordinates
    global list_of_names
    n = int(line[0])
    list_of_coordinates = []
    list_of_names = []
    for i in range(1, n+1):
        coordinates = line[i].split(" ")
        coords_list = [float(coordinates[1]), float(coordinates[2])]
        list_of_coordinates.append(coords_list)
        list_of_names.append(coordinates[0])
    # print(list_of_names)
    return list_of_coordinates, list_of_names

def make_list_of_lat(c):
    global list_lat
    list_lat = []
    for i in range(len(c)):
        list_lat.append(c[i][0])
    return list_lat

def make_list_of_lon(c):
    global list_lon
    list_lon = []
    for i in range(len(c)):
        list_lon.append(c[i][1])
    return list_lon

def avg_lat(x):
    return sum(x) / len(x)

def avg_lon(x):
    return sum(x) / len(x)

def make_matrix(lines):
    n = int(lines[0])
    adj_matrix = []
    for i in range(n+1, n*2+1):
        line = lines[i].split(" ")
        adj_matrix.append(line)
    return adj_matrix

def make_adj_list(m):
    global adj_list
    global list_of_names
    adj_list = []
    for i in range(0, len(m)):
        neighbor = []
        for j in range(0, len(m)):
            if m[i][j] == '1':
                name = convert_to_name(j)
                neighbor.append(name)
        adj_list.append(neighbor)
    return adj_list               

def make_adj_matrix(m):
    global adj_matrix
    global list_of_coordinates
    n = len(m)
    adj_matrix = [[ 0 for i in range(n)] for j in range(n)]
    for i in range(0,n):
        for j in range(0,n):
            if m[i][j] == '1':
                distance = haversineDistance(list_of_coordinates[i],list_of_coordinates[j])
                adj_matrix[i][j] = distance
    return adj_matrix

def make_heuristic_matrix(m):
    global heuristic_matrix
    global list_of_coordinates
    n = len(m)
    heuristic_matrix = [[ 0 for i in range(n)] for j in range(n)]
    for i in range(0,n):
        for j in range(0,n):
            if (i!=j):
                distance = haversineDistance(list_of_coordinates[i],list_of_coordinates[j])
                heuristic_matrix[i][j] = distance
            else:
                heuristic_matrix[i][j] = 0
    return heuristic_matrix

# Convert coordinates to distance
def haversineDistance(a,b):
    lat1 = a[0]
    lon1 = a[1]
    lat2 = b[0]
    lon2 = b[1]
    lat1_rad = lat1 * math.pi / 180.0
    lat2_rad = lat2 * math.pi / 180.0 
    delta_lat = (lat2 - lat1) * math.pi / 180.0
    delta_lon = (lon2 - lon1) * math.pi / 180.0
    a = (pow(math.sin(delta_lat / 2), 2) + pow(math.sin(delta_lon / 2), 2) * math.cos(lat1_rad) * math.cos(lat2_rad))
    r = 6371
    distance = 2 * r * math.asin(math.sqrt(a)) * 1000
    return distance

# convert node to index
def convert_to_idx(node_name):
    global list_of_names
    idx = 0
    for i in range(len(list_of_names)):
        if (list_of_names[i] == node_name):
            idx = i
    return idx

# convert node to name
def convert_to_name(idx):
    global list_of_names
    name = ''
    for i in range(len(list_of_names)):
        if (i == idx):
            name = list_of_names[i]
    return name

# UCS Algorithm
def ucs(initial, final):
    global adj_matrix
    global adj_list
    global list_of_names
    global path

    idx_initial = convert_to_idx(initial)
    idx_final = convert_to_idx(final)
    queue = [[idx_initial, 0, [initial]]]
    visited = set()
    current_node = []
    
    while(len(queue) != 0):
        # dequeue
        current_node = queue.pop(0)
        current_node_idx = convert_to_idx(current_node[0])
        if (current_node_idx == idx_final):
            break
        if current_node[0] not in visited:
            visited.add(current_node[0])
            for neighbor in adj_list[current_node_idx]:
                visited_node = []
                for c in current_node[2]:
                    visited_node.append(c)
                i = convert_to_idx(neighbor)
                visited_node.append(neighbor)
                # masukkan node ke queue
                # param: current_node name, g(current_node), visited_node ke queue
                queue.append([neighbor, current_node[1] + adj_matrix[current_node_idx][i], visited_node])
            # priority queue
            queue.sort(key = lambda q : q[1])

    # shortest path
    path = current_node[2]

    # calculate cost
    cost = 0 
    path_cost = []
    for node in path:
        path_cost.append(convert_to_idx(node))
    for i in range(len(path)-1):
        cost += adj_matrix[path_cost[i]][path_cost[i+1]]

    return path, cost

# A* Algorithm
def astar(initial, final):
    global adj_matrix
    global heuristic_matrix
    global adj_list
    global list_of_names
    global path
    
    idx_initial = convert_to_idx(initial)
    idx_final = convert_to_idx(final)
    queue = [[idx_initial, 0, [initial]]]
    current_node = []

    while(len(queue) != 0):
        # dequeue
        current_node = queue.pop(0)
        temp = current_node[1]
        current_node_idx = convert_to_idx(current_node[0])
        if (current_node_idx == idx_final):
            break
        for neighbor in adj_list[current_node_idx]:
            # print(queue)
            # print("==================================")
            visited_node = []
            for c in current_node[2]:
                visited_node.append(c)
            i = convert_to_idx(neighbor)
            visited_node.append(neighbor)
            # masukkan node ke queue
            # param: current_node name, f(current_node), visited_node ke queue
            queue.append([neighbor, temp + adj_matrix[current_node_idx][i] + heuristic_matrix[i][idx_final], visited_node])
            
            # prioeity queue
            queue.sort(key = lambda q : q[1])

    # shortest path
    path = current_node[2]
    
    # calculate cost
    cost = 0 
    path_cost = []
    for node in path:
        path_cost.append(convert_to_idx(node))
    for i in range(len(path)-1):
        cost += adj_matrix[path_cost[i]][path_cost[i+1]]
    
    return path, cost

def path_coords(path):
    global list_of_names
    global list_of_coordinates
    global list_of_path_coords
    list_of_path_coords = []
    for node in path[0]:
        list_of_path_coords.append(list_of_coordinates[convert_to_idx(node)])
    return list_of_path_coords

# get string route
def string_route(solution):
    solution_list = []
    for i in range(len(solution[0])):
        if (i == (len(solution[0])-1)):
            solution_list.append(solution[0][i])
        else:
            solution_list.append(solution[0][i]+" -> ")
    solution_list = ' '.join([str(elem) for elem in solution_list])
    return "Lintasan terpendek : " + (solution_list)

# initialize awal
def initialize(file_name):
    # data_folder = "../test/"
    file_to_open = file_name
    f = open(file_to_open, "r")
    lines = f.read().splitlines()
    coordinates = make_coordinates(lines)[0]
    list_lat = make_list_of_lat(coordinates)
    list_lon = make_list_of_lon(coordinates)
    node_names = make_coordinates(lines)[1]
    matrix = make_matrix(lines)
    adj_list = make_adj_list(matrix)
    adj_matrix = make_adj_matrix(matrix)
    heur_matrix = make_heuristic_matrix(matrix)