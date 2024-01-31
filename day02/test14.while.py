## while 참인 조건:
## 공통점 if 조건 : elif 조건 : else: , for in range():, while 조건:
count = 0

while count < 10 : # count 변수값이 10보다 작거나 같은 동안 반복
    # 무한루프 : Window OS, 모바일 OS, 자동차네비게이션, 라즈베이파이, 아두이노, 게임
    # Winform 개발, 웹개발
    count = count+1
    print('나무찍기', count)
#debugging
    # F9 중단점 토글, F5 디버깅시작, F10 한줄씩 진행, F11 함수안으로 진입
    # shift + F5 디버깅종료
number = 0
while True:
    number = number + 1
    if str(number).count('3') == 1 or \
    str(number).count('6') == 1 or \
    str(number).count('9') == 1:
        print('짝!')
    else:
        print(number)

    if number == 30: break 