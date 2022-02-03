from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow
from PyQt5.uic import loadUi
import sys
import uuid
import os
import extendedVigenere
import playfairCipher
import vigenere

#initial load enigma GUI
class enigmaScreen(QDialog):
    def __init__(self):
        #setup enigma screen
        super(enigmaScreen, self).__init__()
        loadUi("data/ui/enigmaMachine.ui", self)

        self.backBut.clicked.connect(self.gotoCipher)

    def gotoCipher(self):
        cipherMachine = mainScreen()
        widget.addWidget(cipherMachine)
        widget.setCurrentIndex(widget.currentIndex()+1)

#initial cipher GUI(main screen)
class mainScreen(QMainWindow):
    def __init__(self):
        #setup cipher screen (main screen)
        super(mainScreen, self).__init__()
        loadUi("data/ui/cryptogui.ui", self)
    
        #tombol input file
        self.inputBut.clicked.connect(self.inputFile)
        #tombol encrypt / decrypt
        self.cryptBut.clicked.connect(self.processFile)
        #tombol switch to enigma machine
        self.enigmaBut.clicked.connect(self.gotoEnigma) 

        self.pathFile = ""

    def gotoEnigma(self):
        enigmaMachine = enigmaScreen()
        widget.addWidget(enigmaMachine)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def inputFile(self):
        file = QtWidgets.QFileDialog.getOpenFileName()
        self.pathFile = file[0]

        self.inputBut.setText(self.pathFile.split('/')[-1])

    def processFile(self):
        cipherMethod = self.cipheroption.currentText()
        pt = self.textInput.toPlainText()
        key = self.keyInput.toPlainText()

        if(self.pathFile != ""):
            ext = os.path.splitext(self.pathFile)[1]
            if(ext == ".txt"):
                f = open(self.pathFile)
                pt = f.read()
        if(len(key) == 0):
            return

        result = ""

#encrypt code
        if("encrypt" in cipherMethod.lower()):
            if cipherMethod == "Vigenere Cipher Standard Encrypt":
                cipherText = vigenere.vigenerestdEnc(pt, key)

                result += "Cipher Text:\n"
                result += cipherText
                result += "\n\nCipher (per 5): \n"
                result += ' '.join([cipherText[i: i+5] for i in range(0, len(cipherText), 5)])

            elif cipherMethod == "Extended Vigenere Cipher Encrypt":
                if(self.pathFile != ""):
                    directory = os.path.dirname(os.path.realpath(__file__))
                    filename = "data/output/" + str(uuid.uuid4()) + os.path.splitext(self.pathFile)[1]

                    full_path = os.path.join(directory, filename)

                    success = extendedVigenere.extvigenereEnc(
                        self.pathFile, 
                        key, 
                        full_path
                    )

                    if(success):
                        result += "Encrypt success!\n\n"
                        result += "Filename: %s" %(filename)
                    else:
                        result += "Fail encrypt file"
                else:
                    result = "Please input file!"

            elif cipherMethod == "Playfair Cipher Encrypt":
                # encryption
                playfairSquare = playfairCipher.generatePlayfairSquare(key)
                result += playfairCipher.encrypt(pt, playfairSquare) + '\n\n'
                for i in range(len(playfairSquare)):
                    for j in range(len(playfairSquare[0])):
                        result += ('{} '.format(playfairSquare[i][j]))
                    result += '\n'   

#decrypt code
        else:
            if cipherMethod == "Vigenere Cipher Standard Decrypt":
                pt = vigenere.vigenerestdDec(pt, key)

                result += "Plain Text:\n"
                result += pt
                result += "\n\nPlain Text (per 5): \n"
                result += ' '.join([pt[i: i+5] for i in range(0, len(pt), 5)])

            elif cipherMethod == "Extended Vigenere Cipher Decrypt":
                if(self.pathFile != ""):
                    directory = os.path.dirname(os.path.realpath(__file__))
                    filename = "data/output/" + str(uuid.uuid4()) + os.path.splitext(self.pathFile)[1]

                    full_path = os.path.join(directory, filename)

                    success = extendedVigenere.extvigenereDec(
                        self.pathFile, 
                        key, 
                        full_path
                    )

                    if(success):
                        result += "Decrypt success!\n\n"
                        result += "Filename: %s" %(filename)
                    else:
                        result += "Fail decrypt file"
                else:
                    result = "Please input file!"

            elif cipherMethod == "Playfair Cipher Decrypt":
                playfairSquare = playfairCipher.generatePlayfairSquare(key)
                result += playfairCipher.decrypt(pt, playfairSquare) + '\n\n'
                for i in range(len(playfairSquare)):
                    for j in range(len(playfairSquare[0])):
                        result += ('{} '.format(playfairSquare[i][j]))
                    result += '\n'

        if("Extended Vigenere Cipher" not in cipherMethod):
            directory = os.path.dirname(os.path.realpath(__file__))
            filename = "data/output/" + str(uuid.uuid4()) + ".txt"

            full_path = os.path.join(directory, filename)
            f = open(full_path, 'w')
            f.write(result)

            result += "\n\n\n\n"
            result += "Success!\n\n"
            result += "Filename: %s" %(filename)

#refresh input
        self.outputTB.setPlainText(result)
        self.pathFile = ""
        self.inputBut.setText("Input your file here!")

#main prog
app = QApplication(sys.argv)
main = mainScreen()
widget = QtWidgets.QStackedWidget()
widget.addWidget(main)
widget.setFixedWidth(1000)
widget.setFixedHeight(850)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")