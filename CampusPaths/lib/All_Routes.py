import math as meth
import json
import time

from lib.campuspaths import *

#names is user option : name pair
names = {}

# holds location data
nodes = {}

#nodeChildren is node :  list of children pair
nodeChildren = {}

# tells our path finding function whether or not we have initialized our data
initialized = False

# tells astar whether or not to draw as we go
astar_draw = False
playspeed = 0.5

# helper functions
def set_astar_draw(tf):
    global astar_draw
    astar_draw = bool(tf)

def set_playspeed(val):
    global playspeed
    playspeed = float(val)

#this is for our heuristic, which is going to be the euclidean distance
def find_dist(start, end):
    return meth.sqrt((end[0] - start[0])**2 + (end[1] - start[1])**2)

# main method to run astar
def astar(USN, UDN):
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
                moves = [UDN]
                parent = next[1]
                while parent != USN:
                    moves.append(parent)
                    if astar_draw:
                        DrawPath([elem for elem in moves], ColorKeys["purple"])
                        if playspeed == -1:
                            keyboard.wait('space')
                        else:
                            time.sleep(playspeed)
                    for name_parent in visited:
                        if name_parent[0] == parent:
                            parent = name_parent[1]
                            break
                moves.append(parent)
                if astar_draw:
                    DrawPath([elem for elem in moves], ColorKeys["purple"])
                    if playspeed == -1:
                        keyboard.wait('space')
                    else:
                        time.sleep(playspeed)
                    ClearBoard()
                moves.reverse()
                if astar_draw:
                    DrawPath([elem for elem in moves], ColorKeys["green"])
                    if playspeed == -1:
                        keyboard.wait('space')
                    else:
                        time.sleep(playspeed)
                    ClearBoard()
                # report the length of this path
                DrawText(f"Time for this path: {CalcPathWeight(moves)}")
                return moves

            if any(node in tuple for tuple in visited) == 0:
                temp_cost = 0
                temp_cost += find_dist(nodes[next[1]], nodes[node])
                temp_cost += find_dist(nodes[node], nodes[UDN])
                if node in DisplayNames:
                    temp_cost += 200
                candidates.append([temp_cost, node, next[1]])
        ClearBoard()
        visited.append([next[1],next[2]])
        if astar_draw:
            for elem in visited:
                DrawPath([str(elem[0])], ColorKeys["red"])
            for elem in candidates:
                DrawPath([elem[1]], ColorKeys["blue"])
            if playspeed == -1:
                keyboard.wait('space')
            else:
                time.sleep(playspeed)

def oldastar(visited, current_node, moves):
    global UDN
    to_check = nodeChildren[current_node]
    if UDN in to_check:
        moves.append(UDN)
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
        return moves
    else:
        visited.append(current_node)
        moves.append(temp_node)
        astar(visited, temp_node, moves)
        return moves

def Initialize():
    #open the file that has the names and locations of the nodes
    edgesFileInput = open("./data/edgelist.csv", "r")

    #nodes is name: coordinate pair
    #nodes = {}

    global nodes
    nodes = ImagePoints.copy()

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

    choiceNum = 1
    for i in nodes:
        names[choiceNum] = i
        choiceNum += 1

def CalcPathWeight(path):
    # calculate the distance between each node and succeeding node, add to a path weight
    weight = 0.0
    time = 0.0
    prev_node = None
    for elem in path:
        if prev_node != None:
            weight += find_dist(ImagePoints[prev_node], nodes[elem])
        # if this is a building node, add some extra weight for traversal through doors and the building
        if elem in DisplayNames:
            time += BuildingWeights["Default"]
        prev_node = elem

    # convert weight in pixels to feet
    # calculated based on coordinates and pixels
    feetperpixel = 3.94

    # calculate time based on walking speed
    # default walking speed 5 ft/s
    time += int((weight * feetperpixel) / 5)
    minutes = int(time / 60)
    seconds = time % 60

    return f"{minutes} : {seconds}"

def BFSPathFind(start_int, end_int):
    # initialize if we haven't yet
    global initialized
    if not initialized:
        Initialize()
        initialized = True

    # convert passed in ints to their proper names
    start = names[start_int]
    end = names[end_int]

    # run a shortest-path BFS to find a path
    # create the queue
    visit_queue = []
    # add the source node to the Queue
    visit_queue.append(start)
    # used to store the parents of a node
    parents = {}

    # while the queue is not empty
    while not len(visit_queue) == 0:
        # grab next node in the queue
        curnode = visit_queue.pop(0)

        # see if we reached the end.  if so, return list of shortest path here
        if curnode == end:
            # scan through this node's parents and parent's parents until first node is reached
            # by choosing the first listed parent for this node we guarantee the shortest path
            parent = parents[curnode][0]
            path = [curnode, parent]
            if astar_draw:
                DrawPath([elem for elem in path], ColorKeys["purple"])
                if playspeed == -1:
                    keyboard.wait('space')
                else:
                    time.sleep(playspeed)
            while parent != start:
                parent = parents[parent][0]
                path.append(parent)
                if astar_draw:
                    DrawPath([elem for elem in path], ColorKeys["purple"])
                    if playspeed == -1:
                        keyboard.wait('space')
                    else:
                        time.sleep(playspeed)

            path.reverse()
            if astar_draw:
                DrawPath([elem for elem in path], ColorKeys["green"])
                if playspeed == -1:
                    keyboard.wait('space')
                else:
                    time.sleep(playspeed)
                ClearBoard()

            # report the length of this path
            DrawText(f"Time for this path: {CalcPathWeight(path)}")
            return path
        ClearBoard()
        # add all child nodes of this node to the queue
        # update the parents array for this node
        for child in nodeChildren[curnode]:
            if child not in visit_queue:
                if child == end:
                    visit_queue = []
                visit_queue.append(child)
            if child not in parents:
                parents[child] = [curnode]
            else:
                parents[child].append(curnode)

        if astar_draw:
            # draw the nodes with defined parents as blue
            for elem in parents:
                DrawPath([elem], ColorKeys["blue"])
            # draw the visit queue as red
            for elem in visit_queue:
                DrawPath([elem], ColorKeys["red"])
            if playspeed == -1:
                keyboard.wait('space')
            else:
                time.sleep(playspeed)

    DrawText("No path found.")
    return -1

def TestAStarPath(user_start, user_dest):
    # initialize if we haven't yet
    global initialized
    if not initialized:
        Initialize()
        initialized = True

    global UDN
    if type(user_start) == int:
        USN = (names[user_start])
    else:
        USN = (user_start)
    if type(user_dest) == int:
        UDN = (names[user_dest])
    else:
        UDN = user_dest

    print("%s to %s" % (USN, UDN))
    UST = nodes[USN] # User Start Tuple
    UDT = nodes[UDN] # User Destination Tuple

    visited = []
    moves = [USN]
    return astar(USN, UDN)

def TestAllPaths():
    all_paths = []
    for i in range(1,76):
        for j in range(i, 76):
            if i == j:
                print("length of 0, dumbass")
            else:
                all_paths.append(TestAStarPath(i, j))
                all_paths.append(TestAStarPath(j, i))

    return all_paths

# run doubling method for testing purposes
def TimePaths(tests):
    global initialized
    if not initialized:
        Initialize()
    # paths is in format [[start, end], ...]
    # time amounts
    times = []
    paths = []
    # call bogus fist AStar to initialize stuff, timing is being weird
    bogus = TestAStarPath("Field house", "Hawthorne hall")
    # run each path.  time it and record time it took
    for test in tests:
        # start timer
        starttime = time.perf_counter()
        # run test with astar
        result = TestAStarPath(test[0], test[1])
        # stop timer
        endtime = time.perf_counter()
        # append result
        paths.append(result)
        # report found path and time
        times.append(endtime - starttime)

    return [paths, times]
