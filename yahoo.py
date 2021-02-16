from yahoo_fin import stock_info
from tkinter import *


def stock_price():
    price = stock_info.get_live_price('TSLA')
    Current_stock.set(price)


master = Tk()
Current_stock = StringVar()

Label(master, text="Stonks : TSLA").grid(row=0, sticky=W)
Label(master, text="Value: ").grid(row=3, sticky=W)

result2 = Label(master, text="", textvariable=Current_stock,
                ).grid(row=3, column=1, sticky=W)

mainloop()

