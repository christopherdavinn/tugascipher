import json
from PyQt5 import QtCore, QtWidgets
import sys
import numpy as np
import affineCipher
import extendedVigenere
import fullVigenere
import hill_cipher
import playfairCipher
import vignere_cipher

import uuid
import os


# sys.path.append('/src')


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1129, 868)
        MainWindow.setStyleSheet("background-color: rgb(21, 45, 53);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(420, 10, 321, 71))
        self.label.setStyleSheet("background-color: rgb(52, 91, 99);\n"
                                 "font-family: \"Cascadia Code SemiBold\";\n"
                                 "border: 2px solid black;\n"
                                 "border-radius: 5px;\n"
                                 "font-size: 10px;\n"
                                 "color: #D4ECDD;")
        self.label.setObjectName("label")
        self.outputTextArea = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.outputTextArea.setGeometry(QtCore.QRect(150, 110, 841, 361))
        self.outputTextArea.setStyleSheet("background-color: #D4ECDD;\n"
                                          "font-size: 15px;\n"
                                          "font-weight: bold;\n"
                                          "border-radius: 20px;\n"
                                          "border: 3px solid black;\n"
                                          "font: 75 18pt \"Cascadia Code\";\n"
                                          "padding: 10px;\n"
                                          "color: #112031")
        self.outputTextArea.setPlainText("")
        self.outputTextArea.setObjectName("outputTextArea")
        self.cipherAlgorithmComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.cipherAlgorithmComboBox.setGeometry(
            QtCore.QRect(580, 660, 391, 31))
        self.cipherAlgorithmComboBox.setStyleSheet("background-color: rgb(212, 236, 221);\n"
                                                   "font: 75 10pt \"Cascadia Code\";\n"
                                                   "padding-left: 10px;\n"
                                                   "border: none;")
        self.cipherAlgorithmComboBox.setObjectName("cipherAlgorithmComboBox")
        self.cipherAlgorithmComboBox.addItem("")
        self.cipherAlgorithmComboBox.addItem("")
        self.cipherAlgorithmComboBox.addItem("")
        self.cipherAlgorithmComboBox.addItem("")
        self.cipherAlgorithmComboBox.addItem("")
        self.cipherAlgorithmComboBox.addItem("")
        self.cipherAlgorithmComboBox.addItem("")
        self.cipherAlgorithmComboBox.addItem("")
        self.cipherAlgorithmComboBox.addItem("")
        self.cipherAlgorithmComboBox.addItem("")
        self.cipherAlgorithmComboBox.addItem("")
        self.cipherAlgorithmComboBox.addItem("")
        self.cipherAlgorithmComboBox.addItem("")
        self.cipherAlgorithmComboBox.addItem("")
        self.encryptDecryptButton = QtWidgets.QPushButton(self.centralwidget)
        self.encryptDecryptButton.setGeometry(QtCore.QRect(580, 700, 391, 61))
        self.encryptDecryptButton.setStyleSheet("color: #D4ECDD;\n"
                                                "font: 75 10pt \"Cascadia Code\";\n"
                                                "border: 2px solid #D4ECDD;\n"
                                                "border-radius: 5px;")
        self.encryptDecryptButton.setObjectName("encryptDecryptButton")
        self.inputText = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.inputText.setGeometry(QtCore.QRect(160, 530, 401, 101))
        self.inputText.setStyleSheet("border: 2px solid #D4ECDD;\n"
                                     "border-radius: 5px;\n"
                                     "color: rgb(212, 236, 221);\n"
                                     "padding: 5px;\n"
                                     "font: 75 13pt \"Cascadia Code\";")
        self.inputText.setPlainText("")
        self.inputText.setObjectName("inputText")
        self.inputFileButton = QtWidgets.QPushButton(self.centralwidget)
        self.inputFileButton.setGeometry(QtCore.QRect(580, 530, 391, 111))
        self.inputFileButton.setStyleSheet("color: #D4ECDD;\n"
                                           "font: 75 20pt \"Cascadia Code\";\n"
                                           "border: 2px solid #D4ECDD;\n"
                                           "border-radius: 5px;")
        self.inputFileButton.setObjectName("inputFileButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(160, 500, 111, 21))
        self.label_2.setStyleSheet("color: #D4ECDD;\n"
                                   "font: 75 13pt \"Cascadia Code\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(160, 80, 111, 21))
        self.label_3.setStyleSheet("color: #D4ECDD;\n"
                                   "font: 75 13pt \"Cascadia Code\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(160, 640, 111, 21))
        self.label_4.setStyleSheet("color: #D4ECDD;\n"
                                   "font: 75 13pt \"Cascadia Code\";")
        self.label_4.setObjectName("label_4")
        self.inputText_2 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.inputText_2.setGeometry(QtCore.QRect(160, 670, 401, 101))
        self.inputText_2.setStyleSheet("border: 2px solid #D4ECDD;\n"
                                       "border-radius: 5px;\n"
                                       "color: rgb(212, 236, 221);\n"
                                       "padding: 5px;\n"
                                       "font: 75 13pt \"Cascadia Code\";")
        self.inputText_2.setPlainText("")
        self.inputText_2.setObjectName("inputText_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1129, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # Coding here....
        self.pathFile = ""
        self.matrix = fullVigenere.generateFullVigenereMatrix()
        self.inputFileButton.clicked.connect(self.inputFileHandler)

        # Submit event
        self.encryptDecryptButton.clicked.connect(self.encryptDecryptHandler)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # Add method here...
    def inputFileHandler(self):
        file = QtWidgets.QFileDialog.getOpenFileName()
        self.pathFile = file[0]

        self.inputFileButton.setText(self.pathFile.split('/')[-1])

    def encryptDecryptHandler(self):
        cipherAlgorithm = self.cipherAlgorithmComboBox.currentText()
        text = self.inputText.toPlainText()
        key = self.inputText_2.toPlainText()

        if(self.pathFile != ""):
            ext = os.path.splitext(self.pathFile)[1]
            if(ext == ".txt"):
                f = open(self.pathFile)
                text = f.read()

        if(len(key) == 0):
            return

        res = ""

        # Encrypt
        if("encrypt" in cipherAlgorithm.lower()):
            if cipherAlgorithm == "Vignere Cipher Standard Encrypt":
                cipherText = vignere_cipher.vignere_cipher_standard_encrypt(text, key)

                res += "Cipher Text:\n\n"
                res += cipherText
                res += "\n"
                res += ' '.join([cipherText[i: i+5] for i in range(0, len(cipherText), 5)])

            elif cipherAlgorithm == "Full Vignere Cipher Encrypt":
                res += fullVigenere.encrypt(text, key, self.matrix)
                res += "\n\n"

                for i in range(len(self.matrix)):
                    for j in range(len(self.matrix[0])):
                        res += ('{} '.format(self.matrix[i][j]))
                    res += '\n'

            elif cipherAlgorithm == "Auto Key Vignere Cipher Encrypt":
                cipherText, newKey = vignere_cipher.vignere_cipher_auto_key_encrypt(text, key)

                res += "Cipher Text:\n"
                res += cipherText
                res += "\n"
                res += ' '.join([cipherText[i: i+5] for i in range(0, len(cipherText), 5)])
                res += "\n\n"
                res += "New Key:\n"
                res += newKey

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

            elif cipherAlgorithm == "Playfair Cipher Encrypt":
                # encryption
                playfairSquare = playfairCipher.generatePlayfairSquare(key)
                res += playfairCipher.encrypt(text, playfairSquare) + '\n\n'
                for i in range(len(playfairSquare)):
                    for j in range(len(playfairSquare[0])):
                        res += ('{} '.format(playfairSquare[i][j]))
                    res += '\n'
                      
            elif cipherAlgorithm == "Affine Cipher Encrypt":
                # parsing key
                newKey = key.split(',')
                newKey = [int(item) for item in newKey]

                # decryption
                res += affineCipher.affineEncrypt(text, newKey)

            elif cipherAlgorithm == "Hill Cipher Encrypt":
                key = json.loads(key)
                if(isinstance(key, list)):
                    try:
                        key = np.array(key)
                        res += "Result:\n"
                        res += hill_cipher.hill_cipher_encrypt(text, key)
                    except:
                        res = "Dimensi key harus bisa membagi panjang text nya!"
                else:
                    res += "Please input valid key!"
        else:
            if cipherAlgorithm == "Vignere Cipher Standard Decrypt":
                plainText = vignere_cipher.vignere_cipher_standard_decrypt(text, key)

                res += "Plain Text:\n\n"
                res += plainText
                res += "\n"
                res += ' '.join([plainText[i: i+5] for i in range(0, len(plainText), 5)])

            elif cipherAlgorithm == "Full Vignere Cipher Decrypt":
                res += fullVigenere.decrypt(text, key, self.matrix)
                res += '\n\n'
                for i in range(len(self.matrix)):
                    for j in range(len(self.matrix[0])):
                        res += ('{} '.format(self.matrix[i][j]))
                    res += '\n'

            elif cipherAlgorithm == "Auto Key Vignere Cipher Decrypt":
                plainText = vignere_cipher.vignere_cipher_auto_key_decrypt(text, key)

                res += "Plain Text:\n\n"
                res += plainText
                res += "\n"
                res += ' '.join([plainText[i: i+5] for i in range(0, len(plainText), 5)])

            elif cipherAlgorithm == "Extended Vignere Cipher Decrypt":
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

            elif cipherAlgorithm == "Playfair Cipher Decrypt":
                playfairSquare = playfairCipher.generatePlayfairSquare(key)
                res += playfairCipher.decrypt(text, playfairSquare) + '\n\n'
                for i in range(len(playfairSquare)):
                    for j in range(len(playfairSquare[0])):
                        res += ('{} '.format(playfairSquare[i][j]))
                    res += '\n'

            elif cipherAlgorithm == "Affine Cipher Decrypt":
                # parsing key
                newKey = key.split(',')
                newKey = [int(item) for item in newKey]

                # decryption
                text = affineCipher.textCleaning(text)
                res += affineCipher.affineDecrypt(text, newKey)

            elif cipherAlgorithm == "Hill Cipher Decrypt":
                key = json.loads(key)
                if(isinstance(key, list)):
                    try:
                        key = np.array(key)
                        plainText = hill_cipher.hill_cipher_decrypt(text, key)
                        res += "Plain Text:\n\n"
                        res += plainText
                        res += "\n"
                        res += ' '.join([plainText[i: i+5] for i in range(0, len(plainText), 5)])
                    except:
                        res += "Dimensi key harus bisa membagi panjang text nya!"
                        res += "Panjang text sekarang = {}".format(len(hill_cipher.clean_text(text)))
                        res += "Dimensi key sekarang = {}".format(key.shape[0])
                else:
                    res += "Please input valid key!"

        if("Extended Vignere Cipher" not in cipherAlgorithm):
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
        self.inputFileButton.setText("Input File")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate(
            "MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Classic Cryptography</span></p></body></html>"))
        self.cipherAlgorithmComboBox.setItemText(0, _translate(
            "MainWindow", "Vignere Cipher Standard Encrypt"))
        self.cipherAlgorithmComboBox.setItemText(1, _translate(
            "MainWindow", "Vignere Cipher Standard Decrypt"))
        self.cipherAlgorithmComboBox.setItemText(
            2, _translate("MainWindow", "Full Vignere Cipher Encrypt"))
        self.cipherAlgorithmComboBox.setItemText(
            3, _translate("MainWindow", "Full Vignere Cipher Decrypt"))
        self.cipherAlgorithmComboBox.setItemText(4, _translate(
            "MainWindow", "Auto Key Vignere Cipher Encrypt"))
        self.cipherAlgorithmComboBox.setItemText(5, _translate(
            "MainWindow", "Auto Key Vignere Cipher Decrypt"))
        self.cipherAlgorithmComboBox.setItemText(6, _translate(
            "MainWindow", "Extended Vignere Cipher Encrypt"))
        self.cipherAlgorithmComboBox.setItemText(7, _translate(
            "MainWindow", "Extended Vignere Cipher Decrypt"))
        self.cipherAlgorithmComboBox.setItemText(
            8, _translate("MainWindow", "Playfair Cipher Encrypt"))
        self.cipherAlgorithmComboBox.setItemText(
            9, _translate("MainWindow", "Playfair Cipher Decrypt"))
        self.cipherAlgorithmComboBox.setItemText(
            10, _translate("MainWindow", "Affine Cipher Encrypt"))
        self.cipherAlgorithmComboBox.setItemText(
            11, _translate("MainWindow", "Affine Cipher Decrypt"))
        self.cipherAlgorithmComboBox.setItemText(
            12, _translate("MainWindow", "Hill Cipher Encrypt"))
        self.cipherAlgorithmComboBox.setItemText(
            13, _translate("MainWindow", "Hill Cipher Decrypt"))
        self.encryptDecryptButton.setText(
            _translate("MainWindow", "Encrypt / Decrypt"))
        self.inputFileButton.setText(_translate("MainWindow", "Input File"))
        self.label_2.setText(_translate("MainWindow", "Text Input"))
        self.label_3.setText(_translate("MainWindow", "Text Output"))
        self.label_4.setText(_translate("MainWindow", "Key Input"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
