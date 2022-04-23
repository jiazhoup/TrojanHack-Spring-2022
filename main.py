
import sys
import organizer
import node_parser

fileName = sys.argv[1]

"""
Read policy file, convert to string
"""
data = None
try:
    with open(fileName, 'r') as f:
        data = f.read().rstrip()
except FileNotFoundError:
    print("FILE NOT FOUNND!!!!")
    quit()

"""
Use parser to create node structure
"""
rootNode = node_parser.parse(data)


"""
Organize desktop using node structure
"""
organizer.organizeDesktop(rootNode)


