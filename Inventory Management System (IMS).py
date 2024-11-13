class User:
    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role  # Admin or User

class Authentication:
    def __init__(self):
        # Predefined users with role-based access
        self.users = {
            "admin": User("admin", "admin123", "Admin"),
            "user": User("user", "user123", "User")
        }
        
    def login(self, username, password):
        if username in self.users and self.users[username].password == password:
            return self.users[username]
        else:
            print("Invalid username or password.")
            return None

# Product Management
class Product:
    def __init__(self, product_id, name, category, price, stock_quantity):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.stock_quantity = stock_quantity

class Inventory:
    def __init__(self):
        self.products = {}

    def add_product(self, product):
        if product.product_id in self.products:
            print("Product with this ID already exists.")
        else:
            self.products[product.product_id] = product
            print(f"Product '{product.name}' added successfully.")

    def edit_product(self, product_id, **kwargs):
        product = self.products.get(product_id)
        if product:
            product.name = kwargs.get("name", product.name)
            product.category = kwargs.get("category", product.category)
            product.price = kwargs.get("price", product.price)
            product.stock_quantity = kwargs.get("stock_quantity", product.stock_quantity)
            print(f"Product '{product_id}' updated successfully.")
        else:
            print("Product not found.")

    def delete_product(self, product_id):
        if product_id in self.products:
            del self.products[product_id]
            print(f"Product '{product_id}' deleted successfully.")
        else:
            print("Product not found.")

    def view_products(self):
        if not self.products:
            print("No products in inventory.")
            return
        print("Inventory:")
        for product in self.products.values():
            print(f"ID: {product.product_id}, Name: {product.name}, Category: {product.category}, Price: ${product.price}, Stock: {product.stock_quantity}")
            
    def search_product(self, name=None, category=None):
        for product in self.products.values():
            if (name and product.name == name) or (category and product.category == category):
                print(f"Found - ID: {product.product_id}, Name: {product.name}, Category: {product.category}, Price: ${product.price}, Stock: {product.stock_quantity}")
                return
        print("Product not found.")

    def adjust_stock(self, product_id, quantity):
        product = self.products.get(product_id)
        if product:
            product.stock_quantity += quantity
            print(f"Adjusted stock for '{product_id}'. New quantity: {product.stock_quantity}")
            if product.stock_quantity < 10:
                print("Warning: Low stock level!")
        else:
            print("Product not found.")

# Main Application
class InventoryManagementSystem:
    def __init__(self):
        self.auth = Authentication()
        self.inventory = Inventory()
        self.current_user = None

    def login(self):
        username = input("Username: ")
        password = input("Password: ")
        self.current_user = self.auth.login(username, password)
        
    def run(self):
        while True:
            if not self.current_user:
                self.login()
                if not self.current_user:
                    continue

            print(f"\nWelcome, {self.current_user.username} ({self.current_user.role})")
            print("1. View Inventory")
            print("2. Add Product" if self.current_user.role == "Admin" else "")
            print("3. Edit Product" if self.current_user.role == "Admin" else "")
            print("4. Delete Product" if self.current_user.role == "Admin" else "")
            print("5. Adjust Stock" if self.current_user.role == "Admin" else "")
            print("6. Search Product")
            print("0. Logout")

            choice = input("Enter your choice: ")
            
            if choice == "1":
                self.inventory.view_products()
            elif choice == "2" and self.current_user.role == "Admin":
                product = Product(
                    product_id=input("Product ID: "),
                    name=input("Product Name: "),
                    category=input("Category: "),
                    price=float(input("Price: ")),
                    stock_quantity=int(input("Stock Quantity: "))
                )
                self.inventory.add_product(product)
            elif choice == "3" and self.current_user.role == "Admin":
                product_id = input("Product ID to edit: ")
                name = input("New name (leave blank to keep current): ")
                category = input("New category (leave blank to keep current): ")
                price = input("New price (leave blank to keep current): ")
                stock_quantity = input("New stock quantity (leave blank to keep current): ")
                self.inventory.edit_product(
                    product_id,
                    name=name or None,
                    category=category or None,
                    price=float(price) if price else None,
                    stock_quantity=int(stock_quantity) if stock_quantity else None
                )
            elif choice == "4" and self.current_user.role == "Admin":
                product_id = input("Product ID to delete: ")
                self.inventory.delete_product(product_id)
            elif choice == "5" and self.current_user.role == "Admin":
                product_id = input("Product ID to adjust stock: ")
                quantity = int(input("Quantity to adjust (negative to reduce): "))
                self.inventory.adjust_stock(product_id, quantity)
            elif choice == "6":
                name = input("Search by name: ")
                category = input("Search by category: ")
                self.inventory.search_product(name=name or None, category=category or None)
            elif choice == "0":
                self.current_user = None
                print("Logged out successfully.")
            else:
                print("Invalid choice or insufficient permissions.")

if __name__ == "__main__":
    app = InventoryManagementSystem()
    app.run()

