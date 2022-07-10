'''
VIEW FILE

A simple prototype of a TV controller in Python
'''

import tkinter as tk
from tkinter import ttk, messagebox
import pult_C as p_C

class C_view:
    def __init__(self, cont):
        '''
        :param cont: controller
        '''
        self.cont = cont(self)

    def show(self):
        '''
        Building and displaying the user's workspace
        '''

        # creates a workspace
        self.root = tk.Tk()
        self.root.title('Pult')

        # center the window
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        self.root.geometry(f'250x600+{(screen_width // 2) - 125}+{(screen_height // 2) - 300}')
        self.root.grid()
        self.root.grid_columnconfigure(0, weight=1)

        # creates the styles
        s = ttk.Style()
        s.configure('B.TButton', font=('', 15), width=10)
        s.configure('CH.TButton', font=('', 15), width=4)
        s.configure('num.TButton', font=('', 15), width=4)
        s.configure('Num.TLabel', font=('', 25), width=10, anchor=tk.N)
        s.configure('Txt.TLabel', font=('', 25), width=10, relief='solid', anchor=tk.N)
        s.configure('CH.TLabel', width=5, height=10, relief='solid', anchor=tk.N)

        # Creates the main geometry
        fr = ttk.Frame(self.root)
        fr.grid()

        # Labels for showing the result
        self.lb_n = ttk.Label(fr, style='Num.TLabel', text='---')
        self.lb_n.grid(row=0, pady=5, columnspan=3)
        self.lb_name = ttk.Label(fr, style='Txt.TLabel', text='---')
        self.lb_name.grid(row=1, pady=5, columnspan=3)

        # Control buttons
        ON_bt = ttk.Button(fr, text='ON/OFF', style='B.TButton', command=lambda: self.cont.start())
        ON_bt.grid(row=3, pady=5, columnspan=3)

        bt1 = ttk.Button(fr, text='1', style='num.TButton', command=lambda: self.cont.set(1))
        bt1.grid(row=4, column=0, pady=5, padx=5)
        bt2 = ttk.Button(fr, text='2', style='num.TButton', command=lambda: self.cont.set(2))
        bt2.grid(row=4, column=1, pady=5, padx=5)
        bt3 = ttk.Button(fr, text='3', style='num.TButton', command=lambda: self.cont.set(3))
        bt3.grid(row=4, column=2, pady=5, padx=5)

        bt4 = ttk.Button(fr, text='4', style='num.TButton', command=lambda: self.cont.set(4))
        bt4.grid(row=5, column=0, pady=5, padx=5)
        bt5 = ttk.Button(fr, text='5', style='num.TButton', command=lambda: self.cont.set(5))
        bt5.grid(row=5, column=1, pady=5, padx=5)
        bt6 = ttk.Button(fr, text='6', style='num.TButton', command=lambda: self.cont.set(6))
        bt6.grid(row=5, column=2, pady=5, padx=5)

        bt7 = ttk.Button(fr, text='7', style='num.TButton', command=lambda: self.cont.set(7))
        bt7.grid(row=6, column=0, pady=5, padx=5)
        bt8 = ttk.Button(fr, text='8', style='num.TButton', command=lambda: self.cont.set(8))
        bt8.grid(row=6, column=1, pady=5, padx=5)
        bt9 = ttk.Button(fr, text='9', style='num.TButton', command=lambda: self.cont.set(9))
        bt9.grid(row=6, column=2, pady=5, padx=5)

        # at the moment it's impossible to turn on the channel with the #10+ by number
        bt0 = ttk.Button(fr, text='0', style='num.TButton', command=lambda: self.cont.set(0), state='disabled')
        bt0.grid(row=7, column=1, pady=5, padx=5)

        ch_lb = ttk.Label(fr, style='CH.TLabel')
        ch_lb.grid(row=8, column=0, pady=5, padx=5, rowspan=2)
        bt_next = ttk.Button(ch_lb, text='CH+', style='CH.TButton', command=self.cont.next)
        bt_next.grid(row=8, pady=5, padx=5)
        bt_back = ttk.Button(ch_lb, text='CH-', style='CH.TButton', command=self.cont.prev)
        bt_back.grid(row=9, pady=5, padx=5)

        # No volume yet
        vol = ttk.Label(fr, style='CH.TLabel')
        vol.grid(row=8, column=2, pady=5, padx=5, rowspan=2)
        bt_vol_m = ttk.Button(vol, text='V+', style='CH.TButton', state='disabled')
        bt_vol_m.grid(row=8, column=0, pady=5, padx=5)
        bt_vol_l = ttk.Button(vol, text='V-', style='CH.TButton', state='disabled')
        bt_vol_l.grid(row=9, column=0, pady=5, padx=5)

        # Empty label for geometry
        lb_emp = ttk.Label(fr, style='Num.TLabel', text='')
        lb_emp.grid(row=10, pady=5, columnspan=3)

        # Entry form for setting channels by number or name
        chan = tk.StringVar()
        self.p_e = tk.Entry(fr, width=11, font=('', 25, 'bold'), textvariable=chan, justify='center')
        self.p_e.grid(row=11, pady=5, columnspan=3)
        inp_bt = ttk.Button(fr, text='OK', style='B.TButton', command=lambda: self.cont.find(chan.get()))
        inp_bt.grid(row=12, pady=5, columnspan=3)

        self.root.mainloop()

    def msg(self, info):
        '''
        error message
        '''
        messagebox.showerror(title='Error', message=info)

    def update(self, ch, num):
        '''
        View updating method
        :param ch: current channel name
        :param num: current channel number
        '''
        self.lb_name['text'] = ch
        self.lb_n['text'] = num

    def stop(self):
        self.root.destroy()

# Connecting to the controller
sony = C_view(p_C.Controller)

# starting
sony.show()