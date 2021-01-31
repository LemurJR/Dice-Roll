import random
import tkinter as tk

# initialize window

root = tk.Tk()
root.resizable(width=False, height=False)
root.geometry('150x100')
root.title('Dice-Roll')

# heading
tk.Label(root, text='Dice Roll', font='arial 15 bold').pack()


# variables

numbers = [1, 2, 3, 4, 5, 6]


# dice roll function
rol_sum = tk.StringVar()


def Diceroll():
    dice_sum = random.choice(numbers)

    rol_sum.set(dice_sum)


# dice roll button
tk.Button(root, text='Roll the Dice!', command=Diceroll).pack()

# dice roll entry
tk.Entry(root, textvariable=rol_sum).pack()

root.mainloop()
