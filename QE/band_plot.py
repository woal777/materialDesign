import numpy as np
from pymatgen.io.vasp.outputs import Dos, Spin
from pymatgen.electronic_structure.plotter import DosPlotter

import sys
import matplotlib

matplotlib.use("Qt5Agg")
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, \
    QPushButton, QLineEdit, QHBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt


class MyMplCanvas(FigureCanvas):
    """Ultimately, this is a QWidget (as well as a FigureCanvasAgg, etc.)."""

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = plt.figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        print(dir(self.axes))
        # We want the axes cleared every time plot() is called
        # self.axes.hold(False)

        self.compute_initial_figure()

        #
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QSizePolicy.Expanding,
                                   QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def compute_initial_figure(self):
        pass


class MyDynamicMplCanvas(MyMplCanvas):
    """A canvas that updates itself every second with a new plot."""

    def __init__(self, *args, **kwargs):
        MyMplCanvas.__init__(self, *args, **kwargs)
        self.dsp = DosPlotter()

    def update_figure(self, txt):
        # Build a list of 4 random integers between 0 and 10 (both inclusive)
        self.axes.clear()
        with open(txt) as f:
            ef = float(f.readline().split()[-2])
            arr = [r.split() for r in f.readlines()]
            arr = np.array(arr)
            arr = arr.astype(np.float)
            self.dos = Dos(ef, arr[:, 0], {Spin.up: arr[:, 1]})
            self.dsp.add_dos('tdos', self.dos)
        self.dsp.get_plot(plt=self.axes)
        self.draw()


class ApplicationWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setWindowTitle("application main window")

        self.file_menu = QMenu('&File', self)
        self.file_menu.addAction('&Quit', self.fileQuit,
                                 QtCore.Qt.CTRL + QtCore.Qt.Key_Q)
        self.menuBar().addMenu(self.file_menu)

        self.help_menu = QMenu('&Help', self)
        self.menuBar().addSeparator()
        self.menuBar().addMenu(self.help_menu)

        self.help_menu.addAction('&About', self.about)

        self.main_widget = QWidget(self)
        l = QVBoxLayout(self.main_widget)
        # sc = MyStaticMplCanvas(self.main_widget, width=5, height=4, dpi=100)
        self.dc = MyDynamicMplCanvas(self.main_widget, width=5, height=4, dpi=100)
        # l.addWidget(sc)
        l.addWidget(self.dc)

        self.main_widget.setFocus()
        self.setCentralWidget(self.main_widget)

        self.statusBar().showMessage("All hail matplotlib!", 2000)

        self.lineedit = QLineEdit('/home/ksrc5/HfO2/Fm3m_matarial_project/cb/pbe0/spn-kjpaw/Hf.dos', self)
        # self.lineedit.move(0, 20)
        button = QPushButton('Update Plotting', self)
        button.setToolTip('This is an example button')
        button.clicked.connect(self.update_figure)
        l.addWidget(button)
        l.addWidget(self.lineedit)


    def update_figure(self):
        self.dc.update_figure(self.lineedit.text())

    def fileQuit(self):
        self.close()

    def closeEvent(self, ce):
        self.fileQuit()

    def about(self):
        QMessageBox.about(self, "About",
                          """embedding_in_qt5.py example
  Copyright 2015 BoxControL

  This program is a simple example of a Qt5 application embedding matplotlib
  canvases. It is base on example from matplolib documentation, and initially was
  developed from Florent Rougon and Darren Dale.

  http://matplotlib.org/examples/user_interfaces/embedding_in_qt4.html

  It may be used and modified with no restriction; raw copies as well as
  modified versions may be distributed without limitation."""
                          )


if __name__ == '__main__':
    app = QApplication(sys.argv)

    aw = ApplicationWindow()
    aw.setWindowTitle("PyQt5 Matplot Example")
    aw.show()
    # sys.exit(qApp.exec_())
    app.exec_()
