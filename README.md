# basic-python-2024
부경대 2024 IOT 개발자과정 기초 프로그래밍 언어 - 파이썬

## 1일차
- 개발환경 구축 
    - 코딩폰트 - 나눔고딕코딩
    - Notepad++ 설치
    - Python 설치
    - Visual Studio Code 설치
    - Git 설치
        - TortoiseGit 설치
        - Github 가입
        - Github Desktop 설치

- 파이썬 기초
    - 콘솔출력
    - 주석
    - 변수
    - 자료형
    - 연산자

    ```python
    # 이 부분 주석
    var = 10 # 정수, 실수, 불, 문자열 모두 가능    
    ```

## 2일차
- 파이썬 기초
    - 흐름제어
        - if
        - for
        - while
    - 복합자료형 + 연산자
    - 함수
    - 구구단, 별찍기

## 3일차
- 파이썬 기초
    - 입력방법
    - 별찍기
    - 함수
    - 객체지향 OOP
        - 객체는 명사와 동사의 집합
        - 명사는 변수, 동사는 함수
        - 변수와 함수를 모두 모아둔 곳 : 클래스(class)
        - 클레스에서 하나씩 생성 : 객체(object)
        - 캡슐화(__plateNumber)
    - 패키지
    
## 4일차
- 파이썬 기초
    - 패키지, 모듈 계속
        > pip --version # 버전확인
        > pip list # 현재 설치된 라이브러리 목록 확인
        > pip install 패키지명 # 패키지를 내 컴퓨터에 설치
        > pip uninstall 패키지명 # 패키지를 삭제

    - 예외처리 : 비정상적 프로그램종료 막기
    ```python
    def divide(x,y):
        try:
            return x / y #ZeroDivisionError 발생
    except ZeroDivisionError as e:
        print('[오류]')
        return 0
    ```
    - 파일 입출력

    ```python
    f=open('파일명', mod=rwa, encoding=cp949 | utf-8)
    f.read()
    f.readline() # 읽기
    f.write('text') # 쓰기
    f.close() # 파일은 반드시 닫는다
    ```
- 파이썬 활용
    - 주피터 노트북
        - Ctrl + Shift + P(명령팔레트) 로 시작
        - 사용방법(test31_jupyternb.jpynb)
        - folium 기본사용
        ![folium사용법](https://raw.githubusercontent.com/znah54/basic-python-2024/main/images/Image20240201172242.png)

## 5일차
 - 파이썬 응용
    - 주피터 노트북 활용 - 구글 코랩(colab)
    - folium 계속
    - json 입출력
    - 응용예제 연습(10개)

## 6일차
- Python 라이브러리 경로 : C:\dev\Langs\Python311\Lib\site-packages
 - 파이썬 응용
    - Windiw App(PyQt) 만들기 

    ```shell
    > pip install PyQt5
    > pip install PyQt5Designer
    ```
        
        - PyQt5 기본실행
        - QtDesigner 사용법
        - 쓰레드 학습 : UI쓰레드와 Background쓰레드 분리
          - GIL, 병렬프로세싱 더 학습할 것

        ![쓰레드예제](https://raw.githubusercontent.com/znah54/basic-python-2024/main/images/Thread.gif)
        
        ```python
    # 쓰레드 클래스에서 시그널 선언
    class BackWorker(QThread): # PyQt에서 스레드 클래스 상속
        initSignal = pyqtSignal(int) # 시그널을 UI스레드로 전달하기위한 변수객체
        setSignal = pyqtSignal(int)
        # ...

        def run(self) -> None: # 스레드 실행
            # 스레드로 동작할 내용
            maxVal = 1000001
            self.initSignal.emit(maxVal) # UI쓰레드로 보내기...
            # ...

    class qtwin_exam(QWidget):  # UI 스레드
        # ...
        def btnStartClicked(self):
            th = BackWorker(self)
            th.start() # BackWorker 내의 self.run() 실행
            th.initSignal.connect(self.initPgbTask) # 스레드에서 초기화 시그널이 오면 initPgbTask 슬롯함수가 대신 처리
            # ...  

            # 스레드에서 시그널이 넘어오면 UI처리를 대신 해주는 슬롯함수
    @pyqtSlot(int) # BackWorker self.initSignal.emit() 동작해서 실행
    def initPgbTask(self, maxVal):
            self.pgbTask.setValue(0)
            self.pgbTask.setRange(0, maxVal-1)  
    ```

## 7일차
- 파이썬 응용
    - 객체지향
        - 상속, 오버라이딩(재정의), 오버로딩(같은이름의 함수를 여러개 활용, 매개변수는 다르게)
    - 가상환경 Virtualenv
        - 다른 버전 파이썬도 설치해야 사용 가능
        - 현재 3.11에서 3.9 가상환경 만들려면 3.9 파이썬 설치필요
    - PyQt5와 응요예제 연습
        - 이미지 뷰어
        - 이미지 에디터

     ![PyQt예제](https://raw.githubusercontent.com/znah54/basic-python-2024/main/images/test.jpg)

- 가상환경

## 8일차
- 파이썬 응용
    - PyQt5 응용예제 계속

- 파이썬 기본 코딩테스트
    - 주피터노트북 활용

## 추가
- 파이썬 실행파일 만들기
    - PyQt ui파일이나 이미지파일의 경로가 절대경로가 지정
    - pip install pyinstaller 패키지 설치
    - pyinstaller -w -F 파이썬.py (-w: 콘솔창 없애기, -F: 실행파일 하나로 만들기)