student = []
for _ in range(int(raw_input())):
    name = raw_input()
    score = float(raw_input())
    temp = [name, score]
    student.append(temp)
student.sort(key=lambda x: x[1])
if student[1][1] == student[2][1]:
    result = [student[1][0], student[2][0]]
    result.sort(key=lambda x: x[0])
    print (result[0])
    print (result[1])
else:
    print (student[1][0])
