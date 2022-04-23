import tokenizer
file_object = open("policy.txt", "r")
s = ""
for l in file_object:
    s+=l
p = tokenizer.tokenize(s)
print(p)