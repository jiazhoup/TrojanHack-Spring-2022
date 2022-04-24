import node_parser
import debugUtils
import tokenizer

file_object = open("policy.txt", "r")
s = ""
for l in file_object:
    s+=l
p = tokenizer.tokenize(s)
#print(test_case)

n = node_parser.tokensToNode(p)
print(n)
debugUtils.printNode(n, 0)

def tokenize(s):
    lines = s.split("\n")