
import node
import sys
import organizer

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
rootNode = parser.Parse(data)


"""
Organize desktop using node structure
"""
organizer.organizeDesktop(rootNode)



