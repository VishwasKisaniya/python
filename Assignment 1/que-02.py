
list1 = []
n = int(input("Enter number of elements in list 1 : "))
for i in range(0, n):
    ele1 = int(input("Enter list 1 elements: "))
    list1.append(ele1) 

list2 = []
m = int(input("Enter number of elements in list 2 : "))
for i in range(0, m):
    ele2 = str(input("Enter list 2 elements: "))
    list1.append(ele2) 
list1.extend(list2)
print(list1)

