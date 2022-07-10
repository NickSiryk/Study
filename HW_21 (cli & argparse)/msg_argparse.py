# -*- coding: utf-8 -*-

'''
A script that takes a phrase and prints it out as a text in form.
It is possible to change the message display delay through the `-t` key.
'''
import tkinter as tk
import argparse
import sys

def kill():
    root.destroy()


parser = argparse.ArgumentParser(description='msg')

parser.add_argument('text', nargs='*', help='text', type=str)
parser.add_argument('-t', help='time', type=int)


args = parser.parse_args(sys.argv[1:])

if args.t == None:
    args.t = 5000

root = tk.Tk()
root.after(args.t, kill)
lb = tk.Label(text=args.text, font=('Courier', '22'))
lb.pack()
root.mainloop()