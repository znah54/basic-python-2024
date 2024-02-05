# file : test40_thread.py
# desc : Qt 스레드로 동작

# file : test38_nothread.py
# desc : Qt에서 스레드 없이 동작테스트

import sys
from PyQt5 import QtGui, QtWidgets, uic
from PyQt5.QtCore import *
from PyQt5.QtCore import QObject
from PyQt5.QtGui import *
from PyQt5.QtGui import QCloseEvent
from PyQt5.QtWidgets import *

class BackWorker(QThread): #PyQt에서 스레드 클래스 상속
    initSignal = pyqtSignal(int) # 시그널을 UI 스레드로 전닥하기위한 변수 객체
    setSignal = pyqtSignal(int)
    setLog = pyqtSignal(str)

    def __init__(self,parent) -> None:
        super().__init__(parent)
        self.parent = parent #BackWorker에서 사용할 멤버변수

    def run(self) -> None:
        # 스레드로 동작할 내용
        maxVal = 1000
        self.initSignal.emit(maxVal)
        ##self.parent.pgbTask.setValue(0) # 프로그레스바 0부터 시작 !! QThread에선 UI관련된 처리를 할 수 없음
        ##self.parent.pgbTask.setRange(0, maxVal-1) #  0 부터 100까지
        for i in range(maxVal):
            print_str=f'쓰레드 출력 >> {i}'
            print(print_str)
            self.setSignal.emit(i)
            self.setLog.emit(print_str)
            ##self.parent.txbLog.append(print_str)
            ##self.parent.pgbTask.setValue(i)

class qtwin_exam(QWidget): # QWidget을 상속받음
    
    def __init__(self) -> None:
        super().__init__()
        uic.loadUi('./day06/ThreadApp.ui', self)
        self.btnStart.clicked.connect(self.btnStartClicked)

    def btnStartClicked(self):
        th = BackWorker(self)
        th.start() # BackWorker 내의 self.run() 실행
        th.initSignal.connect(self.initPgbTask) # 스레드에서 초기화 시그널이 오면 initPgbTask 슬롯함수가 대신 처리
        th.setSignal.connect(self.setPgbTask)
        th.setLog.connect(self.setTxbLog) # TextBrowser 위젯에
        
    def closeEvent(self, QCloseEvent) -> None:
        re = QMessageBox.question(self, '종료확인', '종료할래?', QMessageBox.Yes|QMessageBox.No)
        if re == QMessageBox.Yes: #닫기
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()

        # 스레드에서 시그널이 넘어오면 UI처리를 대신 해주는 슬롯함수
    @pyqtSlot(int) # BackWorker self.initSignal.emit() 동작해서 실행
    def initPgbTask(self, maxVal):
            self.pgbTask.setValue(0)
            self.pgbTask.setRange(0, maxVal-1)
        
    @pyqtSlot(str) # BackWorker self.setLog.emit() 동작해서 실행
    def setTxbLog(self, msg):
            self.txbLog.append(msg)

    @pyqtSlot(int) # BackWorker self.setSignal.emit() 동작해서 실행
    def setPgbTask(self, val):
            self.pgbTask.setValue(val)

        
if __name__ == '__main__': # main entry 확인조건 추가
    loop = QApplication(sys.argv)
    instance = qtwin_exam()
    instance.show()
    loop.exec_()

