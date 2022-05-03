# pip upgrade

import os

# Python's de facto standard GUI
import tkinter as tk 

root = tk.Tk()

# Initialize canvas or window ratio
canvas1 = tk.Canvas(root, width = 350, height = 300, bg = '#4B8BBE', relief = 'raised')
canvas1.pack()

# Header name
header = tk.Label(root, text = 'Package Manager Upgrade ', bg = '#4B8BBE')
header.config(font = ('arial', 20))

# Create window
canvas1.create_window(180, 80, window = header)


def upgradePIP():
    """Launches terminal"""
    os.system('start cmd /k python.exe -m pip install --upgrade pip') 
    
upgradeButton = tk.Button(text='Upgrade PIP', command=upgradePIP, bg='#FFE873', fg='black', font=('arial', 12, 'bold'))
canvas1.create_window(170, 150, window=upgradeButton)


root.mainloop()
