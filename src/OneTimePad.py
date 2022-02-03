import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtGui import QTextCursor

import onetimepad
import numpy as np
import os
import pyperclip

qtcreator_file = "OneTimePad.ui" 
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtcreator_file)

imagename = ""
limit = 400 #limit for number of characters in input text box

class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.tabWidget.setCurrentIndex(1)
        self.quitButton.clicked.connect(self.on_Quitclick)
        self.encryptButton.clicked.connect(self.on_encyptclick)
        self.decryptButton.clicked.connect(self.on_decyptclick)
        self.makeButton.clicked.connect(self.make_pad)
        self.textEditIN.textChanged.connect(self.updatecounter)
        self.textEditIN.setText('Type your message to be encypted here - limit is 400 characters')  
        
        #load combo boxes with one-time pads available
        self.padCombo_1.clear()
        self.padCombo_2.clear()
        i = 0
        while os.path.exists("Storage/Pad%s.txt" % i):
            self.padCombo_1.addItem(f"{round(int(i),0)}")
            self.padCombo_2.addItem(f"{round(int(i),0)}")
            i += 1
        
    def on_decyptclick(self):
        print('Button decrypt clicked')        
        PadSel = self.padCombo_2.currentText()   
        with open("Storage/Pad%s.txt" % PadSel, 'r') as f:
            keypad = f.read()           
        msg = onetimepad.decrypt(self.textEditIN_2.toPlainText(), keypad)
        print("Plain text is ", msg)
        self.textEditOUT_2.setText(msg)  
        self.textEditOUT_2.repaint()  
        pyperclip.copy(msg) 

    def on_encyptclick(self):
        print('Button encrypt clicked')
        PadSel = self.padCombo_1.currentText()    
        with open("Storage/Pad%s.txt" % PadSel, 'r') as f:
            keypad = f.read()
        cipher = onetimepad.encrypt(self.textEditIN.toPlainText(), keypad)
        print("Cipher text is ", cipher)     
        self.textEditOUT.setText(cipher)  
        self.textEditOUT.repaint()  
        pyperclip.copy(cipher)         
 
    def make_pad(self):
        self.makeButton.setEnabled(False)
        n = 1024 ** 2  # 1 Mb of random text
        letters = np.array(list(chr(ord('a') + i) for i in range(26)))    
        chars = ''.join(np.random.choice(letters, n))
        i = 0
        while os.path.exists("Storage/Pad%s.txt" % i):
            i += 1

        with open("Storage/Pad%s.txt" % i, 'w+') as f:
            f.write(chars)
            print("One time pad %s written to disk " %i)

        #reload combo boxes with one-time pads available
        self.padCombo_1.clear()
        self.padCombo_2.clear()
        i = 0
        while os.path.exists("Storage/Pad%s.txt" % i):
            self.padCombo_1.addItem(f"{round(int(i),0)}")
            self.padCombo_2.addItem(f"{round(int(i),0)}")
            i += 1
        buttonReply = QMessageBox.question(self, 'NEW One Time Pad made', f"Pad number = {i-1}", QMessageBox.Ok | QMessageBox.Ok)
        self.makeButton.setEnabled(True)

    def on_Quitclick(self): #Quit button has been pressed         
        self.close()
        
    def updatecounter(self): 
        msg = self.textEditIN.toPlainText()
        global limit
        if len(msg)>limit:   
            print('Input testbox limit reached')
            TextData = msg[:limit]
            self.textEditIN.setText(TextData)  
            self.textEditIN.moveCursor(QTextCursor.End)
        msg = self.textEditIN.toPlainText()  
        self.wordcountlabel.setText(f"Characters remaining: {round(int(limit - len(msg)),0)} chars")    
 
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())