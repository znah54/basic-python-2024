# file : test38_pyqt.py
# desc : Qt디자이너 만든 ui와 연동

import sys
from PyQt5 import QtGui, QtWidgets, uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class qtwin_exam(QWidget): # QWidget을 상속받음
    # 생성자
    def __init__(self) -> None:
        super().__init__()
        uic.loadUi('./day06/TestApp.ui', self)
        self.btnStart.clicked.connect(self.btnStartClicked)
        self.btnStop.clicked.connect(self.btnStopClicked)

    def btnStartClicked(self):
        print('시작버튼 클릭')
        self.lblStatus.setText('상태 : 동작시작')
        QMessageBox.about(self, '동작','***시스템이 시작되었습니다')

    def btnStopClicked(self):
        print('종료버튼 클릭')
        self.lblStatus.setText('상태 : 동작중지')

if __name__ == '__main__': # main entry 확인조건 추가
    loop = QApplication(sys.argv)
    instance = qtwin_exam()
    instance.show()
    loop.exec_()