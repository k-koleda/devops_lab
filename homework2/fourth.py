input = ["5","-2","4","C","D","9","+","+"]
result = []
for j in input:
    if j == 'C':
        result.pop()
    elif j == 'D':
        result.append((2*result[-1]))
    elif j == '+':
        result.append(result[-1]+result[-2])
    else:
        result.append(int(j))
print(sum(result))
