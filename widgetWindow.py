from PySide6 import QtCore as qtc
from PySide6.QtWidgets import QWidget
from ui_widgetWindow import Ui_Form

#     pyside6-uic widgetWindow.ui -o ui_widgetWindow.py


class WidgetWindow(QWidget, Ui_Form):

    submitted = qtc.Signal(str)

    def __init__(self, message):
        super().__init__()
        self.uiw = Ui_Form()
        self.uiw.setupUi(self)

        self.uiw.btn_print.clicked.connect(self.btn_print_clicked)
        self.uiw.btn_action.clicked.connect(self.btn_action_clicked)

    @qtc.Slot()
    def btn_print_clicked(self):
        print("btn_print_clicked")
        self.submitted.emit("I am just another setting")

    @qtc.Slot()
    def btn_action_clicked(self):
        print("btn_action_clicked")
        self.submitted.emit("Action")


