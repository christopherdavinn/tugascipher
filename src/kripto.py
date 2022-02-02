from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow
from PyQt5.uic import loadUi
import sys
import numpy as np

import extendedVigenere
import playfairCipher
import vignere_cipher


import uuid
import os


#initial load crypto GUI
class mainScreen(QMainWindow):
    def __init__(self):
        #setup screen
        super(mainScreen, self).__init__()
        loadUi("data/src/cryptogui.ui", self)
        
        #tombol input file
        self.inputBut.clicked.connect(self.inputFile)

        #tombol encrypt / decrypt
        self.cryptBut.clicked.connect(self.processFile)

        self.pathFile = ""

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

        res = ""

        # Encrypt
        if("encrypt" in cipherMethod.lower()):
            if cipherMethod == "Vignere Cipher Standard Encrypt":
                cipherText = vignere_cipher.vignere_cipher_standard_encrypt(pt, key)

                res += "Cipher Text:\n\n"
                res += cipherText
                res += "\n"
                res += ' '.join([cipherText[i: i+5] for i in range(0, len(cipherText), 5)])

            elif cipherMethod == "Extended Vignere Cipher Encrypt":
                if(self.pathFile != ""):
                    dir_path = os.path.dirname(os.path.realpath(__file__))
                    filename = "data/res/" + str(uuid.uuid4()) + os.path.splitext(self.pathFile)[1]

                    full_path = os.path.join(dir_path, filename)

                    success = extendedVigenere.extended_vignere_cipher_encrypt(
                        self.pathFile, 
                        key, 
                        full_path
                    )

                    if(success):
                        res += "Success Encrypt File, Please Check This Directory:\n"
                        res += full_path
                    else:
                        res += "Fail encrypt file"
                else:
                    res = "Please input file!"

            elif cipherMethod == "Playfair Cipher Encrypt":
                # encryption
                playfairSquare = playfairCipher.generatePlayfairSquare(key)
                res += playfairCipher.encrypt(pt, playfairSquare) + '\n\n'
                for i in range(len(playfairSquare)):
                    for j in range(len(playfairSquare[0])):
                        res += ('{} '.format(playfairSquare[i][j]))
                    res += '\n'   

            elif cipherAlgorithm == "Extended Vignere Cipher Encrypt":
                if(self.pathFile != ""):
                    dir_path = os.path.dirname(os.path.realpath(__file__))
                    filename = "data/res/" + str(uuid.uuid4()) + os.path.splitext(self.pathFile)[1]

                    full_path = os.path.join(dir_path, filename)

                    success = extendedVigenere.extended_vignere_cipher_encrypt(
                        self.pathFile, 
                        key, 
                        full_path
                    )

                    if(success):
                        res += "Success Encrypt File, Please Check This Directory:\n"
                        res += full_path
                    else:
                        res += "Fail encrypt file"
                else:
                    res = "Please input file!"

        else:
            if cipherMethod == "Vignere Cipher Standard Decrypt":
                plainText = vignere_cipher.vignere_cipher_standard_decrypt(pt, key)

                res += "Plain Text:\n\n"
                res += plainText
                res += "\n"
                res += ' '.join([plainText[i: i+5] for i in range(0, len(plainText), 5)])

            elif cipherMethod == "Extended Vignere Cipher Decrypt":
                if(self.pathFile != ""):
                    dir_path = os.path.dirname(os.path.realpath(__file__))
                    filename = "data/res/" + str(uuid.uuid4()) + os.path.splitext(self.pathFile)[1]

                    full_path = os.path.join(dir_path, filename)

                    success = extendedVigenere.extended_vignere_cipher_decrypt(
                        self.pathFile, 
                        key, 
                        full_path
                    )

                    if(success):
                        res += "Success Decrypt File, Please Check This Directory:\n"
                        res += full_path
                    else:
                        res += "Fail decrypt file"
                else:
                    res = "Please input file!"

            elif cipherMethod == "Playfair Cipher Decrypt":
                playfairSquare = playfairCipher.generatePlayfairSquare(key)
                res += playfairCipher.decrypt(pt, playfairSquare) + '\n\n'
                for i in range(len(playfairSquare)):
                    for j in range(len(playfairSquare[0])):
                        res += ('{} '.format(playfairSquare[i][j]))
                    res += '\n'

        if("Extended Vignere Cipher" not in cipherMethod):
            dir_path = os.path.dirname(os.path.realpath(__file__))
            filename = "data/res/" + str(uuid.uuid4()) + ".txt"

            full_path = os.path.join(dir_path, filename)
            f = open(full_path, 'w')
            f.write(res)

            res += "\n\n"
            res += "This Result Has Been Saved, Please Check This Directory:\n"
            res += full_path

        # Clear input
        self.outputTextArea.setPlainText(res)
        self.pathFile = ""
        self.inputBut.setText("Input File")

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
