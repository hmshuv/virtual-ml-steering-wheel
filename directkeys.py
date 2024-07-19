# directkeys.py
from pynput.keyboard import Key, Controller

keyboard = Controller()

# Key codes
W = 'w'
A = 'a'
S = 's'
D = 'd'
Space = Key.space

def PressKey(key):
    keyboard.press(key)

def ReleaseKey(key):
    keyboard.release(key)
