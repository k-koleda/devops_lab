output=[]
input=[]
for i in range(int(raw_input())):
    input.append(i)
for j in input:
    if j == 0:
        output.append(j)
    elif j % 5 == 0 and j % 3 == 0:
        output.append("fizbuzz")
    elif j % 3 == 0:
        output.append("fiz")
    elif j % 5 == 0:
        output.append("buzz")
    else:
        output.append(j)
print output
