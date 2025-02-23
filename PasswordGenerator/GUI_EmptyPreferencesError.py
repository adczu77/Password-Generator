from PySide2.QtWidgets import QWidget
from ui_EmptyPreferencesError import Ui_Dialog

class EmptyPreferencesErrorDialog(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.connectOkButton()

    def connectOkButton(self):
        self.ui.pushButton.clicked.connect(self.close)                                                                                  