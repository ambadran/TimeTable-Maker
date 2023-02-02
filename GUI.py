from tkinter import *
from tkinter import filedialog as fd

def doNothing():
    pass


root = Tk()

root.title('TimeTable Maker')
root.geometry(f'{1200}x{600}+100+100')

menu = Menu(root, tearoff=False)
root.config(menu=menu)

fileMenu = Menu(menu, tearoff=False)  # Creating a menu inside a menu
menu.add_cascade(label="File", menu=fileMenu)  # Creates file button with dropdown, sub menu is the drop
fileMenu.add_command(label='open', command=doNothing)
fileMenu.add_separator()
fileMenu.add_command(label='quit', command=root.quit)

EditMenu = Menu(menu, tearoff=False)
menu.add_cascade(label='Edit', menu=EditMenu)
EditMenu.add_command(label='redo', command=doNothing)

openFilebutton = Button(root, text='Open File', command=fd.askopenfilename)
openFilebutton.pack()
filename = fd.askopenfilename()

root.mainloop()
















