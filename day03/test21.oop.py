# file : test2_oop.py
# desc : 객체지향 클래스 만들기

class Person: # 사람 클래스 선언
    name = '' # 멤버 변수 
    age = 0
    gender = ''

    def __init__(self) -> None:
        self.name = 'Tom'
        self.age = 29
        self.gender = 'man'
    
    # 클래스를 호출할때 원하는 형태로 변환해서 보여줄때
    def __str__(self) -> str:
        strs = f'커스텀 출력 : 이름 {self.name} 객체 생성!'
        return strs

    def walk(self):
        print(f'{self.name}이(가) 걷습니다.')

    def stop(self):
        print(f'{self.name}이(가) 멈춥니다.')



# 사람 객체 생성, Instance(사례, 예제)
p1 = Person() # 함수호출처럼 작성하면 됨
p2 = Person()

#print(type(p1)) 
#print(id(p1)) # 다른 객체인지 확인
#print(id(p2))

p1.name ='a'
p1.age = 28
p1.gender = 'man'

p2.name ='b'
p2.age = 28
p2.gender = 'woman'

print('생성자 함수 ---------->')
gd = Person()
print(f'gd=>이름:{gd.name} / 나이:{gd.age}세 / 성별:{gd.gender}')
print(gd)