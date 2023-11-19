n=int(input("Enter a number in octal form: "))
a=[]
while(n>0):
    num=n%2
    a.append(num)
    n=n//2
a.reverse()
for i in a:
    print(i, end="")