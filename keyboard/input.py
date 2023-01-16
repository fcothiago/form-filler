from pynput import keyboard

class shortcut():
    def __init__(self,keys,callback = lambda : ()):
        self.keys = keys
        self.__current__ = 0
        self.callback = callback

    def wait_keys(self):
        with keyboard.Listener(on_press=self.__press__,on_release=self.__release__) as Listener:
            Listener.join()

    def __press__(self,key):
        if self.__current__ > len(self.keys[-1]):
            self.callback()
            return False
        if(key.char == self.keys[self.__current__]):
            self.__current__ = self.__current__ + 1
        else:
            self.__current__ = 0

    def __release__(self,key):
        self.__current__ = 0
