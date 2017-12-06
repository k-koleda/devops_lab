i = int(raw_input())
o = int(raw_input())
output = [i, o]
nod = 0
for j in reversed(range(1, o+1)):
    if output[0] % j == 0 and output[1] % j == 0:
        nod = j
        break
print nod
