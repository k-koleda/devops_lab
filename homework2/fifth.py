output=[]
input=[]
for _ in range(1,int(raw_input())):
    input.append(_)
for j in input:
    if j % 5 == 0 and j % 3 == 0:
        output.append("fizbuzz")
    if j % 3 == 0:
        output.append("fiz")
    elif j % 5 == 0:
        output.append("buzz")
    else:
        output.append(j)
print output
