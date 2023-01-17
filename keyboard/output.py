from pynput.keyboard import Key, Controller
from keyboard.input import shortcut
from format.conversion import convert,reserved

class autotype():
    def __init__(self,command=[Key.ctrl,"1"]):
        self.sc = shortcut(command)
        self.fields = dict()
        self.start_with = ""
        self.end_with = ""
        self.between = Key.tab
        self.keys = []
        self.__keyboard__ = Controller()

    def typeKey(self,key):
        self.__keyboard__.press(convert(key))
        self.__keyboard__.release(convert(key))
    
    def typeText(self,text):
        try:
            for i in text:
                self.typeKey(i)
        except:
            self.typeKey(text)

    def fill(self):
        self.sc.wait_keys()
        self.typeText(self.start_with)
        for i in self.keys:
            text = reserved()[i] if i in reserved().keys() else self.fields[i]
            self.typeText(text)
            self.typeText(self.between)
        self.typeText(self.end_with)
