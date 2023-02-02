import pyautogui as pag
import pyperclip as pc
import time
import pickle
# from tkinter import *


swapWindow = lambda: pag.hotkey('command', 'tab')
scrollUp = lambda: pag.scroll('100')

def go_page():
    """ 
    Prepares the web page:
    swaps to to the web page and scrolls up
    """
    swapWindow()
    swapWindow()


searchboxPosX = 700 
searchboxPosY = 340

def search(subject_code):
    """
    :param subject_code: subject code you want to search for

    NOTE: This function runs assuming the page is fully scrolled up from the go_page function
    """


    pag.click(x=searchboxPosX, y=searchboxPosY)
    pag.click(x=searchboxPosX, y=searchboxPosY)
    pag.click(x=searchboxPosX, y=searchboxPosY)

    pag.press('backspace', presses=50)

    pag.typewrite(subject_code)
    pag.hotkey('return')



def get_raw_data(subjects_wanted, filename):

    first_time = True

    raw_data = []

    for i in subjects_wanted:
        # optional wait at the beginning
        time.sleep(1)

        # Searching for wanted subject
        if first_time:
            go_page()
            first_time = False
        scrollUp()
        time.sleep(0.3)
        search(i)

        # waiting for loading to finish
        # while pag.locateOnScreen('newIdea.png') != None:
        #     pass
        time.sleep(1.5)

        # getting the data 
        pag.scroll(-100)
        pag.moveTo(784, 871)
        pag.dragTo(10, 10, button='left')
        pag.moveTo(1292, 861)
        pag.hotkey('command', 'c')

        # Getting data
        time.sleep(0.5)
        output = pc.paste()

        
        # test for subjects with multiple timings
        if 'This class has multiple meeting times' in output:
            raise ValueError("MOSEEEEEEEEEBAAAAAAAAAAAA")
        else:
            raw_data.append(output)

    #swapping back
    swapWindow()

    with open(f'pickle_files/{filename}.pkl', 'wb') as f:
        pickle.dump(raw_data, f)
    return raw_data

if __name__ == '__main__':
    # subjects_wanted = ['ECEN312', 'ECEN314', 'ECEN315', 'ECEN324', 'ECEN302', 'SPAN101']
    # subjects_wanted = ['NSCI102']
    # subjects_wanted = ['CSCI463', 'ENGL201', 'CSCI305', 'CSCI451', 'CSCI419']
    # wanted_subjects = ['ENGL201']
    wanted_subjects = ['ECEN428', 'ECEN438', 'ECEN433', 'ECEN425', 'ECEN493']
    raw_data = get_raw_data(wanted_subjects, 'output2')
    for i in raw_data:
        print(i)










