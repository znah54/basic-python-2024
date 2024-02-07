a = input(' ')
b=a.split(' ')
print(f'{len(b)}')
num = 1
for i in b:
    if(num%2==0):
        print(i.upper(), end='')
    else:
        print(i, end='')
    num+=1