# file : test23_module.py
# desc : 모듈 사용
import math

PI = 3.141592
radius = 5
print(f'원의 크기는{radius * radius * PI}')
print(f'정확한 원의 크기는{radius * radius * math.PI}')
print(f'cos(0)={math.cos(0)}')
print(2 ** 10)
print(round(3.5)) # 반올리(너무 사용하니까 math에 없음, 기본함수)

import math as m # 별명짓기
