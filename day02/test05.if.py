# date : 20240130
# desc : 흐름제어 if

## 조건이 참일때와 거짓일때로 나누어서 어떤일 처리 if
## if 조건 : - 참인 조건
## else : - 거짓인 조건
## 입력함수 input() - 문자

number = int(input())

if number > 0:  ## if 조건 : - 참인 조건
    print('양수입니다')
elif number == 0: # 양수X 음수X
    print('0입니다')
else: ## else : - 거짓인 조건
    print('음수입니다')
