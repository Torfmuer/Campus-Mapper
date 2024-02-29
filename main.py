import keyboard
from lib.campuspaths import *
from lib.All_Routes import *

# Todo: add consideration for corssing through buildings. can be done with a dictionary stating a given pixel count increase for each building

# display our base map image
DisplayImage("images/campus_map_scaled.png")

# print out the csv with all possible paths

# define the paths to draw
#Paths = LoadPaths(LoadCSV("data/edgelist.csv"))
#Paths = [["Hawthorne hall", "HUB BOP JC", "HUB ARE JC", "EJ sw help", "ROB help east", "Robinson"], ['Graves gym', 'Ballard', 'Chapel', 'CH HWP 1', 'CH HW 1'], ['Weyerhauser', 'HW 3', 'HW 4', 'HW 5', 'HW 6', 'HW 6', 'HW 7', 'HUB', 'HUB BOP JC', 'BOP OUT SIDE', 'Whit Dr Cross', 'Hawth JC', 'Hawthorne hall']]

# draw all calclated path possibilities
def DrawAllDifferentPaths():
    Paths = TestAllPaths()

    # draw all paths
    for path in Paths:
        # draw the same path in new run of TestAStarPath()
        opposite_path = TestAStarPath([name for name in names.values()].index(path[len(path) - 1]) + 1, [name for name in names.values()].index(path[0]) + 1)
        rev_opposite_path = opposite_path.copy()
        rev_opposite_path.reverse()
        # check if we have differing paths
        # if so, display them
        if path != rev_opposite_path:
            DrawPath(opposite_path, ColorKeys["blue"])
            DrawPath(path, ColorKeys["red"])
            keyboard.wait('space')
            ClearBoard()

    print("Done")

# run an input of tests that follow the doubling method and time them
def TimeDoubleMethod():
    paths = [ ["Field house", "Aquatics center"], ["Field house", "HW 1"], ["Field house", "HW 3"], ["Field house", "Dixon hall"]]
    result = TimePaths(paths)

    # scan through results and print path found / time it took
    for i in range(0, len(result[0])):
        DrawPath(result[0][i], "red")
        DrawText(f"Time: {result[1][i] * 1000} ms")

        keyboard.wait('space')
        ClearBoard()

# draw all calculated path possibilities
def DrawAllPaths():
    Paths = TestAllPaths()

    # draw all paths
    for path in Paths:
        # check if we have differing paths
        # if so, display them
        DrawPath(path, ColorKeys["red"])

    print("Done")

# allow the user to enter paths to draw
def UserInteract():
    print(f"Options: {names}")
    print(f"Colors: {ColorNames.values()}")

    # go through every path and draw it in a new color
    while True:
        # gather source of new path
        selectingstart = True
        startpoint = 0
        while selectingstart:
            startpoint = int(input("Select start point: "))
            if startpoint not in range(1, len(names)):
                print(f"{startpoint} is not a valid node")
                continue
            selectingstart = False

        # gather endpoint of new path
        selectingdest = True
        destpoint = 0
        while selectingdest:
            destpoint = int(input("Select destination: "))
            if destpoint not in range(1, len(names)):
                print(f"{destpoint} is not a valid node")
                continue
            selectingdest = False

        # set color of new path
        selectingcolor = True
        color = ""
        while selectingcolor:
            color = input("Select color: ")
            if color[0].upper() + color[1:] not in ColorNames.values():
                print(f"{color} is not a valid color")
                continue
            selectingcolor = False

        DrawPath(TestAStarPath(startpoint, destpoint), ColorKeys[color.lower()])

        # undraw all paths
        print("Press space to clear board, or any other key to continue")
        time.sleep(0.5)
        control = keyboard.read_key()
        if control == 'space':
            ClearBoard()
        elif control == 'q':
            break
        time.sleep(0.3)

# allow the user to enter BFS paths to draw
def UserInteractBFS():
    print(f"Options: {names}")
    print(f"Colors: {ColorNames.values()}")

    # go through every path and draw it in a new color
    while not keyboard.read_key() == 'esc':
        # gather source of new path
        selectingstart = True
        startpoint = 0
        while selectingstart:
            startpoint = int(input("Select start point: "))
            if startpoint not in range(1, len(names)):
                print(f"{startpoint} is not a valid node")
                continue
            selectingstart = False

        # gather endpoint of new path
        selectingdest = True
        destpoint = 0
        while selectingdest:
            destpoint = int(input("Select destination: "))
            if destpoint not in range(1, len(names)):
                print(f"{destpoint} is not a valid node")
                continue
            selectingdest = False

        # set color of new path
        selectingcolor = True
        color = ""
        while selectingcolor:
            color = input("Select color: ")
            if color[0].upper() + color[1:] not in ColorNames.values():
                print(f"{color} is not a valid color")
                continue
            selectingcolor = False

        DrawPath(BFSPathFind(startpoint, destpoint), ColorKeys[color.lower()])

        # undraw all paths
        print("Press backspace to clear board, or any other key to continue")
        time.sleep(0.5)
        if keyboard.read_key() == 'backspace':
            ClearBoard()

# prompts the user on settings for visualizing A* while it draws
def GetVisualizationSettings():
    visualize = input("Would you like the algorithm to visualize its process as the paths draw? ")
    if visualize.lower() == "yes":
        set_astar_draw(True)
        print("Enter # of seconds between each step.")
        set_playspeed(float(input("If you would like to control yourself, enter -1 here and use the space key to step through the process: ")))
    else:
        set_astar_draw(False)

# see what mode user wants to run
selectingmode = True
while selectingmode:
    mode = int(input("1: Draw All Paths | 2: User Interact | 3: User Interact BFS | 4: Test Doubling Method "))
    if mode not in range(1, 5):
        print(f"{mode} is not a valid mode")
        continue
    selectingmode = False

modeswitch = {
    1 : "DrawAll",
    2 : "User",
    3 : "UserBFS",
    4 : "TimeDouble"
}

# run initialization process
global initialized
if not initialized:
    Initialize()

mode_str = modeswitch[mode]
if mode_str == "DrawAll":
    DrawAllPaths()
elif mode_str == "User":
    GetVisualizationSettings()
    UserInteract()
elif mode_str == "UserBFS":
    GetVisualizationSettings()
    UserInteractBFS()
elif mode_str == "TimeDouble":
    TimeDoubleMethod()

# wait until the space again to exit
keyboard.wait('space')

print("Exiting")
