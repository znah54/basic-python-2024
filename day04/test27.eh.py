# file : test27_eh.py
# desc : 예외발생 청리

def add(x, y):
    return x + y
def minux(x, y):
    return x - y
def multi(x, y):
    return x * y
def divide(x, y):
    return x / y

def get0perands():
    try:
        a,b = map(int, intput('두 수 입력(구분자 공백) >').split())
        return a,b
    except ValueError as e:
        #print(e) 정확한 예외 메시지 출력
        print('입력 오류  : 정수만 입력하세요')
        return 1,1
    except ZeroDivisionError as e:
        print('[오류]')
        return 0

while True:
    mnu = input('메뉴입력(p[덧셈],m[뺄셈],t[곱셈],d[나눗셈],x[종료])')
    
    if mnu == 'p':
        a,b = get0perands()
        print(f'덧셈{a} + {b} = {add(a,b)}')
    elif mnu == 'm':
        a,b = get0perands()
        print(f'덧셈{a} - {b} = {minus(a,b)}')
    elif mnu == 't':
        a,b = get0perands()
        print(f'곱셈{a} * {b} = {multi(a,b)}')
    elif mnu == 'd':
        a,b = get0perands()
        print(f'나눗셈{a} / {b} = {divide(a,b)}')
    elif mnu == 'x':
        break
    else:
        continue # 다시 메뉴 선택으로 돌아감