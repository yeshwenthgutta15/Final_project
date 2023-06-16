class FoodItem:
    def __init__(self, name, quantity, price, discount, stock):
        self.food_id = None
        self.name = name
        self.quantity = quantity
        self.price = price
        self.discount = discount
        self.stock = stock

class RestaurantMenu:
    def __init__(self):
        self.menu = {}
# Adding all new food ite
    def add_food_item(self, name, quantity, price, discount, stock):
        food_id = len(self.menu) + 1
        food_item = FoodItem(name, quantity, price, discount, stock)
        food_item.food_id = food_id
        self.menu[food_id] = food_item
# Edit the food items using FoodID.
    def edit_food_item(self, food_id, name, quantity, price, discount, stock):
        if food_id in self.menu:
            food_item = self.menu[food_id]
            food_item.name = name
            food_item.quantity = quantity
            food_item.price = price
            food_item.discount = discount
            food_item.stock = stock
            print(f"Food item with FoodID {food_id} has been updated.")
        else:
            print(f"Food item with FoodID {food_id} does not exist.")
# View all the list of available food items.
    def view_all_food_items(self):
        if self.menu:
            print("List of all food items:")
            for food_id, food_item in self.menu.items():
                print(f"FoodID: {food_id}, Name: {food_item.name}, Quantity: {food_item.quantity}, "
                      f"Price: {food_item.price}, Discount: {food_item.discount}, Stock: {food_item.stock}")
        else:
            print("No food items available in the menu.")
# Removeing the food item from the menu using FoodID.
    def remove_food_item(self, food_id):
        if food_id in self.menu:
            del self.menu[food_id]
            print(f"Food item with FoodID {food_id} has been removed.")
        else:
            print(f"Food item with FoodID {food_id} does not exist.")

# Registering the application. and details to be entered
class User:
    def __init__(self, full_name, phone_number, email, address, password):
        self.full_name = full_name
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.password = password

class FoodOrderingApp:
    def __init__(self):
        self.menu = RestaurantMenu()
        self.users = []
        self.orders = []

    def register_user(self):
        print("User Registration")
        full_name = input("Full Name: ")
        phone_number = input("Phone Number: ")
        email = input("Email: ")
        address = input("Address: ")
        password = input("Password: ")
        user = User(full_name, phone_number, email, address, password)
        self.users.append(user)
        print("Registration successful.")
# Log in to the application
    def login_user(self):
        print("User Login")
        email = input("Email: ")
        password = input("Password: ")
        for user in self.users:
            if user.email == email and user.password == password:
                print("Login successful.")
                return user
        print("Invalid email or password.")
        return None
# The user can only see 3 options:
    def place_new_order(self, user):
        print("List of food items:")
        self.menu.view_all_food_items()
        selected_items = input("Enter the numbers corresponding to the food items you want to order (separated by comma): ")
        selected_items = [int(item) for item in selected_items.split(',') if item.strip().isdigit()]
# Users should be able to select food by entering an array of numbers. For example, if the user wants to order Vegan Burger and Truffle Cake they should enter [2, 3]
        order_items = []
        for item in selected_items:
            if item in self.menu.menu:
                order_items.append(self.menu.menu[item])
# Once the items are selected user should see the list of all the items selected. The user will also get an option to place an order.
        if order_items:
            print("Selected food items:")
            total_cost = 0
            for food_item in order_items:
                print(f"FoodID: {food_item.food_id}, Name: {food_item.name}, Quantity: {food_item.quantity}, "
                      f"Price: {food_item.price}")
                total_cost += food_item.price
            place_order = input("Do you want to place the order? (yes/no): ")
            if place_order.lower() == "yes":
                self.orders.append((user, order_items))
                print(f"Order placed successfully. Total cost: {total_cost}")
        else:
            print("No valid food items selected for the order.")
# Order History should show a list of all the previous orders
    def order_history(self, user):
        user_orders = [order for order in self.orders if order[0] == user]
        if user_orders:
            print("Order history:")
            for order in user_orders:
                user = order[0]
                items = order[1]
                print(f"User: {user.full_name}, Address: {user.address}")
                for item in items:
                    print(f"FoodID: {item.food_id}, Name: {item.name}, Quantity: {item.quantity}, "
                          f"Price: {item.price}, Discount: {item.discount}, Stock: {item.stock}")
                print("-----")
        else:
            print("No order history found.")
# Update Profile: the user should be able to update their profile.
    def update_profile(self, user):
        print("Update Profile")
        print("Leave the field empty if you don't want to update it.")
        full_name = input(f"Full Name [{user.full_name}]: ").strip() or user.full_name
        phone_number = input(f"Phone Number [{user.phone_number}]: ").strip() or user.phone_number
        email = input(f"Email [{user.email}]: ").strip() or user.email
        address = input(f"Address [{user.address}]: ").strip() or user.address
        password = input(f"Password [{user.password}]: ").strip() or user.password
        user.full_name = full_name
        user.phone_number = phone_number
        user.email = email
        user.address = address
        user.password = password
        print("Profile updated successfully.")

    def run(self):
        while True:
            print("1. Register")
            print("2. Login")
            print("3. Exit")
            choice = input("Select an option: ")

            if choice == "1":
                self.register_user()
            elif choice == "2":
                user = self.login_user()
                if user:
                    while True:
                        print("1. Place New Order")
                        print("2. Order History")
                        print("3. Update Profile")
                        print("4. Logout")
                        choice = input("Select an option: ")

                        if choice == "1":
                            self.place_new_order(user)
                        elif choice == "2":
                            self.order_history(user)
                        elif choice == "3":
                            self.update_profile(user)
                        elif choice == "4":
                            print("Logged out.")
                            break
                        else:
                            print("Invalid choice. Please try again.")
            elif choice == "3":
                print("Exiting the application.")
                break
            else:
                print("Invalid choice. Please try again.")

app = FoodOrderingApp()
# The list item should as follows:
app.menu.add_food_item("Chicken Briyani (1 plate)", "1 plate", 180, 25.00, 10)
app.menu.add_food_item("Mutton Briyani (1 plate)", "1 plate", 180, 25.00, 5)
app.menu.add_food_item("Tandoori Chicken (4 pieces)", "4 pieces", 240, 15.00, 8)
app.menu.add_food_item("Chicken Burger (1 Piece)", "1 piece", 250, 10.00, 15)
app.menu.add_food_item("Vegan Burger (1 Piece)", "1 piece", 150, 10.00, 20)
app.menu.add_food_item("Choco Truffle Cake (500gm)", "500gm", 650, 45.00, 3)

app.run()