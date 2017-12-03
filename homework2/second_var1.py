list1 = [1,2,3,4,5,6,7]
list2 = [1,2,3,4,2,3]
pos = 0
dic = {}
if len(list1) < len(list2):
    for _ in list1:
        dic[_] = list2[pos]
        pos += 1
else:
    for _ in list1:
        if pos < len(list2):
            dic[_] = list2[pos]
            pos += 1
        else:
            dic[_] = None
print dic
