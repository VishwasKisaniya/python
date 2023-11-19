'''
import copy
l1 = [[1,2,3], [5,6,7]]
l2 = copy.copy(l1)
print(l1)
print(l2)

def sorting(list):
    for i in (len(list)-1):
        for j in range (len(list) - i-1):
            list[j+1][2] > list[j][2] 
            list[j], list[j+1] = list[j+1], list[j] 
    
            
    
    return list

com = [('google, 2019,139.20'), ('apple, 2019,260'), ('facebook', 2019, 704)]
print(sorting(com))

'''
'''
l1 = [1,2,3,4,5]
for i in enumerate(l1):   #important
    print(i)
'''
l1 = [1,2,3]
l2 = [5,6,8]
l1.append(l2)
l1.append(90)
l2.extend(l1)
print(l1)
print(l2)