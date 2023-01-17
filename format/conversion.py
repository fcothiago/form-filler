from pynput.keyboard import Key

def reserved():
    return {'tab' : '\t',\
            'endl' : '\n'}

def convert(key):
    if key == '\t':
        return Key.tab
    else:
        return key