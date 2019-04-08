import sys
import subprocess
from PyQt5.QtGui import QIcon, QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QApplication, QListView
import os
os.rmdir()

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.initgui()

    def initgui(self):
        view = QListView(self)
        model = QStandardItemModel()
        f = self.check()
        for l in f:
            print(l)
            model.appendRow(QStandardItem(l))
        view.setModel(model)
        self.show()

    def check(self):
        cmd_out = subprocess.check_output('ls').decode(sys.stdout.encoding)
        return str(cmd_out).split()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
