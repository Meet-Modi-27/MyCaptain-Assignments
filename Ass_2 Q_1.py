n1 = 0
n2 = 1
num =int(input("Give the number of elements you need: "))
print(n1)
print(n2)
for i in range(2,num,1):
    n3=n1+n2
    print(n3)
    n1 = n2
    n2 = n3
