string = input("Enter a string: ")
symbols = '[@_!#$%^&*()<>?/\|}{~:]'
string.split()

count_alpha = 0
count_digi = 0
count_symbols = 0
count_upper = 0
count_lower= 0

for i in string:
    if i.isalpha()== True:
        count_alpha += 1
        if i.isupper()== True:
            count_upper += 1
        elif i.islower() == True: 
            count_lower += 1

    elif i.isdigit()== True:
        count_digi += 1
    else:
        for j in range(len(string)):
            string[j] in symbols
        count_symbols +=1

print('count_alpha: ', count_alpha)
print("count_digits: ", count_digi)
print("count_symbols: ", count_symbols)
print("count_lower: ", count_lower)
print("count_upper: ", count_upper)
