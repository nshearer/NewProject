from PySide.QtCore import *
from PySide.QtGui import *

from NewProjectMainWindow_UI import Ui_NewProjectMainWindow_UI

class NewProjectMainWindow(QMainWindow, Ui_NewProjectMainWindow_UI):

    def __init__(self, parent=None):
        super(NewProjectMainWindow, self).__init__(parent=parent)
        self.setupUi(self)
