def tokenize(s):
    lines = s.split("\n")
    file_object = open("policy.txt", "r")
    lines = []
    parsed = []


    for l in file_object:
        lines.append(l)
        

    for l in lines:
        count = 0
        for j in range(0, len(l)):
            if l[j] == ' ':
                count+=1
            else:
                break   
        if count > 0:
            parsed.append(str(count//4) + ":" + l[count:])
        else:
            parsed.append(l)

    return parsed