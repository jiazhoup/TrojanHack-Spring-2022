import os
import node


"""
rootNode: The root node of a Node data structure representing a policy

Reads the Node data structure and organizes the desktop according to it
"""
def organizeDesktop(rootNode):
    return





  
"""
node: The node to start recursively searching
parentDirectory: The path to the directory that the new folder and all nested ones will be created in

A recrusive function that creates a folder structure on the way down and organizes on the way back up
"""  
def organize(node, parentDirectory):
    newDirectoryPath = parentDirectory + "/" + node.getName()
    os.mkdir(newDirectoryPath)

    for regex in node.:

    for child in node.getChildren():
        organize(child, newDirectoryPath)


    

