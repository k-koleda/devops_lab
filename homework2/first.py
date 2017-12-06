i = int(raw_input())
student = [[str(raw_input()), float(raw_input())] for j in range(i)]
student.sort(key=lambda x: x[1])
for j in range(i):
    if student[j][1] < student[j+1][1]:
        if student[j+1][1] == student[j+2][1]:
            temp = sorted((student[j+1][0], student[j + 2][0]), reverse=False)
            print temp[0]
            print temp[1]
            break
        else:
            print student[j + 1][0]
            break
