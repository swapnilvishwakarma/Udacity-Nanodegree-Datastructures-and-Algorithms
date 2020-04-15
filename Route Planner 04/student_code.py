from helpers import Map, load_map, show_map
import math
import heapq as h

map_10 = load_map('map-10.pickle')
map_40 = load_map('map-40.pickle')

def shortest_path(M,start,goal):
    #used pseudo code from wikipedia. https://en.wikipedia.org/wiki/A*_search_algorithm
    ## f = g + h where g is the path cost and h is the estimated distance from the node to the goal 
    closedSet = set([])
    
    openSet = set([start])
    
    cameFrom = {}
    
    availableroads  = list(M.intersections.keys())
    
    gScore = {road : float("inf") for road in availableroads}
        
    gScore[start] = 0
    
    fScore = {road: float("inf") for road in availableroads}
        
    fScore[start] = heuristic(M,start,goal)
    
    frontier = [(fScore[start], start)]
    
    while openSet:
        current = h.heappop(frontier)
        
        #current = fScorel[0][1]
        #current = min(openSet, key = lambda node: fScore[node])

        if current[1] == goal:
            print("shortest path called")
            reversepath = reconstruct_path(cameFrom, current[1])
            reversepath.reverse()
            print(reversepath)
            return reversepath
        
        if current[1] in openSet:    
            openSet.remove(current[1])
            closedSet.add(current[1])
        
        for i in M.roads[current[1]]:
            if i in closedSet:
                continue
                
            if i not in openSet:
                openSet.add(i)
            
            tentative_gScore = gScore[current[1]] + heuristic(M, current[1], i)
            if tentative_gScore >= gScore[i]:
                continue
                
            cameFrom[i] = current[1]
            gScore[i] = tentative_gScore
            fScore[i] = (gScore[i] + heuristic(M, i, goal))
            h.heappush(frontier, (fScore[i], i))
       
    return ("Failed function")

def heuristic(M, startnode, endnode):
    abs_diff_x_square = math.pow((M.intersections[startnode][0] - M.intersections[endnode][0]),2)
    abs_diff_y_square = math.pow((M.intersections[startnode][1] - M.intersections[endnode][1]),2) 
    distance_bet_nodes = math.sqrt(abs_diff_x_square + abs_diff_y_square)
    return distance_bet_nodes

def reconstruct_path(cameFrom, current):
    path = []
    total_path = [current]
    while current in cameFrom:
        current = cameFrom[current]
        total_path.append(current)     
    return total_path