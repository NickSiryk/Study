import tkinter as tk

root = tk.Tk()
root.title('Null')
root.geometry('')
root.eval('tk::PlaceWindow . center')
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()


def task_one():
    '''
    Creates four tkinter panels and lays them out at the four corners of the monitor
    '''
    all = [tk.Tk() for i in range(4)]
    all[0].geometry('200x200+0+0')
    all[1].geometry(f'200x200+{screen_width - 200}+0')
    all[2].geometry(f'200x200+0+{screen_height - 200}')
    all[3].geometry(f'200x200+{screen_width - 200}+{screen_height - 200}')


def task_two():
    '''
    Creates tkinter panel in the center.
    '''
    all1 = tk.Tk()
    all1.title('Center')
    all1.geometry(f'150x150+{(screen_width//2)-75}+{(screen_height//2)-75}')


def task_three_1():
    '''
    Creates tkinter panel that occupy the entire screen in size
    '''
    root.attributes('-fullscreen', True)


def task_three_2():
    '''
    Creates tkinter panel that occupy the entire screen in size
    '''
    root.geometry(f'{screen_width}x{screen_height}+0+0')


def task_four():
    '''
    Creates tkinter panel that occupy the half of the screen in size
    '''
    four = tk.Tk()
    four.title('Four')
    four.geometry(f'{screen_width // 2}x{screen_height}+0+0')


def task_five():
    '''
    Creates two panels tkinter that will occupy the entire screen in height
    and at the same time be located next to each other?
    '''
    five_1 = tk.Tk()
    five_1.title('five_1')
    five_2 = tk.Tk()
    five_2.title('five_2')
    five_1.geometry(f'{screen_width // 2}x{screen_height}+0+0')
    five_2.geometry(f'{screen_width // 2}x{screen_height}+{screen_width // 2}+0')


# task_one()
# task_two()
# task_three_1()
# task_three_2()
# task_four()
# task_five()
root.mainloop()