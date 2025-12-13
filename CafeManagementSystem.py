from tkinter import *
from tkinter import messagebox

menu = {
    "Coffee": 80,
    "Cold Coffee": 120,
    "Tea": 40,
    "Green Tea": 60,
    "Cold Drink": 50,
    "Lemon Soda": 70,
    "Burger": 120,
    "Cheese Burger": 150,
    "Veg Pizza": 200,
    "Cheese Pizza": 250,
    "Sandwich": 100,
    "Grilled Sandwich": 130,
    "Pasta": 150,
    "White Sauce Pasta": 180,
    "French Fries": 90,
    "Momos": 110,
    "Paneer Roll": 140,
    "Ice Cream": 80,
    "Brownie": 100
}

order = {}

def add_item():
    try:
        item = item_var.get()
        qty = int(qty_var.get())
        if item == "":
            return
        if item in order:
            order[item] += qty
        else:
            order[item] = qty
        update_bill()
    except:
        pass

def update_bill():
    bill_text.delete(1.0, END)
    total = 0
    for item, qty in order.items():
        price = menu[item] * qty
        total += price
        bill_text.insert(END, f"{item:<20}{qty:<10}{price}\n")
    gst = total * 0.05
    final = total + gst
    total_var.set(final)

def clear_order():
    order.clear()
    bill_text.delete(1.0, END)
    total_var.set(0)

def place_order():
    if len(order) == 0:
        messagebox.showwarning("Warning", "No items selected")
        return
    messagebox.showinfo("Thank You", "Thank you for ordering!\nYour order is placed successfully.")
    clear_order()

root = Tk()
root.title("Cafe Management System")
root.geometry("900x650")
root.configure(bg="#2c2f33")

Label(root, text="Welcome to Our Cafe", font=("Helvetica", 22, "bold"), bg="#2c2f33", fg="#f5c542").pack(pady=10)
Label(root, text="Fresh Food • Hot Coffee • Great Taste", font=("Arial", 12), bg="#2c2f33", fg="white").pack(pady=5)

main_frame = Frame(root, bg="#2c2f33")
main_frame.pack(pady=10)

left_frame = Frame(main_frame, bg="#23272a", padx=20, pady=20)
left_frame.grid(row=0, column=0, padx=20)

right_frame = Frame(main_frame, bg="#23272a", padx=20, pady=20)
right_frame.grid(row=0, column=1, padx=20)

Label(left_frame, text="Select Item", bg="#23272a", fg="white", font=("Arial", 12)).grid(row=0, column=0, pady=5)
Label(left_frame, text="Quantity", bg="#23272a", fg="white", font=("Arial", 12)).grid(row=0, column=1, pady=5)

item_var = StringVar()
item_var.set(list(menu.keys())[0])
qty_var = StringVar()

OptionMenu(left_frame, item_var, *menu.keys()).grid(row=1, column=0, padx=5)
Entry(left_frame, textvariable=qty_var).grid(row=1, column=1, padx=5)

Button(left_frame, text="Add Item", bg="#f5c542", fg="black", width=18, command=add_item).grid(row=2, column=0, columnspan=2, pady=15)

Label(right_frame, text="Bill Details", bg="#23272a", fg="#f5c542", font=("Arial", 14)).pack(pady=5)
bill_text = Text(right_frame, height=18, width=45, bg="#1e2124", fg="white")
bill_text.pack()

bottom_frame = Frame(root, bg="#2c2f33")
bottom_frame.pack(pady=10)

total_var = DoubleVar()
Label(bottom_frame, text="Total Amount (Including GST)", bg="#2c2f33", fg="white", font=("Arial", 12)).grid(row=0, column=0, padx=10)
Entry(bottom_frame, textvariable=total_var, state="readonly", width=20, bg="#f5c542", fg="black", font=("Arial", 12, "bold")).grid(row=0, column=1)

btn_frame = Frame(root, bg="#2c2f33")
btn_frame.pack(pady=10)

Label(root, text="Thank You for Visiting Our Cafe", bg="#2c2f33", fg="#f5c542", font=("Arial", 11)).pack(pady=10)

Button(btn_frame, text="Place Order", bg="#43b581", fg="white", width=18, command=place_order).grid(row=0, column=0, padx=15)
Button(btn_frame, text="Clear Order", bg="#f04747", fg="white", width=18, command=clear_order).grid(row=0, column=1, padx=15)

root.mainloop()
