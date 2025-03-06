# cart.py
import customtkinter as ctk
from tkinter import messagebox

def initialize_cart(cart_frame, items, total, toggle_callback):
    global cart_items, grand_total
    cart_items = items
    grand_total = total

    cart_content = ctk.CTkScrollableFrame(master=cart_frame, width=550)
    cart_content.pack(fill=ctk.BOTH, expand=True, padx=10, pady=10)

    grand_total_frame = ctk.CTkFrame(master=cart_frame)
    grand_total_frame.pack(fill=ctk.X, padx=10, pady=5)

    grand_total_label = ctk.CTkLabel(master=grand_total_frame, text="Grand Total:")
    grand_total_label.pack(side=ctk.LEFT, padx=(0, 2))

    grand_total_entry = ctk.CTkEntry(master=grand_total_frame, width=100, state='disabled')
    grand_total_entry.pack(side=ctk.LEFT, padx=5)
    grand_total_entry.insert(0, f"{grand_total:.2f}")

    back_btn = ctk.CTkButton(master=grand_total_frame, text="Back", command=toggle_callback)
    back_btn.pack(side=ctk.RIGHT, padx=5)

    update_cart_display(cart_frame, cart_items, grand_total)

def update_cart_display(cart_frame, items, total):
    global cart_items, grand_total
    cart_items = items
    grand_total = total

    cart_content = cart_frame.winfo_children()[0]
    for widget in cart_content.winfo_children():
        widget.destroy()

    for idx, (product, price, quantity, item_total) in enumerate(cart_items):
        item_frame = ctk.CTkFrame(master=cart_content)
        item_frame.pack(fill=ctk.X, pady=5)

        item_label = ctk.CTkLabel(
            master=item_frame,
            text=f"{product}    ${price:.2f}    ${item_total:.2f}",
            font=("Arial", 14),
            anchor="w",
            width=300
        )
        item_label.pack(side=ctk.LEFT, padx=5)

        qty_frame = ctk.CTkFrame(master=item_frame)
        qty_frame.pack(side=ctk.RIGHT, padx=5)

        minus_btn = ctk.CTkButton(
            master=qty_frame,
            text="-",
            width=30,
            command=lambda i=idx: subtract_quantity(i, cart_frame)
        )
        minus_btn.pack(side=ctk.LEFT, padx=2)

        qty_display = ctk.CTkLabel(
            master=qty_frame,
            text=str(quantity),
            width=50,
            font=("Arial", 14),
            justify="center"
        )
        qty_display.pack(side=ctk.LEFT, padx=2)

        plus_btn = ctk.CTkButton(
            master=qty_frame,
            text="+",
            width=30,
            command=lambda i=idx: add_quantity(i, cart_frame)
        )
        plus_btn.pack(side=ctk.LEFT, padx=2)

        delete_btn = ctk.CTkButton(
            master=qty_frame,
            text="Delete",
            width=60,
            fg_color="red",
            hover_color="darkred",
            command=lambda i=idx: remove_item(i, cart_frame)
        )
        delete_btn.pack(side=ctk.LEFT, padx=5)

    grand_total_frame = cart_frame.winfo_children()[1]
    grand_total_entry = grand_total_frame.winfo_children()[1]
    grand_total_entry.configure(state='normal')
    grand_total_entry.delete(0, ctk.END)
    grand_total_entry.insert(0, f"{total:.2f}")
    grand_total_entry.configure(state='disabled')

def subtract_quantity(index, cart_frame):
    global cart_items, grand_total
    product, price, quantity, item_total = cart_items[index]
    if quantity > 1:
        new_quantity = quantity - 1
        new_total = price * new_quantity
        grand_total = grand_total - item_total + new_total
        cart_items[index] = (product, price, new_quantity, new_total)
        update_cart_display(cart_frame, cart_items, grand_total)

def add_quantity(index, cart_frame):
    global cart_items, grand_total
    product, price, quantity, item_total = cart_items[index]
    new_quantity = quantity + 1
    new_total = price * new_quantity
    grand_total = grand_total - item_total + new_total
    cart_items[index] = (product, price, new_quantity, new_total)
    update_cart_display(cart_frame, cart_items, grand_total)

def remove_item(index, cart_frame):
    global cart_items, grand_total
    item_total = cart_items[index][3]
    grand_total -= item_total
    cart_items.pop(index)
    update_cart_display(cart_frame, cart_items, grand_total)
    if not cart_items:
        cart_frame.pack_forget()