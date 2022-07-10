'''
Simple slot-machine program
Three label objects + button.
By pressing a button, numbers randomly drop out in label objects
'''


import tkinter as tk
from tkinter import ttk
import random
from threading import Event


def win():
	'''
	changes style if the winning combination
	'''
	if lb1['text'] == lb2['text'] == lb3['text']:
		lb1['style'] = 'W2.TLabel'
		lb2['style'] = 'W2.TLabel'
		lb3['style'] = 'W2.TLabel'
		lb0['text'] = 'You WIN!'


def clear():
	'''
	clear labels
	'''
	lb0['text'] = ''
	lb1['style'] = 'B.TLabel'
	lb2['style'] = 'B.TLabel'
	lb3['style'] = 'B.TLabel'


def play():
	clear()
	# imitation of animation
	for i in range(15):
		lb1['text'] = random.randint(1, 9)
		if i <= 10:
			lb2['text'] = random.randint(1, 9)
		if i <= 5:
			lb3['text'] = random.randint(1, 9)
		Event().wait(0.1)
		root.update()
	win()


root = tk.Tk()
root.title('Slot machine')
root.geometry('600x300+100+200')
root.grid()
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

s = ttk.Style()
s.configure('B.TButton', font=('', 25))
s.configure('B.TLabel', font=('', 25), width=3, relief='solid', anchor="center")
s.configure('W2.TLabel', background='green', font=('', 25), width=3, relief='solid', anchor="center")
s.configure('W1.TLabel', font=('', 25), anchor="center", foreground='red')

fr = ttk.Frame(root)
fr.grid()
lb0 = ttk.Label(fr, style='W1.TLabel')
lb0.grid(row=0, pady=10, columnspan=3)
lb1 = ttk.Label(fr, text='7', style='B.TLabel')
lb1.grid(row=1, column=0, padx=3)
lb2 = ttk.Label(fr, text='7', style='B.TLabel')
lb2.grid(row=1, column=1, padx=3)
lb3 = ttk.Label(fr, text='7', style='B.TLabel')
lb3.grid(row=1, column=2, padx=3)

bt = ttk.Button(fr, text='Play!', style='B.TButton', command=play)
bt.grid(row=2, pady=10, columnspan=3)

root.mainloop()
