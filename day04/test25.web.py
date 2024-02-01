# file : test_web.py
# desc : urlib 모듈 사용법


#from urllib.request import Request, urlopen / request 모듈안의 모든 내용 다 사용할때

from urllib.request import Request, urlopen #Request클래스와 urlopen만 쓰겠다

req = Request('https://www.naver.com/') # 네이버 웹주소(url)
res = urlopen(req) # url주소로 웹사이트 열어달라고 요청

print(f'응답 코드 :{res.status}') # url로 요청된 웹사이트 응답 확인
print(res.read())


