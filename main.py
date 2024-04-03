import PyQt5
import sys
from connection import get_data
from PyQt5 import uic, QtWidgets
from form import *


class Artur(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(Artur, self).__init__(parent)
        res_data = get_data()
        print(res_data)
        height = 0
        for i in res_data:
            height += 50
            label = QtWidgets.QLabel(self)
            label.setGeometry(20, height, 500, 21)
            label.setObjectName(f"{i[0]}")
            label.setText(f"{i[1]}: {i[3]} {i[4]} {i[5]}; {i[6]} ")



if __name__ =='__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    form = Artur()
    form.show()
    sys.exit(app.exec_())











