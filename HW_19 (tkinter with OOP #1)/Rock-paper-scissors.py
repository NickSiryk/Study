'''
A Class-based game using Tkinter as an interface
The following features:
1. Has a password entry form.
2. The user can choose between two games:
- rock-paper-scissors game
- rock-paper-scissors-lizard-spock game
'''


import tkinter as tk
from tkinter import ttk
import random

class Game:
	def __init__(self, root_o: tk.Tk):
		'''
		:param root_o: interpreter
		'''

		self.root = root_o

		# creates a workspace
		self.all_geom()

		# creates the styles
		self.s = ttk.Style()
		self.s.configure('B.TButton', font=('', 15))
		self.s.configure('TOP.TLabel', font=('', 25), width=20, anchor="center")
		self.s.configure('W.TLabel', background='green', font=('', 25), width=20, anchor="center")
		self.s.configure('L.TLabel', background='RED', font=('', 25), width=20, anchor="center")
		self.s.configure('WAIT.TLabel', font=('', 25), width=20, anchor="center")

		# the table of keys to determine the winner
		self.key = ((0, 2, 1, 2, 1),
					(1, 0, 2, 2, 1),
					(2, 1, 0, 1, 2),
					(1, 1, 2, 0, 2),
					(2, 2, 1, 1, 0))

	def exit(self):
		self.root.destroy()

	def all_geom(self):
		# code for creating game window
		self.root.title('Game')

		# center the window
		screen_width = self.root.winfo_screenwidth()
		screen_height = self.root.winfo_screenheight()
		self.root.geometry(f'700x400+{(screen_width//2)-350}+{(screen_height//2)-200}')

		# Window grid geometry
		self.root.grid()
		self.root.grid_rowconfigure(0, weight=1)
		self.root.grid_columnconfigure(0, weight=1)

	def set_pass(self, p_ans):
		'''
		Method to set the password
		:param p_ans: new password
		'''
		self.p_ans = p_ans

	def play(self):
		'''
		General start game method
		'''
		self.pass_check()

	def pass_check(self):
		'''
		Creates a password verification form
		'''

		self.p_word = tk.StringVar()
		self.p_fr = ttk.Frame(self.root)
		self.p_fr.grid()

		self.p_lb0 = ttk.Label(self.p_fr, style='TOP.TLabel', text='Enter password!')
		self.p_lb0.grid(row=0, pady=10)

		self.p_lb1 = ttk.Label(self.p_fr, style='WAIT.TLabel')
		self.p_lb1.grid(row=1, pady=10)

		self.p_e = tk.Entry(self.p_fr, width=20, font=('', 25, 'bold'), textvariable=self.p_word,
							show="*", justify='center')
		self.p_e.grid(row=2, pady=10)

		# Sends the entered password to the verification method by pressing a Label Button or hitting <Enter>
		self.root.bind('<Return>', self.pass_input)
		self.p_bt = ttk.Button(self.p_fr, text='OK', style='B.TButton', command=self.pass_input)
		self.p_bt.grid(row=3, pady=10)

		self.p_bt10 = ttk.Button(self.p_fr, text='Exit', style='B.TButton', command=self.exit)
		self.p_bt10.grid(row=4, pady=10)

	def pass_input(self, *args):
		'''
		Password verification method
		'''

		if self.p_word.get() == self.p_ans:
			self.p_lb1['text'] = 'Correct!'
			self.p_lb1['style'] = 'W.TLabel'
			self.p_bt.destroy()

			# Start game options  by pressing a Label Button or hitting <Enter>
			self.root.bind('<Return>', self.pass_stop)
			self.p_bt1 = ttk.Button(self.p_fr, text='Play!', style='B.TButton', command=self.pass_stop)
			self.p_bt1.grid(row=3, pady=10)
		else:
			self.p_lb1['text'] = 'Wrong!'
			self.p_lb1['style'] = 'L.TLabel'

	def pass_stop(self, *args):
		'''
		Method to starts playing
		'''

		# Destroys password form
		self.p_fr.destroy()

		# Calls method to create entering game window
		self.gameplay()

	def gameplay(self):
		'''
		Creating entering game window
		'''

		self.m_fr = ttk.Frame(self.root)
		self.m_fr.grid()
		self.m_lb0 = ttk.Label(self.m_fr, style='TOP.TLabel', text='Choose type')
		self.m_lb0.grid(row=0, pady=10, columnspan=2)

		# Button for rock-paper-scissors game
		self.m_bt = ttk.Button(self.m_fr, text='R-P-S', width=10, style='B.TButton', command=self.small)
		self.m_bt.grid(row=1, column=0, pady=10, padx=2)

		# Button for rock-paper-scissors-lizard-spock game
		self.m_bt1 = ttk.Button(self.m_fr, text='R-P-S-L-Sp', width=10, style='B.TButton', command=self.big)
		self.m_bt1.grid(row=1, column=1, pady=10, padx=2)

		# Exit button
		self.p_bt10 = ttk.Button(self.m_fr, text='Exit', style='B.TButton', command=self.exit)
		self.p_bt10.grid(row=2, pady=10, columnspan=2)

	def small(self):
		'''
		Rock-paper-scissors game
		'''
		# points counters
		self.p = 0
		self.c = 0

		# game type index for key-table
		self.game = 3

		# entering game window destroys and r-p-s game frame creates
		self.m_fr.destroy()

		self.g_fr = ttk.Frame(self.root)
		self.g_fr.grid()

		self.g_lb0 = ttk.Label(self.g_fr, style='WAIT.TLabel', text=' ')
		self.g_lb0.grid(row=0, pady=10, columnspan=3)
		self.g_lb00 = ttk.Label(self.g_fr, style='WAIT.TLabel', text=' ')
		self.g_lb00.grid(row=1, pady=10, columnspan=3)

		# Selection buttons
		self.g_bt = ttk.Button(self.g_fr, text='Rock', width=10, style='B.TButton', command=self.rock)
		self.g_bt.grid(row=2, column=0, pady=10, padx=2)
		self.g_bt1 = ttk.Button(self.g_fr, text='Paper', width=10, style='B.TButton', command=self.paper)
		self.g_bt1.grid(row=2, column=1, pady=10, padx=2)
		self.g_bt2 = ttk.Button(self.g_fr, text='Scissors', width=10, style='B.TButton', command=self.scissors)
		self.g_bt2.grid(row=2, column=2, pady=10, padx=2)

		# points labels
		self.g_lb1 = ttk.Label(self.g_fr, style='WAIT.TLabel', text=f'Player:{self.p} | Comp:{self.c}')
		self.g_lb1.grid(row=3, pady=10, columnspan=3)

		# Exit button
		self.g_bt5 = ttk.Button(self.g_fr, text='Back', width=10, style='B.TButton', command=self.back)
		self.g_bt5.grid(row=4, pady=10, columnspan=3)

	def big(self):
		'''
		Rock-paper-scissors-lizard-spock game
		'''
		# points counters
		self.p = 0
		self.c = 0

		# game type index for key-table
		self.game = 5

		# entering game window destroys and r-p-s-l-sp game frame creates
		self.m_fr.destroy()

		self.g_fr = ttk.Frame(self.root)
		self.g_fr.grid()

		self.g_lb0 = ttk.Label(self.g_fr, style='WAIT.TLabel', text=' ')
		self.g_lb0.grid(row=0, pady=10, columnspan=5)
		self.g_lb00 = ttk.Label(self.g_fr, style='WAIT.TLabel', text=' ')
		self.g_lb00.grid(row=1, pady=10, columnspan=5)

		# Selection buttons
		self.g_bt = ttk.Button(self.g_fr, text='Rock', width=10, style='B.TButton', command=self.rock)
		self.g_bt.grid(row=2, column=0, pady=10, padx=2)
		self.g_bt1 = ttk.Button(self.g_fr, text='Paper', width=10, style='B.TButton', command=self.paper)
		self.g_bt1.grid(row=2, column=1, pady=10, padx=2)
		self.g_bt2 = ttk.Button(self.g_fr, text='Scissors', width=10, style='B.TButton', command=self.scissors)
		self.g_bt2.grid(row=2, column=2, pady=10, padx=2)
		self.g_bt3 = ttk.Button(self.g_fr, text='Lizard', width=10, style='B.TButton', command=self.lizard)
		self.g_bt3.grid(row=2, column=3, pady=10, padx=2)
		self.g_bt4 = ttk.Button(self.g_fr, text='Spock', width=10, style='B.TButton', command=self.spock)
		self.g_bt4.grid(row=2, column=4, pady=10, padx=2)

		# points labels
		self.g_lb1 = ttk.Label(self.g_fr, style='WAIT.TLabel', text=f'Player:{self.p} | Comp:{self.c}')
		self.g_lb1.grid(row=3, pady=10, columnspan=5)

		# Exit button
		self.g_bt5 = ttk.Button(self.g_fr, text='Back', width=10, style='B.TButton', command=self.back)
		self.g_bt5.grid(row=4, pady=10, columnspan=5)

	def back(self):
		'''
		Exit from game to entry page
		'''
		self.g_fr.destroy()
		self.gameplay()

	def rock(self):
		# player's choice
		player = 0
		self.compare(player)

	def paper(self):
		# player's choice
		player = 2
		self.compare(player)

	def scissors(self):
		# player's choice
		player = 1
		self.compare(player)

	def lizard(self):
		# player's choice
		player = 3
		self.compare(player)

	def spock(self):
		# player's choice
		player = 4
		self.compare(player)

	def compare(self, p):
		'''
		Method to compare player's and copmuter's choices
		:param p: index of player's choice
		'''

		# Computer makes choice
		c = random.randint(0, self.game-1)
		if c == 0:
			self.g_lb0['text'] = 'Rock'
		elif c == 2:
			self.g_lb0['text'] = 'Paper'
		elif c == 1:
			self.g_lb0['text'] = 'Scissors'
		elif c == 3:
			self.g_lb0['text'] = 'Lizard'
		elif c == 4:
			self.g_lb0['text'] = 'Spock'

		# Key-table Comparing procedure with result display
		if self.key[p][c] == 0:
			self.g_lb00['text'] = 'DRAW!'
		elif self.key[p][c] == 2:
			self.g_lb00['text'] = 'You WIN!'
			self.p += 1
		else:
			self.g_lb00['text'] = 'You Loose!'
			self.c += 1

		# updates the score
		self.g_lb1['text'] = f'Player:{self.p} | Comp:{self.c}'


root_gl = tk.Tk()

# choose interpreter
g = Game(root_gl)

# set the password
g.set_pass('qwerty')
g.play()
root_gl.mainloop()