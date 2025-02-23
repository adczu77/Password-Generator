import random
from PasswordExceptions import EmptyPreferencesError

class Password:
    def __init__(self, signNumber, smallLetters=True, bigLetters=True, numbers=True, specialSigns=False):
        self.signNumber = signNumber
        self.smallLetters = smallLetters
        self.bigLetters = bigLetters
        self.numbers = numbers
        self.specialSigns = specialSigns
        self.preferencesList = []
        self.generatedPassword = ""
    
    def getGeneratedPassword(self):
        return self.generatedPassword
    
    def getSignNumber(self):
        return self.signNumber
    
    def getSmallLettersState(self):
        return self.smallLetters

    def getBigLettersState(self):
        return self.bigLetters

    def getNumbersState(self):
        return self.numbers
    
    def getSpecialSignsState(self):
        return self.specialSigns

    def getPreferencesList(self):
        return self.preferencesList
    
    def setSignNumber(self, signNumber):
        self.signNumber = signNumber
    
    def setSmallLettersState(self, newSmallLettersState):
        self.smallLetters = newSmallLettersState
    
    def setBigLettersState(self, newBigLettersState):
        self.bigLetters = newBigLettersState
    
    def setNumbersState(self, newNumbersState):
        self.numbers = newNumbersState
    
    def setSpecialSignsState(self, newSpecialSignsState):
        self.specialSigns = newSpecialSignsState
    
    def setPreferencesList(self, newPreferencesList):
        self.preferencesList = newPreferencesList
    
    def applyPreferences(self):
        self.preferencesList = []
        if self.smallLetters == True:
            self.preferencesList.append(list(range(97, 122+1)))
        if self.bigLetters == True:
            self.preferencesList.append(list(range(65, 90+1)))
        if self.numbers == True:
            self.preferencesList.append(list(range(48, 57+1)))
        if self.specialSigns == True:
            specialSignsList = list(range(33,47+1))+list(range(58,64+1))+list(range(91,96+1))+list(range(123,126+1))
            self.preferencesList.append(specialSignsList)

    
    def generatePassword(self):
        self.generatedPassword = ""
        if self.preferencesList == []:
            raise EmptyPreferencesError()
        else:
            for i in list(range(1, self.signNumber+1)):
                category = random.choice(self.preferencesList)
                sign = chr(random.choice(category))
                self.generatedPassword += sign
