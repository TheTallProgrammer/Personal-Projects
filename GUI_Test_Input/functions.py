import header
from header import *

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        # set the title
        self.setWindowTitle("Lo-Kag.exe")
        
        # setting  the geometry (dimensions) of window
        self.setGeometry(0, 0, 500, 500)
        
        # show all the widgets
        self.show()
        