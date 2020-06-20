# _*_coding:utf-8_*_
# author:leo
# date:
# email:alplf123@163.com

from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QWidget, QVBoxLayout, QFrame
from PyQt5.Qt import QSize
import sys

class Example(QMainWindow):

    def __init__(self):
        super(Example, self).__init__()

        self._initUI()
    def _initUI(self):
        #控件随窗口改变而改变
        # 可以通过继承 QMainWindow 来实现
        self.resize(400, 400)
        #建立顶层控件
        self.centeralwidget = QWidget()
        self.vbox = QVBoxLayout(self.centeralwidget)
        edit = QTextEdit()
        self.vbox.addWidget(edit)
        #通过设置中心控件，将子控件填充布局
        #如果有多个控件最好在加一层widget这样最好布局，控制
        self.setCentralWidget(self.centeralwidget)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())