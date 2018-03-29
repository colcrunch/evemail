from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from ui.mainw import Ui_MainWindow
from ui.compose import Ui_MainWindow as Ui_Compose
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Test")
        self.ui.pushButton.clicked.connect(self.compose)
        self.comp = ComposeWindow()

    def compose(self):
        self.comp.show()
        self.comp.raise_()


class ComposeWindow(QMainWindow):
    def __init__(self):
        super(ComposeWindow, self).__init__()
        self.ui = Ui_Compose()
        self.ui.setupUi(self)
        self.setWindowTitle("Compose")


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    window.raise_()
    app.exec_()


if __name__ == "__main__":
    main()