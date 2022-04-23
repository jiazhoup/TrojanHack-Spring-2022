import node_parser
import debugUtils

test_case_f = open('policy.txt', 'r')
test_case = []
for l in test_case_f:
    test_case.append(l)
#print(test_case)

n = node_parser.tokensToNode(test_case)
print(n)
debugUtils.printNode(n, 0)

