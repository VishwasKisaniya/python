#creating a input list from user.
list1 = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    ele = int(input())
    list1.append(ele) 
#taking input position to be edited
pos = int(input("Enter the position where you want to add or drop: "))
# loop for asking choice/changes user want to do.
choice = 1
while choice !=0 :
    print("0. Exit")
    print("1. add")
    print("2. drop")
    choice=int(input("Enter choice: "))
    if choice == 1:
        element = int(input("Enter element to add: "))
        list1.insert(pos,element)
        for i in range(0,n):
            print(list1[i],end=" ")
        print("\n")
    elif choice== 2:
        list1.remove(list1[pos])
        for i in range(0,n-1):
            print(list1[i], end =" ")
        print("\n")
    elif choice == 0:
        break
    





