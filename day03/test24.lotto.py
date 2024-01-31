# file : test24_lotto.py
# desc : 로또번호 생성
import random as rnd # 랜덤은 주로 rnd로 줄여서 많이 씀

numbers = list(range(1,46))
#print(numbers)

lottery = list()

for i in range(6):
    lottery.append(rnd.choice(numbers)) #1~45까지 숫자 중 하나를 랜덤꺼내기

lottery.sort()
print(lottery)
rnd.shuffle(weight)

lottery = rnd.choice(numbers, weight)

