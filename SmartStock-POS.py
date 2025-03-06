# main.py
import customtkinter as ctk
from tkinter import messagebox, TclError
import mysql.connector
from mysql.connector import Error
import cart

# Initialize global variables
grand_total = 0.0
cart_items = []

try:
    print("Attempting to connect to database...")
    database = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='smartstock_inventory'
    )
    print("Database connection successful!")
    cursor = database.cursor()

    root = ctk.CTk()
    root.title("Product Inventory")
    root.state('zoomed')

    # Vertical Navbar Frame (always visible)
    navbar_frame = ctk.CTkFrame(master=root, width=200, corner_radius=0)
    navbar_frame.pack(side=ctk.LEFT, fill=ctk.Y, padx=0, pady=0)

    logo_label = ctk.CTkLabel(master=navbar_frame, text="Logo", font=("Arial", 20, "bold"))
    logo_label.pack(pady=20)

    all_products_btn = ctk.CTkButton(master=navbar_frame, text="All Products", command=lambda: filter_products(None))
    all_products_btn.pack(pady=5, padx=10, fill=ctk.X)

    cpu_btn = ctk.CTkButton(master=navbar_frame, text="CPU", command=lambda: filter_products(1))
    cpu_btn.pack(pady=5, padx=10, fill=ctk.X)

    memory_btn = ctk.CTkButton(master=navbar_frame, text="Memory", command=lambda: filter_products(2))
    memory_btn.pack(pady=5, padx=10, fill=ctk.X)

    storage_btn = ctk.CTkButton(master=navbar_frame, text="Storage", command=lambda: filter_products(3))
    storage_btn.pack(pady=5, padx=10, fill=ctk.X)

    motherboard_btn = ctk.CTkButton(master=navbar_frame, text="Motherboard", command=lambda: filter_products(4))
    motherboard_btn.pack(pady=5, padx=10, fill=ctk.X)

    powersupply_btn = ctk.CTkButton(master=navbar_frame, text="Power Supply", command=lambda: filter_products(5))
    powersupply_btn.pack(pady=5, padx=10, fill=ctk.X)

    peripherals_btn = ctk.CTkButton(master=navbar_frame, text="Peripherals", command=lambda: filter_products(6))
    peripherals_btn.pack(pady=5, padx=10, fill=ctk.X)

    chasis_btn = ctk.CTkButton(master=navbar_frame, text="Chassis", command=lambda: filter_products(7))
    chasis_btn.pack(pady=5, padx=10, fill=ctk.X)

    # Main content frame (now for product items)
    main_frame = ctk.CTkFrame(master=root)
    main_frame.pack(side=ctk.LEFT, fill=ctk.BOTH, expand=True, padx=10, pady=10)

    product_display_frame = ctk.CTkScrollableFrame(master=main_frame, width=550)  # Moved from right to middle
    product_display_frame.pack(fill=ctk.BOTH, expand=True, padx=0, pady=0)

    # Right-side frame for entries and buttons
    right_frame = ctk.CTkFrame(master=root, width=300)
    right_frame.pack(side=ctk.RIGHT, fill=ctk.Y, padx=10, pady=10)

    entry_frame = ctk.CTkFrame(master=right_frame)
    entry_frame.pack(side=ctk.TOP, fill=ctk.X, pady=5)

    ctk.CTkLabel(master=entry_frame, text="Name:").pack(side=ctk.TOP, padx=(0, 2), pady=2)
    name_entry = ctk.CTkEntry(master=entry_frame, width=200, state='disabled')
    name_entry.pack(side=ctk.TOP, padx=5, pady=2)

    ctk.CTkLabel(master=entry_frame, text="Price:").pack(side=ctk.TOP, padx=(0, 2), pady=2)
    price_entry = ctk.CTkEntry(master=entry_frame, width=200)
    price_entry.pack(side=ctk.TOP, padx=5, pady=2)

    ctk.CTkLabel(master=entry_frame, text="Quantity:").pack(side=ctk.TOP, padx=(0, 2), pady=2)
    qty_entry = ctk.CTkEntry(master=entry_frame, width=200)
    qty_entry.pack(side=ctk.TOP, padx=5, pady=2)

    ctk.CTkLabel(master=entry_frame, text="Total:").pack(side=ctk.TOP, padx=(0, 2), pady=2)
    total_entry = ctk.CTkEntry(master=entry_frame, width=200, state='disabled')
    total_entry.pack(side=ctk.TOP, padx=5, pady=2)

    button_frame = ctk.CTkFrame(master=right_frame)
    button_frame.pack(side=ctk.TOP, pady=10)


    def toggle_cart():
        global cart_visible
        if not cart_visible:
            main_frame.pack_forget()
            right_frame.pack_forget()
            cart_frame.pack(side=ctk.LEFT, fill=ctk.BOTH, expand=True, padx=10, pady=10)
            cart.update_cart_display(cart_frame, cart_items, grand_total)
            cart_visible = True
            cart_btn.configure(text="Hide Cart")
        else:
            cart_frame.pack_forget()
            main_frame.pack(side=ctk.LEFT, fill=ctk.BOTH, expand=True, padx=10, pady=10)
            right_frame.pack(side=ctk.RIGHT, fill=ctk.Y, padx=10, pady=10)
            cart_visible = False
            cart_btn.configure(text="View Cart")


    refresh_btn = ctk.CTkButton(master=button_frame, text="Refresh Products",
                                command=lambda: [populate_product_display(), clear_selections()])
    refresh_btn.pack(side=ctk.TOP, padx=5, pady=5)

    add_btn = ctk.CTkButton(master=button_frame, text="Add to Cart",
                            command=lambda: [add_to_cart(), clear_selections()])
    add_btn.pack(side=ctk.TOP, padx=5, pady=5)

    cart_btn = ctk.CTkButton(master=button_frame, text="View Cart", command=toggle_cart)
    cart_btn.pack(side=ctk.TOP, padx=5, pady=5)

    # Cart Frame (hidden initially, initialized once)
    cart_frame = ctk.CTkFrame(master=root)
    cart_frame.pack_forget()
    cart.initialize_cart(cart_frame, cart_items, grand_total, lambda: toggle_cart())

    selected_item_button = None
    cart_visible = False


    def populate_product_display(category_id=None):
        global selected_item_button
        for widget in product_display_frame.winfo_children():
            widget.destroy()

        try:
            if category_id is None:
                query = "SELECT Name, Price FROM products"
                cursor.execute(query)
            else:
                query = "SELECT Name, Price FROM products WHERE CategoryID = %s"
                cursor.execute(query, (category_id,))
            rows = cursor.fetchall()
            print(f"Fetched {len(rows)} products for display (CategoryID: {category_id if category_id else 'All'})")
            if not rows:
                no_items_label = ctk.CTkLabel(master=product_display_frame, text="No products available",
                                              font=("Arial", 14))
                no_items_label.pack(pady=10)
            for row in rows:
                item_button = ctk.CTkButton(
                    master=product_display_frame,
                    text=f"{row[0]}\n${row[1]:.2f}",
                    command=lambda name=row[0], price=row[1]: select_product_item(name, price, item_button),
                    height=60,
                    corner_radius=5,
                    hover_color="lightblue",
                    fg_color="gray20",
                    text_color="white",
                    font=("Arial", 14)
                )
                item_button.pack(pady=5, padx=5, fill=ctk.X)
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Query failed: {err}")
            print(f"Query error: {err}")


    def select_product_item(name, price, button):
        global selected_item_button
        if selected_item_button and selected_item_button != button:
            selected_item_button.configure(fg_color="gray20")

        button.configure(fg_color="blue")
        selected_item_button = button

        name_entry.configure(state='normal')
        name_entry.delete(0, ctk.END)
        name_entry.insert(0, name)
        name_entry.configure(state='disabled')
        price_entry.delete(0, ctk.END)
        price_entry.insert(0, f"{price:.2f}")
        qty_entry.delete(0, ctk.END)
        qty_entry.insert(0, "1")
        total_entry.configure(state='normal')
        total_entry.delete(0, ctk.END)
        total_entry.insert(0, f"{price:.2f}")
        total_entry.configure(state='disabled')


    def clear_selections():
        global selected_item_button
        if selected_item_button:
            selected_item_button.configure(fg_color="gray20")
            selected_item_button = None


    def filter_products(category_id):
        try:
            print(f"Filtering products by CategoryID: {category_id if category_id else 'All'}")
            populate_product_display(category_id)
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Query failed: {err}")
            print(f"Query error: {err}")


    def add_to_cart():
        global grand_total, cart_items
        try:
            product = name_entry.get()
            price = float(price_entry.get())
            quantity = int(qty_entry.get())
            if not product:
                messagebox.showwarning("Missing Data", "Product name cannot be empty")
                return
            if price < 0:
                messagebox.showwarning("Invalid Price", "Price cannot be negative")
                return
            if quantity <= 0:
                messagebox.showwarning("Invalid Quantity", "Please enter a quantity greater than 0")
                return
            total = price * quantity
            grand_total += total
            cart_items.append((product, price, quantity, total))
            print(f"Added to cart: {product}, Total: {total:.2f}, Grand Total: {grand_total:.2f}")
            if cart_visible:
                cart.update_cart_display(cart_frame, cart_items, grand_total)
            name_entry.configure(state='normal')
            name_entry.delete(0, ctk.END)
            name_entry.configure(state='disabled')
            price_entry.delete(0, ctk.END)
            qty_entry.delete(0, ctk.END)
            total_entry.configure(state='normal')
            total_entry.delete(0, ctk.END)
            total_entry.configure(state='disabled')
        except ValueError:
            messagebox.showwarning("Invalid Input", "Please enter valid numbers for price and quantity")


    def update_total(*args):
        try:
            price = float(price_entry.get())
            qty = int(qty_entry.get())
            total = price * qty
            total_entry.configure(state='normal')
            total_entry.delete(0, ctk.END)
            total_entry.insert(0, f"{total:.2f}")
            total_entry.configure(state='disabled')
        except (ValueError, TclError):
            pass


    qty_entry.bind("<KeyRelease>", update_total)
    price_entry.bind("<KeyRelease>", update_total)

    # Populate product display on startup
    populate_product_display()

    root.mainloop()

except mysql.connector.Error as err:
    messagebox.showerror("Connection Error", f"Cannot connect to database: {err}")
    print(f"Connection error: {err}")

finally:
    if 'database' in locals():
        print("Closing database connection")
        database.close()