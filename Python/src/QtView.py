import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import BackEnd as be
import random as rd

form_class = uic.loadUiType("main.ui")[0]

sideMenu = [
    '두부연근튀김', '리얼 티라미수 찰떡', '후라이드 순살(중)', '후라이드 순살(소)_양념치킨소스', '후라이드 순살(소)_케이준소스',
    '튼튼도시락', '반찬 계란말이', '반찬 치즈계란말이', '반찬 묵은지김치찌개', '반찬 소고기육개장', '반찬 카레',
    '반찬 소불고기', '반찬 순살 고등어데리야끼', '반찬 치킨', '반찬 고기고기', '반찬 돈까스 도련님', '반찬 제육볶음',
    '반찬 토네이도 소세지', '반찬 돈까스', '리얼꿀 미니호떡', '바삭 군만두', '미니 찹쌀핫도그', '미니 찹쌀탕수육',
    '감자고로케', '케이준후라이', '고메이 크림 고로케', '토네이도 소세지 튀김세트', '찹쌀탕수육박스(대)', '찹쌀탕수육박스(중)',
    '오리지널 닭강정(중)', '오리지널 닭강정(소)', '치킨 BOX(대)', '치킨BOX(중)_양식소스', '치킨BOX(중)_타르타르소스',
    '오징어젓갈', '오이지무침', '한솥 두부강된장소스', '한솥 감초볶음고추장소스', '볶음김치', '김치', '무말랭이 무침', '한솥밥',
    '현미밥', '아이스 애플망고'
]

class MyWindow(QMainWindow, form_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_AllRandom.clicked.connect(self.AllRandom_Click)
        self.btn_Menu.clicked.connect(self.Random_Click)

    def AllRandom_Click(self):
        try:
            menu = be.DataLoad()
            result = rd.choice(menu)
            self.lb_Result.setText(result)
            self.lb_Price.setText(be.PriceLoad(result))
        except:
            QMessageBox.critical(self, "오류", "심각한 문제가 발생했습니다!")

    def Random_Click(self):
        try:
            menu = be.DataLoad()
            result = rd.choice(menu)
            while result in sideMenu:
                result = rd.choice(menu)
            self.lb_Result.setText(result)
            self.lb_Price.setText(be.PriceLoad(result))
        except:
            QMessageBox.critical(self, "오류", "심각한 문제가 발생했습니다!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
