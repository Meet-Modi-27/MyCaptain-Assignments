list1 = []
list2 = []
a=int(input("How many values you want?"))
for i in range(0,a):
    c = int(input("Give Value"))
    list1.append(c)
for i in list1:
    if i>=0:
        list2.append(i)
print(list2)
