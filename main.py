import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QAction, QPushButton
from Ben10dle import Ui_MainWindow

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())