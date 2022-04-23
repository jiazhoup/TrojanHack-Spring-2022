from node import Node

def tokenize(file):
    pass

def stringToNode(tokens):
    n = Node()

def recurseNodes(tokens, token_index):
    #grab the next token as the current level
    tokens_spl = tokens.split(":")
    if int(tokens_spl) == 2:
        level = int(tokens_spl[0])
        name = tokens_spl[1]
    elif len(tokens_spl) == 1:
        level = 0
        name = tokens[token_index]
    else:
        print("Token parse error: file names should have 0 or 1 ':'!")

    #scour through the file to find the following levels
    all_sub_dir = []                 #things in directory
    all_sub_files = []
    while token_index < len(tokens):
        token_spl = tokens.split(":")
        if int(tokens_spl) == 2:
            next_level = int(tokens_spl[0])
            next_name = tokens_spl[1]
        elif len(tokens_spl) == 1:
            next_level = 0
            next_name = tokens[token_index]
        else:
            print("Token parse error: file names should have 0 or 1 ':'!")
        
        #if we go back one level or return the original one, we ended scouring that 
        #level
        if next_level <= level:
            break
        elif next_level == level + 1:   #if the next level exists
            #recurse for that level then add result to the list of things in this directory
            data = recurseNodes(tokens, tokens_index)
            if data[1] == "str":
                all_sub_files.append(data[0])
            elif data[1] == "dir":
                all_sub_dir.append(data[0])
        else:
            print("Token parse error: Can't jump 2 directories")

        token_index += 1

    if len(all_sub_dir) + len(all_sub_files) == 0:
        return name, "str"
    else:
        n = Node(name)
        for nn in all_sub_dir:
            n.add_child(nn)
        for fn in all_sub_files:
            n.add_regex(fn)
        return n, "dir"
