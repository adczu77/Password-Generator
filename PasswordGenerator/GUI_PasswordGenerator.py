import sys
from ui_PasswordGenerator import Ui_MainWindow
from PySide2.QtWidgets import QApplication, QMainWindow
from Password import Password
from PasswordExceptions import EmptyPreferencesError
from GUI_EmptyPreferencesError import EmptyPreferencesErrorDialog
from GUI_SavingPassword import SavingPasswordDialog

class Window(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.connectGenerateButton()
        self.connectSavePasswordButton()
        self.password = Password(8)
        self.enableDefaultPreferences()
        self.emptyPreferencesErrorDialog = EmptyPreferencesErrorDialog()
        self.savingPasswordDialog = SavingPasswordDialog()
    
    def enableDefaultPreferences(self):
        self.ui.spinBox.setValue(self.password.getSignNumber())
        self.ui.checkBox.setChecked(True)
        self.ui.checkBox_2.setChecked(True)
        self.ui.checkBox_3.setChecked(True)
        self.ui.checkBox_4.setChecked(False)
    
    def setPreferences(self):
        self.password.setSmallLettersState(self.ui.checkBox.isChecked())
        self.password.setBigLettersState(self.ui.checkBox_2.isChecked())
        self.password.setNumbersState(self.ui.checkBox_3.isChecked())
        self.password.setSpecialSignsState(self.ui.checkBox_4.isChecked())
        self.password.setSignNumber(self.ui.spinBox.value())
        self.password.applyPreferences()

    def generate(self):
        self.setPreferences()
        try:
            self.password.generatePassword()
            self.ui.textBrowser_2.clear()
            self.ui.textBrowser_2.append(self.password.getGeneratedPassword()) 
        except EmptyPreferencesError:
            self.emptyPreferencesErrorDialog.show()

    def showSavePasswordDialog(self):
        if self.ui.textBrowser_2.toPlainText() == "":
            print("Jajco")
        else:
            self.savingPasswordDialog.show()                                                                                    

    def connectGenerateButton(self):
        self.ui.pushButton.clicked.connect(self.generate)
    
    def connectSavePasswordButton(self):
        self.ui.menuSave_Password.aboutToShow.connect(self.showSavePasswordDialog)

def guiMain(args):
    app = QApplication(args)
    window = Window()
    window.show()
    return app.exec_()

if __name__ == "__main__":
    guiMain(sys.argv)