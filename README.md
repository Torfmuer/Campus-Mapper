# Campus Map Director (CMD) 
By: Adam Cassidy, Atticus Templeton, Jonathan Hamstra, and Owen Foster

## Purpose and Goals
The primary goal of Campus Map Director is to present to a user the shortest and most efficient route between two buildings on Whitworth Campus. In order to accomplish this, Campus Map Director uses an A* search algorithm to traverse a graph of vertices in edge-list format to find the shortest path between two vertices. 

## How to run Campus Map Director

### What is A*?
A* is a search algorithm derived from Dijkstra's algorithm. The main mechanism is the same as Dijkstra's, but What sets A* apart is that it factors in a hueristic when traversing graph and calculating shortest distances. When this hueristic is 0, A* is functionally equivalent to Dijkstra's, however in the A* algorithm used by CMD, the heuristic is the Euclidean distance between each vertex. 

## Assumptions Made:
Campus Map Director is very easy to use. CMD outputs a key with which numbers correspond to which buildings, then asks for the user the number of where they want to start and end. This should be very accessible to anyone. 

Assumptions are also made that the user knows where they are on campus, as well as can navigate the output map. 

## A* Algorithm Psuedocode

Psuedocode for astar_v2

Pass in the string name of start node and end node

Visited <--- starting node data (name, parent)

candidates <--- first candidate, namely the starting node (node_cost, name, parent)

start infinite loop
    initialize next node as weight infinity
    
    find candidate node that is the cheapest node_cost
    remove the newly found candidate node from the list

    create a list with every child of the new node to be checked
    if it is the goal jump to FINISH code
    
    loop through every child node, checking for if it is the goal first,
    then calculate the G cost (path length plus added distance between previous node and this new node)
    then add the H cost
    (H cost is euclidian distance from node to goal)

    take this G + H value and append all the new info to the candidates list
		(the node weight, name of node, name of parent)

finally append the (node, parent) pair to the visited list now that it has been calculated

FINISH
    once we find the goal node, add the final connection to the visited list
    now create a moves list that holds the sequential order of each step in the path
    add the goal to it
    now take the parent node of this junction, and find the pair in visited where it
    is the main node

    then add that node to the moves list, and take it's parent as the new parent variable

    repeat until you have found the starting node
    reverse the order of the list and return it
    
## A* Analysis 
    When analyzing for our worst case, our research indicated that the worst case for
    A* is the exact same as the worst case for Dijkstra's algorithm. This research and 
    our own analysis showed us that the worst case is O((V+E)logV), where V is number of vertices
    and E is number of edges. This means that for the graph we created, the worst case is
    about 200log75.

    When using the doubling method, we tested using our algorithm a little differently. To double
    things, we ran the search algorithm between nodes that were 1 step away, 2 steps away, 4 steps away,
    and 8 steps away. We would have done 16 away as well, but no nodes in our graph were that far from
    each other.

    Our data is as follows:
    1 step: .42 ms
    2 steps: .81 ms
    4 steps: .92 ms
    8 steps: 1.10 ms

    We created a regression, and saw that this data follows the equation y = 0.2745log(V).
    This indicates that since E + V is about 200 in our graph, and 200 / .2745 = 728, that our
    algorithm in practice is about 728 times faster than the worst case. This indicates that
    our heuristic did well, because a bad heuristic will make A* decompose to Dijkstra's algorithm.

## File Directory and Documentation
To find the grading rubric and instructions go to CampusPaths\final-project.

To see full documentation of all included files and functions, please see DOCUMENTATION.md in the main repository.

## Works Cited
We used graphics.py by John Zelle.

Find the file here: https://mcsp.wartburg.edu/zelle/python/graphics.py

Find the documentation here: https://mcsp.wartburg.edu/zelle/python/graphics/graphics.pdf

    



