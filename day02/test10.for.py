# file : test10_for.py
# desc : for 반복문
std = [80,90,100,50,60,66,55,77,70,100]
kor_sum = 0

for i in std:
    kor_sum = kor_sum + i
print(kor_sum)
print(kor_sum/len(kor_sum))

list_a = [[1,3,5],[2,4,8],[10,20,30]]

for i in list_a:
    for j in i:
        print(j)