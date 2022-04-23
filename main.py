"""
idk
"""

import node
import sys

fileName = sys.argv[1]

"""
 Read policy file, convert to string
"""
try:
    with open(fileName, 'r') as f:
        data = f.read().rstrip()
except FileNotFoundError:
    print("FILE NOT FOUNND!!!!")
    pass



"""
parser
"""




