def printNode(n, level):
    print('\t' * level + n.getName())
    for ar in n.getAcceptedRegexs():
        print('\t' * (level + 1) + ar)
    for node in n.getChildren():
        printNode(node, level + 1)