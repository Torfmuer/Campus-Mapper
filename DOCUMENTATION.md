# Documentation for Campus Map Director
By: Adam Cassidy, Atticus Templeton, Jonathan Hamstra, and Owen Foster
## Part 1 - File stack
Main: `main.py`
- Contains functions to calculate and draw most efficient route

`All_Routes.py`
- Contains A* and BFS algorithms along with relevant helper functions

`campusPaths.py`
- Contains dictionaries storing the edge-list graph and XY coordinates of each point of interest on campus
- Contains functions used to draw points and lines on the window

`graphics.py`
- Imported library written by John Zelle
- Generates the graphics used in final representation of program

`csv_handling.py`
- Helper file to construct the dictionaries from imported CSV data

`__init__.py`
- Initialization (empty)

_DEPRICATED:_ `newastar.py`
- Helper file containing A* algorithms that are incorporated into All_Routes.py

## Part 2 - Function Definitions
### `main.py`
_Note that every function in this file takes in no parameters and returns no parameters. The primary result of most of these functions is to display images on the screen and take in user input._

__DrawAllDifferentPaths():__

Displays every pair of paths that an alternate path when reversely calculated.

__TimeDoubleMethod():__

Runs through a set list of example searches to measure the time spent to run them. Prints results to terminal.

__DrawAllPaths():__

Draws all possible paths on campus.

__UserInteract():__

Handles user input to select which search they want to use, beginning and end points, as well as the color of the path to draw. Then draws the path between the two nodes.

__GetVisualizationSettings():__ 

Takes user input to fully customize the display, including draw speed and whether or note to manually iterate throw the drawing or automatically display all paths.

*Starting at line 166, the main line of the program runs, taking in basic user input and subsequently calling all relevant functions.*

## 
### `All_Routes.py`

__set_astar_draw(tf):__ _Takes in tf, which is converted to a boolean._

Sets the global astar_draw to the boolean value of tf, turning the drawing functions on or off.

__set_playspeed(val):__ _Takes in val, a float._

Sets the playback speed to val. 

__find_dist(start, end):__ _Takes in two nodes, start and end._

Calculates and returns the Euclidean distance between both nodes.

__astar(USN, UDN):__ _Takes in two nodes, the node chosen to start from and the node chosen to end at._

Runs A* search algorithm on the entire data set of nodes for Whitworth campus. Returns a list of nodes by which a path can be draw to be the shortest route between the two input points. Will also report the length of this path and the time it would take to walk it. 

*DEPRICATED:* __oldastar(visited, current_node, moves):__ _Takes in a list of nodes, the node currently being accessed, and the moves take prior to arrival at the current node._

Runs A* search algorithm and returns a list of nodes by which the route is shortest. 

__Initialize():__ _No input or output._

Reads in a file to aid in initializing node coordinates, names, and chlidren.

__CalcPathWeight(path):__ _Takes in `path`, a list of nodes._

Calculates and returns the total time needed to traverse the input path.

__BFSPathFind(start_int, end_int):__ _Takes in the index of the starting node and the index of the ending node._

Uses a Breadth-first search to calculate the shortest path between the to input nodes. Returns the list of nodes needed to be traversed in the shortest path, as well as the length of the path and the time needed to walk it. 

__TestAStarPath(user_start, user_dest):__ _Takes in the indices of the start and end nodes_.

Calls astar(USN, UDN) given the two indices the user has input. 

__TestAllPaths():__ _No i/o._

Tests all possible paths between each node to ensure there are no errors in typesetting and positive transitive closure. 

__TimePaths(tests):__ _Takes in tests, a list of paths needed to be timed._

Calculates the time needed to traverse all paths given to it. Returns a list of paths associated with their respective times. 

## 
### `campuspaths.py`

__Dictionary: ColorKeys__

Contains easier to manage names for display colors.

__Dictionary: ColorNames__ 

Renames colors for the image display functions. 

__Dictionary: BuildingWeights__

Contains the default value (20 seconds) needed to be added to the heuristic for accessing a building while traversing campus. 

__Dictionary: ImagePoints__

Contains names of all nodes on campus along with their X and Y image coordinates. These coordinates are needed to calculate heuristic and total distance travelled in a path. Also tells graph functions where to draw each node on the output image.

__Dictionary: DisplayNames__

Cleans up and recasts the names of the nodes to be accurate to their actual names. The names used to assocaite them with their coordinates were shorthand and used significnat amounts of abreviation.  Only includes names of buildings.

__ClearBoard():__ _No i/o._

Clears the current drawing. 

__DrawLine(point1, point2, color, width):__ _Takes in the two points (nodes) to draw between, and the color and width of the line to be drawn._

Draws a line between two nodes.

__DrawText(text):__ _Takes in a string to display._

Called by a DrawLine or DrawPoint function. Displays a string of text at the next available line at the right-hand side.

__DrawPoint(point_obj, num, color):__

Draws a circle at the specified coordinates.

__DrawPath(points, color):__ _Takes in the points the draw between and the color of line to draw._

The main drawing function. Calls DrawLine between every point in the input path and calls DrawText in every major node. All campus buildings are considered to be major nodes. Pathways and junctions are not drawn as points.

__DisplayImage(image_file_location):__ _Takes in file path of the image to display._

Displays the drawn image to the user. The file path is for the background image, then paths and points are drawn over the top. 

## 
### `csv_handling.py`

__LoadCSV(filepath):__ _Takes in string location, returns list of lists for the table._

Loads the csv file from `filepath` into a list of lists. This is for formatting to make creating a dictionary much easier. 

__LoadPaths(list):__ _Takes in the list created in LoadCSV("...")_.

Using the path definition csv layout, creates a list of strings of defined paths.

__PrintCSV(filepath):__ _Takes in filepath to output to._

Trints the CSV. Used for debugging.

## 
### `graphics.py`

This is an original file used to generate graphics in Python, created by John Zelle.

Find the file here: https://mcsp.wartburg.edu/zelle/python/graphics.py

Find the documentation here: https://mcsp.wartburg.edu/zelle/python/graphics/graphics.pdf

