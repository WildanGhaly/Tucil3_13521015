# file: show_map.py

from PyQt5.QtCore import QUrl
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout
from PyQt5.QtWebEngineWidgets import QWebEngineView
import os

class MainWindow(QMainWindow):
    # Define the file path as a class variable
    html_file_path = os.getcwd() + "/map.html"

    def __init__(self):
        super().__init__()

        # Create a QWidget instance to hold the QWebEngineView widget
        widget = QWidget(self)
        self.setCentralWidget(widget)
        
        self.setMinimumSize(QtCore.QSize(1080, 720))
        self.setMaximumSize(QtCore.QSize(1080, 720))

        # Create a QVBoxLayout instance to hold the QWebEngineView widget
        layout = QVBoxLayout(widget)

        # Create a QWebEngineView widget and add it to the layout
        self.webview = QWebEngineView()
        self.webview.setGeometry(QtCore.QRect(210, 150, 841, 531))
        self.webview.setMinimumSize(QtCore.QSize(841, 531))
        self.webview.setMaximumSize(QtCore.QSize(841, 531))
        layout.addWidget(self.webview)

        # Load the HTML file into the QWebEngineView widget
        self.url = QUrl.fromLocalFile(MainWindow.html_file_path)
        print("Was here")