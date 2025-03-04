inventory = {}

def AddItem(itemName, quantity):
    ## if item already exists
    if itemName in inventory:
        inventory[itemName] += quantity
    else:
        inventory[itemName] = quantity
    print(f"Added {quantity} {itemName}(s) to the inventory.")

def RemoveItem(itemName, quantityToRemove):
    if itemName in inventory:
        if inventory[itemName] <= quantityToRemove:
            del inventory[itemName]
            print(f"{itemName} removed completely from inventory.")
        else:
            inventory[itemName] -= quantityToRemove
            print(f"Removed {quantityToRemove} from {itemName}. Remaining: {inventory[itemName]}")
    else:
        print(f"No Such Item Exists in the Inventory.")

def ViewInventory():
    if not inventory:
        print("Inventory is empty.")
    else:
        ## enumerate returns an index and a key
        for i, item in enumerate(inventory, start=1):
            print(f"Item {i}: {item} | Quantity: {inventory[item]}")

## Input Menu
print("\n1. Add Item to Inventory.")
print("2. Remove Item from Inventory.")
print("3. View Inventory.")
print("4. Exit.")

while True:

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input! Please enter a number.")
        ## Skip the rest of the loop and ask again
        continue

    if choice == 1:
        newItem = input("Enter Item Name: ")
        try:
            quantity = int(input("Enter quantity: "))
            AddItem(newItem, quantity)
        except ValueError:
            print("Invalid quantity! Please enter a number.")

    elif choice == 2:
        itemName = input("Enter Item Name: ")
        try:
            quantity = int(input("How much quantity to remove? "))
            RemoveItem(itemName, quantity)
        except ValueError:
            print("Invalid quantity! Please enter a number.")

    elif choice == 3:
        ViewInventory()

    elif choice == 4:
        print("Exiting...")
        break

    else:
        print("Please Enter a Valid Choice!")
