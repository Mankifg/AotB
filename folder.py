import os

onlyfiles = []
everything = []

pathToItems = os.path.abspath(os.getcwd()) 
pathToItems = pathToItems + "/NotEnoughUpdates-REPO/items"


for path in os.listdir(pathToItems):
    # check if current path is a file
    if os.path.isfile(os.path.join(pathToItems, path)):
        onlyfiles.append(path)
        
print(onlyfiles)

