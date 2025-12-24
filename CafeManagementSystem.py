import tkinter as tk
from tkinter import messagebox
import random

# ---------------- MENU (20+ ITEMS) ----------------
menu = {
    "Coffee": 40,
    "Cold Coffee": 60,
    "Espresso": 80,
    "Cappuccino": 90,
    "Latte": 100,
    "Tea": 20,
    "Green Tea": 30,
    "Cold Drink": 50,
    "Lemon Soda": 40,
    "Burger": 60,
    "Cheese Burger": 80,
    "Veg Sandwich": 50,
    "Grilled Sandwich": 70,
    "French Fries": 60,
    "Pizza": 120,
    "Garlic Bread": 80,
    "Pasta": 110,
    "Noodles": 100,
    "Momos": 70,
    "Chocolate Cake": 90,
    "Ice Cream": 60
}

TAX_PERCENT = 5
order_total = 0


# ---------------- FUNCTIONS ----------------
def add_item():
    global order_total

    item = item_var.get()
    qty = qty_entry.get()

    if item == "" or qty == "":
        messagebox.showerror("Error", "Select item and quantity")
        return

    if not qty.isdigit():
        messagebox.showerror("Error", "Quantity must be number")
        return

    qty = int(qty)
    cost = menu[item] * qty
    order_total += cost

    bill_text.insert(tk.END, f"{item:<18} x{qty:<2} ₹{cost}\n")
    total_label.config(text=f"Subtotal : ₹{order_total}")
    qty_entry.delete(0, tk.END)


def generate_bill():
    if order_total == 0:
        messagebox.showerror("Error", "Order something first")
        return

    table_no = random.randint(1, 20)
    messagebox.showinfo("Table Assigned", f"Table No {table_no} is assigned to you")

    tax = (order_total * TAX_PERCENT) / 100
    total = order_total + tax

    bill_text.insert(tk.END, "\n-----------------------------\n")
    bill_text.insert(tk.END, f"Table No : {table_no}\n")
    bill_text.insert(tk.END, f"Tax ({TAX_PERCENT}%) : ₹{tax:.2f}\n")
    bill_text.insert(tk.END, f"Total     : ₹{total:.2f}\n")
    bill_text.insert(tk.END, "-----------------------------\n")


def clear_all():
    global order_total
    order_total = 0
    bill_text.delete("1.0", tk.END)
    total_label.config(text="Subtotal : ₹0")


# ---------------- GUI ----------------
root = tk.Tk()
root.title("Cafe Management System")
root.geometry("650x600")  # FIXED SMALL SIZE
root.resizable(False, False)
root.configure(bg="#0F172A")  # Dark navy

# HEADER
tk.Label(
    root,
    text="☕ Cafe Management System",
    font=("Segoe UI", 20, "bold"),
    bg="#0F172A",
    fg="#38BDF8"
).pack(pady=10)

# ORDER FRAME
order_frame = tk.Frame(root, bg="#020617", bd=2, relief=tk.GROOVE)
order_frame.pack(padx=15, pady=10, fill="x")

tk.Label(order_frame, text="Item", bg="#020617", fg="white").grid(row=0, column=0, padx=10, pady=8)
item_var = tk.StringVar()
tk.OptionMenu(order_frame, item_var, *menu.keys()).grid(row=0, column=1)

tk.Label(order_frame, text="Quantity", bg="#020617", fg="white").grid(row=0, column=2, padx=10)
qty_entry = tk.Entry(order_frame, width=8)
qty_entry.grid(row=0, column=3)

tk.Button(
    order_frame,
    text="Add",
    bg="#22C55E",
    fg="black",
    width=12,
    command=add_item
).grid(row=0, column=4, padx=10)

# BILL FRAME
bill_frame = tk.Frame(root, bg="#020617", bd=2, relief=tk.GROOVE)
bill_frame.pack(padx=15, pady=10, fill="both", expand=True)

tk.Label(
    bill_frame,
    text="🧾 Bill",
    bg="#020617",
    fg="#FACC15",
    font=("Segoe UI", 14, "bold")
).pack()

bill_text = tk.Text(
    bill_frame,
    height=14,
    bg="#E5E7EB",
    fg="black",
    font=("Courier New", 10),
    bd=0
)
bill_text.pack(padx=8, pady=8, fill="both", expand=True)

# FOOTER
total_label = tk.Label(
    root,
    text="Subtotal : ₹0",
    font=("Segoe UI", 13, "bold"),
    bg="#0F172A",
    fg="#FACC15"
)
total_label.pack()

btn_frame = tk.Frame(root, bg="#0F172A")
btn_frame.pack(pady=10)

tk.Button(
    btn_frame,
    text="Generate Bill",
    bg="#38BDF8",
    fg="black",
    width=18,
    command=generate_bill
).grid(row=0, column=0, padx=10)

tk.Button(
    btn_frame,
    text="Clear",
    bg="#EF4444",
    fg="white",
    width=18,
    command=clear_all
).grid(row=0, column=1, padx=10)

root.mainloop()
