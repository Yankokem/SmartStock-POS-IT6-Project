# main.py
import customtkinter as ctk
from tkinter import messagebox, TclError
from tkinter.ttk import Treeview
import mysql.connector
from mysql.connector import Error
import cart  # Import the cart module

# Initialize global grand_total
grand_total = 0.0
cart_items = []  # Shared cart list

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

    # Vertical Navbar Frame
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

    # Main content frame
    main_frame = ctk.CTkFrame(master=root)
    main_frame.pack(side=ctk.LEFT, fill=ctk.BOTH, expand=True, padx=10, pady=10)

    products_frame = ctk.CTkFrame(master=main_frame)
    products_frame.pack(side=ctk.TOP, fill=ctk.X, pady=(0, 5))

    products_tree = Treeview(products_frame, columns=("Product", "Price"), show="headings", height=10)
    products_tree.heading("Product", text="Product Name")
    products_tree.heading("Price", text="Price")
    products_tree.column("Product", width=400)
    products_tree.column("Price", width=100)
    products_tree.pack(fill=ctk.X)

    entry_frame = ctk.CTkFrame(master=main_frame)
    entry_frame.pack(side=ctk.TOP, fill=ctk.X, pady=5)

    ctk.CTkLabel(master=entry_frame, text="Name:").pack(side=ctk.LEFT, padx=(0, 2))
    name_entry = ctk.CTkEntry(master=entry_frame, width=200, state='disabled')
    name_entry.pack(side=ctk.LEFT, padx=5)

    ctk.CTkLabel(master=entry_frame, text="Price:").pack(side=ctk.LEFT, padx=(0, 2))
    price_entry = ctk.CTkEntry(master=entry_frame, width=80)
    price_entry.pack(side=ctk.LEFT, padx=5)

    ctk.CTkLabel(master=entry_frame, text="Quantity:").pack(side=ctk.LEFT, padx=(0, 2))
    qty_entry = ctk.CTkEntry(master=entry_frame, width=50)
    qty_entry.pack(side=ctk.LEFT, padx=5)

    ctk.CTkLabel(master=entry_frame, text="Total:").pack(side=ctk.LEFT, padx=(0, 2))
    total_entry = ctk.CTkEntry(master=entry_frame, width=80, state='disabled')
    total_entry.pack(side=ctk.LEFT, padx=5)

    button_frame = ctk.CTkFrame(master=main_frame)
    button_frame.pack(side=ctk.TOP, pady=10)

    refresh_btn = ctk.CTkButton(master=button_frame, text="Refresh Products",
                                command=lambda: [populate_products_tree(), populate_product_display(),
                                                 clear_selections()])
    refresh_btn.pack(side=ctk.LEFT, padx=5)

    add_btn = ctk.CTkButton(master=button_frame, text="Add to Cart",
                            command=lambda: [add_to_cart(), clear_selections()])
    add_btn.pack(side=ctk.LEFT, padx=5)

    cart_btn = ctk.CTkButton(master=button_frame, text="View Cart",
                             command=lambda: cart.show_cart(root, cart_items, grand_total))
    cart_btn.pack(side=ctk.LEFT, padx=5)

    # Right-side Product Display Frame
    product_display_frame = ctk.CTkScrollableFrame(master=root, width=300)
    product_display_frame.pack(side=ctk.RIGHT, fill=ctk.Y, padx=10, pady=10)

    selected_item_button = None


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
        products_tree.selection_remove(products_tree.selection())
        global selected_item_button
        if selected_item_button:
            selected_item_button.configure(fg_color="gray20")
            selected_item_button = None


    def populate_products_tree(category_id=None):
        try:
            print("Executing query to fetch products for Treeview...")
            products_tree.delete(*products_tree.get_children())
            if category_id is None:
                query = "SELECT Name, Price FROM products"
                cursor.execute(query)
            else:
                query = "SELECT Name, Price FROM products WHERE CategoryID = %s"
                cursor.execute(query, (category_id,))
            rows = cursor.fetchall()
            print(f"Fetched {len(rows)} products for Treeview (CategoryID: {category_id if category_id else 'All'})")
            if not rows:
                messagebox.showinfo("Info", "No products found in the database")
            for row in rows:
                products_tree.insert("", "end", values=(row[0], row[1]))
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Query failed: {err}")
            print(f"Query error: {err}")


    def filter_products(category_id):
        try:
            print(f"Filtering products by CategoryID: {category_id if category_id else 'All'}")
            populate_products_tree(category_id)
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
            cart.update_cart_display(cart_items, grand_total)  # Update cart display
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


    def update_product_entries(event):
        selected = products_tree.selection()
        if selected:
            item = products_tree.item(selected[0])
            product = item['values'][0]
            price = item['values'][1]
            name_entry.configure(state='normal')
            name_entry.delete(0, ctk.END)
            name_entry.insert(0, product)
            name_entry.configure(state='disabled')
            price_entry.delete(0, ctk.END)
            price_entry.insert(0, price)
            qty_entry.delete(0, ctk.END)
            qty_entry.insert(0, "1")
            total_entry.configure(state='normal')
            total_entry.delete(0, ctk.END)
            total_entry.insert(0, price)
            total_entry.configure(state='disabled')


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


    products_tree.bind("<<TreeviewSelect>>", update_product_entries)
    qty_entry.bind("<KeyRelease>", update_total)
    price_entry.bind("<KeyRelease>", update_total)

    # Populate both Treeview and product display on startup
    populate_products_tree()
    populate_product_display()

    root.mainloop()

except mysql.connector.Error as err:
    messagebox.showerror("Connection Error", f"Cannot connect to database: {err}")
    print(f"Connection error: {err}")

finally:
    if 'database' in locals():
        print("Closing database connection")
        database.close()