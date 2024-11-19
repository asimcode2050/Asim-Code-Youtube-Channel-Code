class GroceryItem:
    def __init__(self, name, quantity, category):
        self.name = name
        self.quantity = quantity
        self.category = category
        self.purchased = False  # Tracks if item is bought

    def mark_as_purchased(self):
        self.purchased = True

    def __str__(self):
        return f"{self.quantity} x {self.name} ({self.category}) - {'Purchased' if self.purchased else 'Not Purchased'}"


class GroceryList:
    def __init__(self):
        self.items = []  # List to hold all grocery items

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item_name):
        self.items = [item for item in self.items if item.name != item_name]

    def display_list(self):
        if not self.items:
            print("Your grocery list is empty.")
        for item in self.items:
            print(item)

    def mark_item_purchased(self, item_name):
        for item in self.items:
            if item.name == item_name:
                item.mark_as_purchased()

    def get_items_by_category(self, category):
        return [item for item in self.items if item.category == category]


grocery_list = GroceryList()
milk = GroceryItem("Milk", 2, "Dairy")
bread = GroceryItem("Bread", 1, "Bakery")
apples = GroceryItem("Apples", 6, "Fruits")
grocery_list.add_item(milk)
grocery_list.add_item(bread)
grocery_list.add_item(apples)
print("Initial grocery list:")
grocery_list.display_list()
grocery_list.mark_item_purchased("Milk")
print("\nUpdated grocery list:")
grocery_list.display_list()
print("\nItems in Dairy category:")
dairy_items = grocery_list.get_items_by_category("Dairy")
for item in dairy_items:
    print(item)
