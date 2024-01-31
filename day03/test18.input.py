#file : test18.input.py
#desc : 다중 입력...
#원래는 (in_a in_b) 튜플형으로 데이터받는게 정석 -> 생략
##input_a, input_b = input('값 두 개(공백으로 구분)>')


# 2. map() 함수 사용
input_a, input_b = map(int, input('값 두개 입력(공백 구분) >')).split('')

print(f'입력값{input_a}, {input_b}').split(' ')
