import os
from node import Node
from os import walk
import re


"""
rootNode: The root node of a Node data structure representing a policy

Reads the Node data structure and organizes the desktop according to it
"""
def organizeDesktop(rootNode):

    desktopPath = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') 

    # Organizing all children that are not the desktop node
    for child in Node.getChildren(rootNode):
        organize(child, desktopPath, desktopPath)





  
"""
node: The node to start recursively searching
parentDirectory: The path to the directory that the new folder and all nested ones will be created in

A recrusive function that creates a folder structure on the way down and organizes on the way back up
"""  
def organize(node, parentDirectory, desktopPath):
    # Create new folder for node object
    newDirectoryPath = os.path.join(parentDirectory, node.getName())
    os.mkdir(newDirectoryPath)

    # Search desktop for files that satisfy each accepting regex
    desktopFilenames = next(walk(desktopPath), (None, None, []))[2]  # [] if no file
    for regex in Node.getAcceptedRegexs(node):

        # Moving files to the directory path that match the regex
        for matchedFile in getMatchingStrings(desktopFilenames, regex):
            os.rename(os.path.join(desktopPath, matchedFile), os.path.join(newDirectoryPath, matchedFile))


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

    

