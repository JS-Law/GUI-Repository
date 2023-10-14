from PyQt6.QtWidgets import QApplication, QLabel
from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtCore import Qt

import sys


app = QApplication(sys.argv)
palette = QPalette()
palette.setColor(QPalette.ColorRole.Window, QColor(0, 128, 255))
palette.setColor(QPalette.ColorRole.WindowText, Qt.GlobalColor.white)
app.setPalette(palette)

w = QLabel("Palette Test")
w.show()

app.exec()
