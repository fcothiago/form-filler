from pynput import keyboard
from pynput.keyboard import Controller
from pynput.keyboard._xorg import KeyCode
class shortcut():
    def __init__(self,keys,callback = lambda : ()):
        self.keys = keys
        self.__current__ = 0
        self.callback = callback

    def wait_keys(self):
        with keyboard.Listener(on_press=self.__press__,on_release=self.__release__) as Listener:
            Listener.join()
            for i in self.keys:
                Controller().release(i)
            self.callback()

    def __press__(self,key):
        if self.__current__ >= len(self.keys)-1:
            return False
        char =  key.char if isinstance(key,KeyCode) else key
        if(char == self.keys[self.__current__]):
            self.__current__ = self.__current__ + 1
        else:
            self.__current__ = 0

    def __release__(self,key):
        self.__current__ = 0
