# file : text_fileio.py
# desc : 텍스트 파일 입출력
# mode : a : 내용 추가 r : 읽기 w : 쓰기
# encoding : cp949(한글), utf-8(만국공통어)
f = open('sample.txt', mode='w', encoding='utf-8')

f.write('안녕하세요, 우리는 IOT개발자 과정입니다') # mode = a,w 

f.close() # 파일은 무조건 마지막에 닫는다.
print('파일생성')