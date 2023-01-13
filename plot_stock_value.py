from tkinter import *
import yahoo_fin.stock_info as si
import matplotlib.pyplot as plt

def get_stock_data():
    start_date = start_date_entry.get()
    end_date = end_date_entry.get()
    symbol = symbol_entry.get()
    stock_data = si.get_data(symbol, start_date=start_date, end_date=end_date)
    plt.plot(stock_data["close"])
    plt.xlabel("Date")
    plt.ylabel("Closing Price")
    plt.title(f"{symbol} Stock Price")
    plt.show()

root = Tk()
root.title("Stock Price Graph")

start_date_label = Label(root, text="Start Date (YYYY-MM-DD)")
start_date_label.grid(row=0, column=0)
start_date_entry = Entry(root)
start_date_entry.grid(row=0, column=1)

end_date_label = Label(root, text="End Date (YYYY-MM-DD)")
end_date_label.grid(row=1, column=0)
end_date_entry = Entry(root)
end_date_entry.grid(row=1, column=1)

symbol_label = Label(root, text="Stock Symbol")
symbol_label.grid(row=2, column=0)
symbol_entry = Entry(root)
symbol_entry.grid(row=2, column=1)

get_data_button = Button(root, text="Get Stock Data", command=get_stock_data)
get_data_button.grid(row=3, column=0, columnspan=2)

root.mainloop()
