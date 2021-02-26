#%%
from tkinter import *
from tkinter import filedialog
from openpyxl.workbook import Workbook
from openpyxl import load_workbook
import nupur as bg



def get_file_path():
    global file_path
    # Open and return file path
    file_path= filedialog.askopenfilename(title = "Select A File", filetypes = (("type1", "*.png"), ("type2", "*.jpg"),("type3","*jpeg")))
    l1 = Label(window, text = "File path: " + file_path).pack()

def submit():
    bg.background(file_path)
window = Tk()
window.title("Image to Text")

b1 = Button(window, text = "Open File", command = get_file_path).pack(side=LEFT)
b2 = Button(window, text= "Submit", command= submit).pack(padx = 20,pady=10, side=LEFT)
window.mainloop()

# %%
