import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtGui import QTextCursor

import onetimepad
import numpy as np
import os
import pyperclip
       
def otpDec(self):
    print('Button decrypt clicked')        
    PadSel = self.padList.currentText()   
    with open("Storage/Pad%s.txt" % PadSel, 'r') as f:
        keypad = f.read()           
    msg = onetimepad.decrypt(self.inputText.toPlainText(), keypad)
    print("Plain text is ", msg)
    self.outputText.setText(msg)  
    self.outputText.repaint()  
    pyperclip.copy(msg) 

def otpEnc(self):
    print('Button encrypt clicked')
    PadSel = self.padList.currentText()    
    with open("Storage/Pad%s.txt" % PadSel, 'r') as f:
        keypad = f.read()
    cipher = onetimepad.encrypt(self.inputText.toPlainText(), keypad)
    print("Cipher text is ", cipher)     
    self.outputText.setText(cipher)  
    self.outputText.repaint()  
    pyperclip.copy(cipher)         
 
def newPad(self):
    self.padBut.setEnabled(False)
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
    self.padList.clear()
    i = 0
    while os.path.exists("Storage/Pad%s.txt" % i):
        self.padList.addItem(f"{round(int(i),0)}")
        i += 1
    buttonReply = QMessageBox.question(self, 'NEW One Time Pad made', f"Pad number = {i-1}", QMessageBox.Ok | QMessageBox.Ok)
    self.padBut.setEnabled(True)
