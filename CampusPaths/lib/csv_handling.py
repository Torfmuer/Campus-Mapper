__version__ = "1.0"
import csv

# import a csv file and load into a list to use
# takes in string location, returns list of lists for the table
def LoadCSV(filepath):
    with open(filepath, 'r') as csvfile:
        # load the csv from the file defined
        reader = csv.reader(csvfile)
        file_list_form = []
        for elem in reader:
            file_list_form.append(elem)
        return file_list_form

# using the path definition csv layout, create a list of strings of defined paths
def LoadPaths(list):
    paths = []
    for row in list:
        if row:
            # first element in each row is the "home" node
            # each following element is a node connected to that node
            invalidelem = True
            while invalidelem:
                if row[0] == '':
                    row.pop(0)
                else:
                    invalidelem = False
            homenode = row[0]
            row.pop(0)
            for elem in row:
                newpath = [str(homenode), str(elem)]
                if newpath not in paths:
                    paths.append(newpath)

    return paths

# prints the CSV.  used for debuggin purposes
def PrintCSV(filepath):
    csv = LoadCSV(filepath)
    for elem in csv:
        print(elem)