# =============================================
# HEADER
# Custom Libraries
import darkModeTheme, functions, header
from header import *
from functions import *

# App Instance
app = QApplication([])
# =============================================

# =============================================
# Appearance(s)
darkModeTheme.windowColorTheme(app)
app.setStyle('Fusion')
# =============================================

# =============================================
# Function Calls
window = Window() 
# =============================================

# =============================================
# Main Driver
app.exec()
# sys.exit(app.exec_())
# =============================================