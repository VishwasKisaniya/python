#Que: 01
'''
string = "Hi there class"
print(string.split())

'''

#que: 02
'''
planet = "Earth"
diameter = 12742

sentence = "The diameter of {0} is {1} kilometers.".format(planet,diameter)
print(sentence)
 
'''

#que: 03
'''
lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
print(lst[3][1][2])

'''

#que: 04
'''
d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}

print(d['k1'][3]['tricky'][3]['target'][3])

'''

#que- 05
'''
def catcher(email):
    m = email.split('@')[1]
    print(m)
    return
  
email = input("write email: ")
catcher(email)

'''

#que- 06
'''
def finder(sentence):
    m = sentence.lower().split()
    if 'dog' in m:
        print('Yes')
    else:
        print("No")
    return

string = 'hello my dear DOG'
finder(string)

'''

#que: 07
'''

def finder(sentence):
    m = sentence.lower().split()
    count = 0
    for i in range (len(m)):

        if(m[i] == 'dog'):
            count +=1
        else: 
            count = count

    return print(count)

string = 'hello dog my dog dear DOG'
finder(string)

'''

#que: 08
