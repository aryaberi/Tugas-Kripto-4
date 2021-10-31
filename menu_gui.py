#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 5.0.3
#  in conjunction with Tcl version 8.6
#    Oct 01, 2021 05:15:11 PM +07  platform: Windows NT

import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import menu_gui_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    menu_gui_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    menu_gui_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#ffffff'  # X11 color: 'white'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("600x450+720+298")
        top.minsize(148, 1)
        top.maxsize(1924, 1055)
        top.resizable(1, 1)
        top.title("New Toplevel")
        top.configure(background="#ffffff")

        self.ButtonRSA = tk.Button(top)
        self.ButtonRSA.place(relx=0.367, rely=0.244, height=33, width=150)
        self.ButtonRSA.configure(activebackground="#ececec")
        self.ButtonRSA.configure(activeforeground="#000000")
        self.ButtonRSA.configure(background="#ffffff")
        self.ButtonRSA.configure(disabledforeground="#a3a3a3")
        self.ButtonRSA.configure(font="-family {Segoe UI} -size 9")
        self.ButtonRSA.configure(foreground="#000000")
        self.ButtonRSA.configure(highlightbackground="#ffffff")
        self.ButtonRSA.configure(highlightcolor="black")
        self.ButtonRSA.configure(pady="0")
        self.ButtonRSA.configure(text='''Algoritma RSA''')
        self.ButtonRSA.configure(command=lambda: menu_gui_support.openRSAWindow())

        self.ButtonElgamal = tk.Button(top)
        self.ButtonElgamal.place(relx=0.367, rely=0.333, height=33, width=150)
        self.ButtonElgamal.configure(activebackground="#ececec")
        self.ButtonElgamal.configure(activeforeground="#000000")
        self.ButtonElgamal.configure(background="#ffffff")
        self.ButtonElgamal.configure(disabledforeground="#a3a3a3")
        self.ButtonElgamal.configure(font="-family {Segoe UI} -size 9")
        self.ButtonElgamal.configure(foreground="#000000")
        self.ButtonElgamal.configure(highlightbackground="#ffffff")
        self.ButtonElgamal.configure(highlightcolor="black")
        self.ButtonElgamal.configure(pady="0")
        self.ButtonElgamal.configure(text='''Algoritma Elgamal''')
        self.ButtonElgamal.configure(command=lambda: menu_gui_support.openElgamalWindow())
