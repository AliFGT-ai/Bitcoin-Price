import requests
import tkinter as tk
from datetime import datetime
from threading import Thread

def trackBitcoin():
    url = "https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,IQD,EUR"
    response = requests.get(url).json()
    price = response['USD']
    price2 = response['EUR']
    time = datetime.now().strftime("%H:%M:%S")

    labelPrice.config(text = str(price) + " $")
    labelPrice2.config(text=price2)
    labelTime.config(text = "Updated at: " + time)

    s = canvas.after(1000, trackBitcoin)
    Thread(target=s).start

canvas = tk.Tk()
canvas.geometry("400x500")
canvas.title('Bitcoin Tracker')

f1 = ("poppins", 24, 'bold')
f2 = ("poppins", 22, 'bold')
f22 = ('poppins', 20, 'bold')
f3 = ("poppins", 18, 'normal')

label = tk.Label(canvas, text='Bitcoin Price', font=f1)
label.pack(pady=20)

labelPrice = tk.Label(canvas, font=f2)
labelPrice.pack(pady=20)

labelPrice2 = tk.Label(canvas, font=f22)
labelPrice2.pack(pady=15)

labelTime = tk.Label(canvas, font=f3)
labelTime.pack(pady=20)

Thread(target=trackBitcoin()).start
canvas.mainloop()

