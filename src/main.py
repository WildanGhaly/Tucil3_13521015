# file: main.py

from GUI_visual import ShortestPathFinder
import PyQt5.QtWidgets as QtWidgets
import sys

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = ShortestPathFinder()
    window.show()
    sys.exit(app.exec_())