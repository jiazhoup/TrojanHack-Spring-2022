from node import Node

#def tokenize(file):
#    pass

def tokensToNode(tokens):
    nodes = []
    for index, token in enumerate(tokens):
        if not (token[0].isdigit() and token[1] == ':'):
            nodes.append(recurseNodes(tokens, index)[:2])
    n = Node("HEAD")
    for node in nodes:
        if node[1] == "str":
            n.add_regex(node[0])
        if node[1] == "dir":
            n.addChild(node[0])
    return n

def recurseNodes(tokens, token_index):
    #grab the next token as the current level
    tokens_spl = tokens[token_index].split(":")
    if len(tokens_spl) == 2:
        level = int(tokens_spl[0])
        name = tokens_spl[1]
    elif len(tokens_spl) == 1:
        level = 0
        name = tokens[token_index]
    else:
        print("Token parse error: file names should have 0 or 1 ':'!")
    token_index += 1

    #scour through the file to find the following levels
    all_sub_dir = []                 #things in directory
    all_sub_files = []
    while token_index < len(tokens):
        tokens_spl = tokens[token_index].split(":")
        if len(tokens_spl) == 2:
            next_level = int(tokens_spl[0])
            next_name = tokens_spl[1]
        elif len(tokens_spl) == 1:
            next_level = 0
            next_name = tokens_spl[0]
        else:
            print("Token parse error: file names should have 0 or 1 ':'!")
        
        #if we go back one level or return the original one, we ended scouring that 
        #level
        #print('going from: ' + str(level) + " "  + name.strip())
        #print('to: ' + str(next_level) + " " + next_name.strip())
        if next_level <= level:
            break
        elif next_level == level + 1:   #if the next level exists
            #recurse for that level then add result to the list of things in this directory
            data = recurseNodes(tokens, token_index)
            if data[1] == "str":
                all_sub_files.append(data[0])
            elif data[1] == "dir":
                all_sub_dir.append(data[0])
            token_index = data[2]
        else:
            print("Token parse error: Can't jump more than 1 directory")

    if len(all_sub_dir) + len(all_sub_files) == 0:
        return name.strip(), "str", token_index
    else:
        n = Node(name.strip())
        for nn in all_sub_dir:
            n.addChild(nn)
        for fn in all_sub_files:
            n.add_regex(fn)
        return n, "dir", token_index
