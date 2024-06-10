import sys
from PySide6 import QtCore as qtc
from PySide6.QtWidgets import QApplication, QMainWindow

#     pyside6-uic mainWindow.ui -o ui_mainWindow.py
#     pyside6-uic widgetWindow.ui -o ui_widgetWindow.py

from ui_mainWindow import Ui_MainWindow
# from ui_widgetWindow import Ui_Form
from widgetWindow import WidgetWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn_callWidget.clicked.connect(self.callWidget)
        self.ui.lbl_mainWindow.setText("I am being programatically set")

        # Reference the application window appWindow
        self.widget_window = WidgetWindow(self.ui.lbl_mainWindow.text())

    # BUTTONS
    def callWidget(self):
        self.widget_window.submitted.connect(self.update_messages)
        self.widget_window.show()
        print("callWidget")

    def calltoaction(self):
        print("I am call to Action")

    @qtc.Slot(str)
    def update_messages(self, message):
        if message == "Action":
            self.calltoaction()
        else:
            self.ui.lbl_mainWindow.setText(message)
