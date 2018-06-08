import sys
import random
import string
import timeit   #library that calulcates runtime
import time
import pdb

#creates a randomly generated number or character
def rando_gen(size = 1, chars = string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for x in range (size))

def dj(graph, source, dest, visited = [], distances = {}, predecessors = {}):
    #calculates a shortest path tree in src
       
    # check-up time!
    if source not in graph:
        raise TypeError('The root cannot be found')
    if dest not in graph:
        raise TypeError('The destination cannot be found')    
    # ending: dest == found
    if source == dest:
        # We build the shortest path and display it
        path = []
        prev = dest
        while prev != None:
            path.append(prev)
            prev = predecessors.get(prev, None)
            
        #prints distance and creates the key
        print('shortest path: '+ str(path)+" cost = "+str(distances[dest]))
        print(''.join(path))
    else :     
        # if the node isn't visited in the first go-around, the cost is initialized
        if not visited: 
            distances[source] = 0
        # visit the neighbors
        for neighbor in graph[source]:
            if neighbor not in visited:
                new_distance = distances[source] + graph[source][neighbor]
                if new_distance < distances.get(neighbor, float('inf')):
                    distances[neighbor] = new_distance
                    predecessors[neighbor] = source
                                       
        # mark as visited
        visited.append(source)
        # now that we've said hi to all the neighbors: go around again! (recursion)                         
        # select the non-visited node with lowest distance 'd'
        # run dj (short for dijkstra) with source = 'd'
        notvisited = {}
        for i in graph:
            if i not in visited:
                notvisited[i] = distances.get(i, float('inf'))
                             
        d = min(notvisited, key = notvisited.get)
        dj(graph, d, dest, visited, distances, predecessors)
        


if __name__ == "__main__":
    
    
    #graph of characters a-z, A-Z, 0-9
    #random vertices with random weighted edges between 0-9 are attached to each key
    graph2 = {'A': {rando_gen(): random.randint(1,9), rando_gen(): random.randint(1,9)},
             'B': {rando_gen(): random.randint(1,9), rando_gen(): random.randint(1,9)},
             'C': {rando_gen(): random.randint(1,9), rando_gen(): random.randint(1,9)},
             'D': {rando_gen(): random.randint(1,9), rando_gen(): random.randint(1,9)},
             'E': {rando_gen(): random.randint(1,9), rando_gen(): random.randint(1,9)},
             'F': {rando_gen(): random.randint(1,9), rando_gen(): random.randint(1,9)},
             'G': {rando_gen(): random.randint(1,9), rando_gen(): random.randint(1,9)},
             'H': {rando_gen(): random.randint(1,9), rando_gen(): random.randint(1,9)},
             'I': {rando_gen(): random.randint(1,9), rando_gen(): random.randint(1,9)},
             'J':{rando_gen(): random.randint(1,9), rando_gen(): random.randint(1,9)},
             'K':{rando_gen(): random.randint(1,9), rando_gen(): random.randint(1,9)},
             'L':{rando_gen(): random.randint(1,9), rando_gen(): random.randint(1,9)},
             'M':{rando_gen(): random.randint(1,9), rando_gen(): random.randint(1,9)},
             'N':{rando_gen(): random.randint(1,9), rando_gen(): random.randint(1,9)},
             'O':{rando_gen(): random.randint(1,9), rando_gen(): random.randint(1,9)},
             'P':{rando_gen(): random.randint(1,9), rando_gen(): random.randint(1,9)},
             'Q':{rando_gen(): random.randint(1,9), rando_gen(): random.randint(1,9)},
             'R':{rando_gen(): random.randint(1,9), rando_gen(): random.randint(1,9)},
             'S':{rando_gen(): random.randint(1,9), rando_gen(): random.randint(1,9)},
             'T':{rando_gen(): random.randint(1,9), rando_gen(): random.randint(1,9)},
             'U':{rando_gen(): random.randint(1,9), rando_gen(): random.randint(1,9)},
             'V':{rando_gen(): random.randint(1,9), rando_gen(): random.randint(1,9)},
             'W':{rando_gen(): random.randint(1,9), rando_gen(): random.randint(1,9)},
             'X':{rando_gen(): random.randint(1,9), rando_gen(): random.randint(1,9)},
             'Y':{rando_gen(): random.randint(1,9), rando_gen(): random.randint(1,9)},
             'Z':{rando_gen(): random.randint(1,9), rando_gen(): random.randint(1,9)},
             'a':{rando_gen(): random.randint(1,9), rando_gen(): random.randint(1,9)},
             'b':{rando_gen(): random.randint(1,9), rando_gen(): random.randint(1,9)},
             'c':{rando_gen(): random.randint(1,9), rando_gen(): random.randint(1,9)},
             'd':{rando_gen(): random.randint(1,9), rando_gen(): random.randint(1,9)},
             'e':{rando_gen(): random.randint(1,9), rando_gen(): random.randint(1,9)},
             'f':{rando_gen(): random.randint(1,9), rando_gen(): random.randint(1,9)},
             'g':{rando_gen(): random.randint(1,9), rando_gen(): random.randint(1,9)},
             'h':{rando_gen(): random.randint(1,9), rando_gen(): random.randint(1,9)},
             'i':{rando_gen(): random.randint(1,9), rando_gen(): random.randint(1,9)},
             'j':{rando_gen(): random.randint(1,9), rando_gen(): random.randint(1,9)},
             'k':{rando_gen(): random.randint(1,9), rando_gen(): random.randint(1,9)},
             'l':{rando_gen(): random.randint(1,9), rando_gen(): random.randint(1,9)},
             'm':{rando_gen(): random.randint(1,9), rando_gen(): random.randint(1,9)},
             'n':{rando_gen(): random.randint(1,9), rando_gen(): random.randint(1,9)},
             'o':{rando_gen(): random.randint(1,9), rando_gen(): random.randint(1,9)},
             'p':{rando_gen(): random.randint(1,9), rando_gen(): random.randint(1,9)},
             'q':{rando_gen(): random.randint(1,9), rando_gen(): random.randint(1,9)},
             'r':{rando_gen(): random.randint(1,9), rando_gen(): random.randint(1,9)},
             's':{rando_gen(): random.randint(1,9), rando_gen(): random.randint(1,9)},
             't':{rando_gen(): random.randint(1,9), rando_gen(): random.randint(1,9)},
             'u':{rando_gen(): random.randint(1,9), rando_gen(): random.randint(1,9)},
             'v':{rando_gen(): random.randint(1,9), rando_gen(): random.randint(1,9)},
             'w':{rando_gen(): random.randint(1,9), rando_gen(): random.randint(1,9)},
             'x':{rando_gen(): random.randint(1,9), rando_gen(): random.randint(1,9)},
             'y':{rando_gen(): random.randint(1,9), rando_gen(): random.randint(1,9)},
             'z':{rando_gen(): random.randint(1,9), rando_gen(): random.randint(1,9)},
             '0':{rando_gen(): random.randint(1,9), rando_gen(): random.randint(1,9)},
             '1':{rando_gen(): random.randint(1,9), rando_gen(): random.randint(1,9)},
             '2':{rando_gen(): random.randint(1,9), rando_gen(): random.randint(1,9)},
             '3':{rando_gen(): random.randint(1,9), rando_gen(): random.randint(1,9)},
             '4':{rando_gen(): random.randint(1,9), rando_gen(): random.randint(1,9)},
             '5':{rando_gen(): random.randint(1,9), rando_gen(): random.randint(1,9)},
             '6':{rando_gen(): random.randint(1,9), rando_gen(): random.randint(1,9)},
             '7':{rando_gen(): random.randint(1,9), rando_gen(): random.randint(1,9)},
             '8':{rando_gen(): random.randint(1,9), rando_gen(): random.randint(1,9)},
             '9':{rando_gen(): random.randint(1,9), rando_gen(): random.randint(1,9)}
         }

    #print (graph2.keys())
    start = time.time()
    dj(graph2, rando_gen(), rando_gen())
    stop = time.time()

    

    print 'Dijkstra:', stop - start

    graphSize = sys.getsizeof(graph2)
    print 'The size of the graph is:', graphSize, "bytes"
