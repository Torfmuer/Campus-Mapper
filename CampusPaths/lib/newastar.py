import math as meth
import json

#this is for our heuristic, which is going to be the euclidean distance
def find_dist(start, end):
    return meth.sqrt((end[0] - start[0])**2 + (end[1] - start[1])**2)

def astar(visited, current_node, moves):
    global UDN
    to_check = nodeChildren[current_node] # uses the dictionary nodeChildren to lookup every child and put it in a list
    if UDN in to_check: # checks if the destination is in the children list
        moves.append(UDN) # if found adds it as the final move
        return moves
    low_cost = meth.inf
    temp_node = "null"
    for i in to_check:
        if i not in visited:
           temp_cost = 0
           temp_cost += find_dist(nodes[current_node],nodes[i])
           temp_cost += find_dist(nodes[i], nodes[UDN])
           if temp_cost < low_cost:
                low_cost = temp_cost
                temp_node = i
    if low_cost == meth.inf:
        moves.pop()
        visited.append(current_node)
        astar(visited, moves[-1], moves)
    visited.append(current_node)
    moves.append(temp_node)
    astar(visited, temp_node, moves)
    return moves


def astarv2(USN,UDN):
    global nodeChildren
    visited = [[USN, 'source']] # format is [name, parent]
    candidates = [[0, USN, "source"]] # format is [node_cost, name, parent]
    while True:
        next = [meth.inf, "wack", "daddy"]
        for candidate in candidates:
            if candidate[0] < next[0]:
                next = candidate
        candidates.remove(next)
        to_calculate = nodeChildren[next[1]]
        low_cost = meth.inf
        for node in to_calculate: #each node is just a name
            if node == UDN:
                visited.append([next[1],next[2]])
                print("yahoo")
                moves = [UDN]
                parent = next[1]
                while parent != USN:
                    moves.append(parent)
                    for name_parent in visited:
                        if name_parent[0] == parent:
                            parent = name_parent[1]
                            break
                moves.append(parent)
                moves.reverse()
                return moves
            if any(node in tuple for tuple in visited) == 0:
                temp_cost = 0
                temp_cost += find_dist(nodes[next[1]], nodes[node])
                temp_cost += find_dist(nodes[node], nodes[UDN])
                candidates.append([temp_cost, node, next[1]])
        visited.append([next[1],next[2]])




#open the file that has the names and locations of the nodes
locationsFileInput = open("locations.txt", "r")
edgesFileInput = open("edgelist.csv", "r")

#nodes is name: coordinate pair
#nodes = {}

with open('locations.txt') as f:
    data = f.read()

    nodes = json.loads(data)

#names is user option : name pair
names = {}

#nodeChildren is node :  list of children pair
nodeChildren = {}

#variables for user start and end
userDestination = 0
userStart = 0

#initialize nodes and names maps from file
#for index, val in enumerate(locationsFileInput):
#    val.strip()
#    data = val.split(",")
#    nodes[data[0]] = (int(data[1]), int(data[2]))
#    names[index + 1] = data[0]
    



#initialize nodes with their children to create edges
for i in edgesFileInput:
    i = i.strip()
    data = i.split(',')
    nodeChildren[data[1]] = []
    for j in range(2, len(data)):
        nodeChildren[data[1]].append(data[j])

#print out the options for the user
choiceNum = 1
print("Please select your starting point ")
for i in nodes:
    names[choiceNum] = i
    if choiceNum - 1 % 5 == 0:
        print()
    print(str(choiceNum) + ": " + str(i) , end = ' ')
    choiceNum += 1

print()
userStart = input("Please select the number that corresponds with your starting point ")
userStart = int(userStart)
userDestination = input("Please select the number that corresponds with your destination ")
userDestination = int(userDestination)


#print(names[userStart])
#print(nodes[names[userStart]])

#print(names[userDestination])
#print(nodes[names[userDestination]])


USN = (names[userStart])
UDN = (names[userDestination])
UST = nodes[USN] # User Start Tuple
UDT = nodes[UDN] # User Destination Tuple


#output = astar(visited,USN,moves)
output = astarv2(USN,UDN)
print("progress")
distance = 0
for i in range(len(output) - 1):
    distance += find_dist(nodes[output[i]], nodes[output[i+1]])
    print(distance)


print(output)
print("You have a distance of %d" % (distance))