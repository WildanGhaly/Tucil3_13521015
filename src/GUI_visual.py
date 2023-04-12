# File GUI_visual.py

from PyQt5.QtWidgets import QWidget , QFileDialog
from ui_GUI import Ui_Form
from show_map import MainWindow as map
from PyQt5 import QtCore
import graph as g
import map_visual as mv

# Pemanggilan GUI
class ShortestPathFinder(map, QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.browse.clicked.connect(self.select_file_button_clicked)
        self.astar.clicked.connect(self.astar_clicked)
        self.ucs.clicked.connect(self.ucs_clicked)
        self.isMapSelected = False

    def select_file_button_clicked(self):
        file_name,_ = QFileDialog.getOpenFileName(self, "Open File",
                                 "../test",
                                 "Text(*.txt);;Images (*.png *.xpm *.jpg);;All files(*.*)")
        if((file_name == "")):
            return
        
        g.initialize(file_name)
        
        self.filename.setText(file_name)
        self.dropbox_start.clear()
        self.dropbox_goal.clear()
        _translate = QtCore.QCoreApplication.translate
        
        for i in range (len(g.list_of_names)):
            self.dropbox_start.addItem("")
            self.dropbox_start.setItemText(i, _translate("Form", g.list_of_names[i]))
            self.dropbox_goal.addItem("")
            self.dropbox_goal.setItemText(i, _translate("Form", g.list_of_names[i]))
        
        self.isMapSelected = True

    def astar_clicked(self):
        if (not self.isMapSelected):
            return
        
        self.startNode = self.dropbox_start.currentText()
        self.goalNode = self.dropbox_goal.currentText()
        if self.dropbox_start.currentIndex() > self.dropbox_goal.currentIndex():
            self.startNode, self.goalNode = self.goalNode, self.startNode
   
        self.label.lower()
        self.display.lower()
        self.webview.setGeometry(QtCore.QRect(210, 150, 841, 531))
        
        self.path_solution = g.astar(self.startNode, self.goalNode)
        self.list_path = g.path_coords(self.path_solution)
        
        mv.visual_map(self.list_path, self.path_solution, False)
        
        self.webview.load(self.url)
    
    def ucs_clicked(self):
        if (not self.isMapSelected):
            return
        
        self.startNode = self.dropbox_start.currentText()
        self.goalNode = self.dropbox_goal.currentText()
        if self.dropbox_start.currentIndex() > self.dropbox_goal.currentIndex():
            self.startNode, self.goalNode = self.goalNode, self.startNode
   
        self.label.lower()
        self.display.lower()
        self.webview.setGeometry(QtCore.QRect(210, 150, 841, 531))
        
        self.path_solution = g.ucs(self.startNode, self.goalNode)
        self.list_path = g.path_coords(self.path_solution)
        
        mv.visual_map(self.list_path, self.path_solution, True)
        
        self.webview.load(self.url)