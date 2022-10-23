import pygame, tkinter as tk
from tkinter import messagebox

def OpenMessageBox():
    
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("Title", "Message")