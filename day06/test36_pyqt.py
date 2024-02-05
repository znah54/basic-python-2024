# file : test36_pyqt.py
# desc : PyQt 기본화면 만들기

import sys 
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPaintEvent, QPainter, QColor, QFont
from PyQt5.QtWidgets import QApplication, QWidget


#print(sys.argv) # 현재 파이썬파일의 경로표시

class qtwin_exam(QWidget): # QWidget을 상속받을거야. Qwidget이 가진 모든것을 사용할 수 있다
    # 생성자
    def __init__(self) -> None:
        super().__init__()
        self.initUI() # 화면초기화 함수를 호출

    def initUI(self):
        self.setGeometry((1920-400)//2, (1080-300)//2, 400,300) # x, y, width, heigth
        self.setWindowTitle('Qt5 Hello world!')
        self.text = ''
        self.show()
    
    def drawText(self, event, paint):
        paint.setPen(QColor(0, 0, 0)) #red green blue 순 (0,0,0은 black) 0~255  
        paint.setFont(QFont('NanumGothic',15))
        paint.drawText(400//2, 300//2, 'HELL WORLD!')
        paint.drawText(event.rect(),Qt.AlignLeft, self.text)

    def paintEvent(self, event) -> None: # 재정의(Override)
        paint = QPainter()
        paint.begin(self) # 열면
        self.drawText(event, paint)
        paint.end() #닫는다

loop = QApplication(sys.argv) # 소스 위치 앱 성생
instance = qtwin_exam() # Qwidget을 상소한 qtwin_exam 객체를 생성
loop.exec_()
