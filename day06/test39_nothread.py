# file : test38_nothread.py
# desc : Qt에서 스레드 없이 동작테스트

import sys
from PyQt5 import QtGui, QtWidgets, uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtGui import QCloseEvent
from PyQt5.QtWidgets import *

class qtwin_exam(QWidget): # QWidget을 상속받음
    # 생성자
    def __init__(self) -> None:
        super().__init__()
        uic.loadUi('./day06/ThreadApp.ui', self)
        self.btnStart.clicked.connect(self.btnStartClicked)

    def btnStartClicked(self):
        maxVal = 101
        print('시작버튼 클릭')
        self.pgbTask.setValue(0) # 프로그레스바 0부터 시작
        self.pgbTask.setRange(0, maxVal-1) #  0 부터 100까지
        for i in range(maxVal): # 0~100까지
            print_str=f'노쓰레드 출력 >> {i}'
            print(print_str)
            self.txbLog.appedn(print_str)
            self.pgbTask.setValue(i) 

    # Qwidget에 있는 closeEvent를 그대로 쓰면 그냥 닫힘
    # 닫을지 말지를 한번더 물어보는 형태로 다시 구현하고 싶음(재정의 : Override)
    def closeEvent(self, QCloseEvent) -> None:
        re = QMessageBox.question(self, '종료확인', '종료할래?', QMessageBox.Yes|QMessageBox.No)
        if re == QMessageBox.Yes: #닫기
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()

if __name__ == '__main__': # main entry 확인조건 추가
    loop = QApplication(sys.argv)
    instance = qtwin_exam()
    instance.show()
    loop.exec_()