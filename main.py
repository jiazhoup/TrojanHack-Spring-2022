
import sys
from unittest.mock import DEFAULT
import organizer
import node_parser
import tokenizer

DEFAULT_POLICY_PATH = "default_policy"

fileName = sys.argv[1]

if fileName == None:
    fileName = DEFAULT_POLICY_PATH

"""
Read policy file, convert to string
"""
data = None
try:
    with open(fileName, 'r') as f:
        data = f.read().rstrip()
except FileNotFoundError:
    print("Error. File not found.")
    quit()

"""
Use parser to create node structure
"""
rootNode = node_parser.tokensToNode(tokenizer.tokenize(data));

"""
Organize desktop using node structure
"""
organizer.organizeDesktop(rootNode)



