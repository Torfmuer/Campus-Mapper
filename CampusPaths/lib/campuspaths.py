from lib.graphics import *
import time
import keyboard
from lib.csv_handling import *

# dictionary of colors based in a pressed key
ColorKeys = {
    "green" : "spring green",
    "red" : "red",
    "yellow" : "yellow",
    "blue" : "dodger blue",
    "orange" : "orange",
    "purple" : "magenta3"
}
ColorNames = {
    "dodger blue" : "Blue",
    "spring green" : "Green",
    "red" : "Red",
    "yellow" : "Yellow",
    "orange" : "Orange",
    "magenta3" : "Purple",
    "cyan" : "Cyan"
}

# building weights
BuildingWeights = {
    "Default" : 20
}

# dictionary of locations to pixel locations of the graph
ImagePoints = {
    "Chapel" : [520, 324],
    "Dixon hall" : [594, 233],
    "Cowles music" : [541, 174],
    "Robinson" : [665, 430],
    "Cowles aud" : [609, 184],
    "Weyerhauser" : [558, 405],
    "McEachran hall" : [654, 191],
    "URec" : [517, 560],
    "MacKay hall" : [654, 190],
    "Auld house" : [520, 116],
    "President's house" : [811, 75],
    "Pine Bowl" : [429, 264],
    "Hardwick house" : [874, 152],
    "WALT" : [364, 406],
    "The Pines" : [969, 173],
    "Hawthorne hall" : [985, 215],
    "HUB" : [780, 281],
    "EJ" : [740, 400],
    "Library" : [672, 344],
    "Hendrick hall" : [779, 380],
    "Lindaman center" : [603, 367],
    "Graves gym" : [421, 366],
    "Baseball/Soccer fields" : [315, 286],
    "Omache field" : [365, 210],
    "Field house" : [350, 480],
    "Aquatics center" : [387, 502],
    "Merkel field" : [170, 636],
    "Westminster hall" : [508, 485],
    "Art building" : [564, 498],
    "Dornsife" : [638, 525],
    "Steam plant" : [678, 494],
    "The Village" : [862, 439],
    "Boppell hall" : [912, 332],
    "Duvall hall" : [960, 390],
    "Oliver hall" : [930, 465],
    "BJ hall" : [794, 478],
    "Stewart hall" : [821, 418],
    "Arend hall" : [775, 343],
    "Warren hall" : [548, 263],
    "Macmillan" : [493, 390],
    "Ballard" : [480, 340],
    "WH HWP 1" : [566, 288],
    "CH HWP 1" : [530, 310],
    "DIX HWP 1" : [598, 260],
    "DIX HWP 2" : [635, 232],
    "DIX HWP 3" : [651, 221],
    "HW 7" : [704, 276],
    "HW 6" : [671, 295],
    "HW 5" : [640, 318],
    "HW 4" : [592, 355],
    "HW 3" : [548, 388],
    "HW 2" : [526, 404],
    "HW 1" : [471, 444],
    "CH HW 1" : [553, 344],
    "ROB help west" : [635, 409],
    "ROB help east" : [701, 409],
    "DORN south street help" : [626, 482],
    "EJ sw help" : [705, 370],
    "Health center" : [602, 450],
    "HUB BOP JC" : [821, 325],
    "HUB ARE JC" : [751, 325],
    "HUB LIB JC" : [707, 322],
    "BOP OUT" : [894, 351],
    "DUV OUT" : [930, 390],
    "OLI OUT" : [914, 449],
    "VIL OUT" : [856, 469],
    "STE OUT" : [851, 390],
    "ARE STE JC" : [825, 366],
    "Whit Dr Cross" : [900, 250],
    "BOP OUT SIDE" : [884, 298],
    "Hawth JC" : [964, 210],
    "DRW OUT" : [702, 149],
    "Security Office" : [848, 99],
    "Track helper" : [388, 318],
    "BJ EJ JC" : [727, 427],
    "Stew west" : [795, 419],
    "EJ ARE JC" : [749, 374]
}

# stores display names of given nodes
# not all nodes will have display names.  if a chosen node doesn't have a display name,
# then a circle will not be displayed on it but the path through will still be visible
DisplayNames = {
    "Chapel" : "Seeley G. Mudd Chapel",
    "Dixon hall" : "Dixon Hall",
    "Cowles music" : "Cowles Music Center",
    "Robinson" : "Robinson Science Hall",
    "Cowles aud" : "Cowles Memorial Auditorium",
    "Weyerhauser" : "Weyerhauser Hall",
    "McEachran hall" : "McEachran Hall",
    "Urec" : "U-Rec",
    "MacKay hall" : "MacKay Hall",
    "Auld house" : "Auld House",
    "President's house" : "President's House",
    "Pine Bowl" : "Pine Bowl",
    "Hardwick house" : "Hardwick House",
    "WALT" : "WALT Center",
    "The Pines" : "The Pines Cafe / Campus Store",
    "Hawthorne hall" : "Hawthorne Hall",
    "HUB" : "The Hub",
    "EJ" : "Eric Johnston Science Center",
    "Library" : "H.C. Cowles Memorial Library",
    "Hendrick hall" : "Hendrick Hall",
    "Lindaman center" : "Lindaman Center",
    "Graves gym" : "Graves Gym",
    "Tennis courts behind graves" : "Graves Tennis Courts",
    "Baseball / Soccer fields" : "Marks / Soccer Fields",
    "Omache field" : "Omache Field",
    "Field house" : "Fieldhouse",
    "Aquatics center" : "Megan E. Thompson Aquatic Center",
    "Merkel field" : "Merkel Field",
    "Westminster hall" : "Westminster Hall",
    "Art building" : "Lied Center for the Visual Arts",
    "Dornsife" : "Dornsife Health Sciences Building",
    "Facilities services" : "Facilities Services",
    "The Village" : "The Village (Akili, Tiki, Shalom)",
    "Boppell hall" : "Boppel Hall",
    "Duvall hall" : "Duvall Hall",
    "Oliver hall" : "Oliver Hall",
    "BJ hall" : "Baldwin-Jenkins Hall",
    "Stewart hall" : "Stewart Hall",
    "Arend hall" : "Arend Hall",
    "Warren hall" : "Warren Hall",
    "Macmillan" : "McMillan Hall",
    "Ballard" : "Ballard Hall",
    "Health center" : "Schumacher Hall - Health Center",
    "Steam plant" : "Steam Plant"
}

# set up our window
window_width = 1350
window_height = 650
win = GraphWin('Campus Paths', window_width, window_height)
win.setCoords(0, 0, window_width, window_height)

# keeps track of where the furthest down text is on the right hand column
text_column_height = 0

# stores current drawn elements, allowing us to erase them later
CurDrawn = []

# clear all drawn elements
def ClearBoard():
    for elem in CurDrawn:
        elem.undraw()
    global text_column_height
    text_column_height = 0

# draws a line between two defined nodes
def DrawLine(point1, point2, color, width):
    # draw the line between the two points using their respective coordinates
    line = Line(point1, point2)
    line.setOutline(color)
    line.setWidth(width)
    line.draw(win)

    # add all drawn objects to the CurDrawn list
    global CurDrawn
    CurDrawn.append(line)

# draws text on the next available space in the side column
def DrawText(text):
    # scale the text column height to avoid overwriting text
    global text_column_height
    text_column_height += 15

    # write the text in our list for this endpoint
    endpointtext = Text(Point(win.getWidth() - 125, win.getHeight() - text_column_height), text)
    endpointtext.setSize(10)
    endpointtext.draw(win)

    # add all drawn objects to the CurDrawn list
    global CurDrawn
    CurDrawn.append(endpointtext)

# draws a circle at specified coordinates
def DrawPoint(point_obj, num, color):
    # draw circle to represent this point
    drawpoint = Circle(point_obj, 8)
    drawpoint.setFill(color)
    drawpoint.draw(win)

    # draw the number for this point
    pointnum = Text(drawpoint.getCenter(), str(num))
    pointnum.setSize(10)
    pointnum.draw(win)

    # add all drawn objects to the CurDrawn list
    global CurDrawn
    CurDrawn.append(drawpoint)
    CurDrawn.append(pointnum)

# draws a path between two nodes
def DrawPath(points, color):
    # various tracker / helper vars for drawing a path
    prev_point = None
    prevpointname = None
    pointcount = 1
    prevpointdrawn = False

    # create a line to separate from paths before it
    DrawText(f"---------------{ColorNames[color]}---------------")

    # run through the points and build the path
    for point in points:
        # convert to point objects for the graphics library
        # if exception caught, this is an invalid point.  report the point and stop drawing this point
        try:
            draw_point = Point(ImagePoints[point][0], ImagePoints[point][1])
        except:
            break

        # if the previous point is defined, draw a line
        if prev_point != None:
            # draw line between last and current point
            DrawLine(prev_point, draw_point, color, 3)

            # draw the point before this one in the line if needed to avoid covering a node
            if prevpointdrawn:
                DrawPoint(prev_point, pointcount - 1, color)

        # reset our prevpointdrawn flag
        prevpointdrawn = False

        if point in DisplayNames:
            # draw this point if it is a main node
            if pointcount > 1:
                DrawPoint(draw_point, pointcount, color)
            else:
                DrawPoint(draw_point, "", color)

            DrawText(f"{pointcount} : {DisplayNames[point]}")

            # increase the counter for main nodes we have passed through
            pointcount += 1

            prevpointdrawn = True
        elif pointcount == 1:
            # draw this point if it is a main node
            DrawPoint(draw_point, "", color)

            DrawText(f"{pointcount} : {point}")

            # increase the counter for main nodes we have passed through
            pointcount += 1

            prevpointdrawn = True

        prev_point = draw_point
        prevpointname = point

# displays an image on the window
def DisplayImage(image_file_location):
    map_image = Image(Point(0, 0), image_file_location)
    x_location = (win.getWidth() / 2) - ((win.getWidth() - map_image.getWidth()) / 2)
    y_location = (win.getHeight() / 2) - ((win.getHeight() - map_image.getHeight()) / 2)

    map_image_draw = Image(Point(x_location, y_location), image_file_location)
    map_image_draw.draw(win)

