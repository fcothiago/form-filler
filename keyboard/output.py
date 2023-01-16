from pynput.keyboard import Key, Controller
from keyboard.input import shortcut

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
        self.__keyboard__.press(key)
        self.__keyboard__.release(key)
    
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
            text = self.fields[i]
            self.typeText(text)
            self.typeText(self.between)
        self.typeText(self.end_with)
