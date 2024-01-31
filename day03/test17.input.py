# file : test17_input.py
# desc : 콘솔 입력

# input()
a = input('곱할 수 입력 >')
if a.isnumeric() == True:
    a = int(a)
    print(f'입력값 = {a}')
    # 곱하기
    result = a * 5
    print(f'결과 = {result}')
else:
    print('정수만 입력')

