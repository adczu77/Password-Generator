from PySide2.QtWidgets import QWidget
from ui_SavingPassword import Ui_Dialog

class SavingPasswordDialog(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.connectSaveButton()

    def connectSaveButton(self):
        self.ui.pushButton.clicked.connect(self.close)                                                                                  