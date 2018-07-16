# direct inputs
# source to this solution and code:
# http://stackoverflow.com/questions/14489013/simulate-python-keypresses-for-controlling-a-game
# http://www.gamespp.com/directx/directInputKeyboardScanCodes.html

import ctypes
import time
import win32api as wapi

SendInput = ctypes.windll.user32.SendInput

#18 Possible Keys

#D-Pad Keys - Unsure
W = 0x11 #D-Up
A = 0x1E #D-Left
S = 0x1F #D-Down
D = 0x20 #D-Right

#Functional Buttons
Q = 0x10 #A - Confirm / Snap
E = 0x12 #B - Back
SHIFT = 0x2A #Z-Trigger - Toggle Aiming
ENTER = 0x1C #Start - Just Start Things

R = 0x13 #Left Trigger - Unsure
F = 0x21 #Right Trigger - Unsure

#C-Pad Keys - Unsure
T = 0x14 #C-Up
Y = 0x15 #C-Left
G = 0x22 #C-Right
H = 0x23 #C-Down

#"Joystick" - Aiming
#Arrow Keys Correspond to Direction
UP = 0xC8
LEFT = 0xCB
RIGHT = 0xCD
DOWN = 0xD0

NK = "NK"

#KEYS = [W,A,S,D,Q,E,SHIFT,R,F,T,Y,G,H,UP,LEFT,RIGHT,DOWN,NK]
KEYS = [UP,LEFT,RIGHT,DOWN,Q]

keyList = ["\b"]
for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ 123456789,.'£$/\\":
    keyList.append(char)

def key_check():
    keys = []
    for key in keyList:
        if wapi.GetAsyncKeyState(ord(key)):
            keys.append(key)
    return keys


# C struct redefinitions 
PUL = ctypes.POINTER(ctypes.c_ulong)
class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class HardwareInput(ctypes.Structure):
    _fields_ = [("uMsg", ctypes.c_ulong),
                ("wParamL", ctypes.c_short),
                ("wParamH", ctypes.c_ushort)]

class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time",ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                 ("mi", MouseInput),
                 ("hi", HardwareInput)]

class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]

# Actuals Functions

def PressKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def ReleaseKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008 | 0x0002, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def TapKey(hexKeyCode):
    PressKey(hexKeyCode)
    time.sleep(0.075)
    ReleaseKey(hexKeyCode)
    time.sleep(0.075)


if __name__ == '__main__':
    for i in range(25):
        TapKey(W)
