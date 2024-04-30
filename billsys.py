import tkinter as tk
from tkinter import ttk

def calculate():
    quantity = float(qty_text.get())
    price = float(price_text.get())
    total = quantity*price
    totel_text.delete(0, tk.END)
    totel_text.insert(0, total)


def add():
    grand_total = 0
    item = item_text.get()
    qty = qty_text.get()
    price = price_text.get()
    total = float(totel_text.get())
    
    
    table.insert("", tk.END, values=(item, qty, price, total))
    
    
    item_text.delete(0, tk.END)
    qty_text.delete(0, tk.END)
    price_text.delete(0, tk.END)
    totel_text.delete(0, tk.END)
    
    
    for item in table.get_children():
        values = table.item(item, 'values')
        ind_total = float(values[3])
        grand_total +=ind_total
        g_total.configure(text=f'Grand Total: {grand_total}')






window = tk.Tk()
window.title("Billing System")
window.geometry("820x500")


heading = tk.Label(window, text="Billing System", font=("Arial",30,), fg='white' ,bg='red' )
heading.pack(pady=20)

item_details = tk.Frame(window)
item_details.pack()

for col in range(4):
    item_details.columnconfigure(col, minsize=200)
    
    

item_label = tk.Label(item_details, text="Item Name", font=("arial", 15))
item_label.grid(row=0, column=0)

qty_label = tk.Label(item_details, text="Quantity", font=("arial", 15))
qty_label.grid(row=0, column=1)


price_label = tk.Label(item_details, text="Price", font=("arial", 15))
price_label.grid(row=0, column=2)

total_label = tk.Label(item_details, text="Total", font=("arial", 15))
total_label.grid(row=0, column=3)




item_text = tk.Entry(item_details, font=("arial, 15"), width=15)
item_text.grid(row=1, column=0)


qty_text = tk.Entry(item_details, font=("arial, 15"), width=15, justify="right")
qty_text.grid(row=1, column=1)


price_text = tk.Entry(item_details, font=("arial, 15"), width=15, justify="right")
price_text.grid(row=1, column=2)


totel_text = tk.Entry(item_details, font=("arial, 15"), width=15, justify="right")
totel_text.grid(row=1, column=3)



calc_btn = tk.Button(item_details, text="calculator", font=("arial, 15"), bg='blue', fg='white', command=calculate)
calc_btn.grid(row=2, column=2,pady=10, padx=10)


add_btn = tk.Button(item_details, text="add", font=("arial, 15"), bg='blue', fg='white', command=add)
add_btn.grid(row=2, column=3,pady=10, padx=10)


table = ttk.Treeview(item_details, columns=('itam', 'qty', 'price', 'total'), show='headings')
table.grid(row=3, column=0, columnspan=4, padx=5, pady=5)
table.heading("#1", text='Item Name')
table.heading("#2", text='Quantity')
table.heading("#3", text='Price')
table.heading("#4", text='Total')

g_total = tk.Label(window, text='Grand Total:', fg='green', font=('arial,18'))
g_total.pack(pady=5)







window.mainloop()