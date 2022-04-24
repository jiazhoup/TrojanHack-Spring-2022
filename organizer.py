import os
from node import Node
from os import walk
import re


OUTPUT_LOG_PATH = "output_log.txt"

"""
rootNode: The root node of a Node data structure representing a policy

Reads the Node data structure and organizes the desktop according to it
"""
def organizeDesktop(rootNode):
    desktopPath = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') 

    moveHistory = [] # List of 2-tuples of previous path string and new path string

    # Organizing all children that are not the desktop node
    for child in Node.getChildren(rootNode):
        organize(child, desktopPath, desktopPath, moveHistory)

    # Outputting all moves to an output.log file
    output_str = ""
    for move in moveHistory:
        output_str += "Moved from: " + move[0] + " to " + move[1] + "\n"

    # Saving output.log file to desktop
    output_path = os.path.join(desktopPath, OUTPUT_LOG_PATH)
    output_file = open(output_path, "w")
    output_file.write(output_str)
    output_file.close()

    print("Move log outputted to " + output_path)

  
"""
node: The node to start recursively searching
parentDirectory: The path to the directory that the new folder and all nested ones will be created in

A recrusive function that creates a folder structure on the way down and organizes on the way back up
"""  
def organize(node, parentDirectory, desktopPath, moveHistory):
    # Create new folder for node object
    newDirectoryPath = os.path.join(parentDirectory, node.getName())

    if not os.path.exists(newDirectoryPath):
        os.mkdir(newDirectoryPath)

    # Search desktop for files that satisfy each accepting regex
    desktopFilenames = next(walk(desktopPath), (None, None, []))[2]  # [] if no file
    for regex in Node.getAcceptedRegexs(node):

        # Moving files to the directory path that match the regex
        for matchedFile in getMatchingStrings(desktopFilenames, regex):
            previousPath = os.path.join(desktopPath, matchedFile)
            newPath = os.path.join(newDirectoryPath, matchedFile)
            os.rename(previousPath, newPath)

            # Log the move
            moveHistory.append((previousPath, newPath))



    # Recursively organize all children folders
    for child in Node.getChildren(node):
        organize(child, newDirectoryPath, desktopPath)


"""
Returns the subset of the list of strings that match the regex
"""
def getMatchingStrings(listOfStrings, regex):
    out = []
    for string in listOfStrings:
        if re.match(regex, string):
            out.append(string)
    return out

    

