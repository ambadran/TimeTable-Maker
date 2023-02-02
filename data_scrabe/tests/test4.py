import pyautogui as pag
import pyperclip as pc
import time
import pickle

swapWindow = lambda: pag.hotkey('command', 'tab')
scrollUp = lambda: pag.scroll('100')

swapWindow()
swapWindow()

img = 'start_anchor.png'

while not pag.locateOnScreen(img):
    print("didn't find the pic")

img = pag.locateOnScreen(img)

with open('test.pkl', 'wb') as f:
    pickle.dump(img, f)


swapWindow()



