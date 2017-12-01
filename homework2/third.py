n = int(raw_input())
a = []
result = ''
input = [1,4,11]
for j in range(1,n + 1):
   if j > 1:
       for i in range(2,j):
           if (j % i) == 0:
               break
       else:
           a.append(j)

print a
for j in range(input.__len__()):
     result += str(a[input[j]])
print result
