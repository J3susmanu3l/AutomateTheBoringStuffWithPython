# Inventory:
# 12 arrow
# 42 gold coin
# 1 rope
# 6 torch
# 1 dagger
# Total number of items: 62




def display_inventory(inventory):
    print("Inventory:")
    for object, quantity in inventory.items():
        print(f"{quantity} {object}")
    print(f"Total number of items: {sum(inventory.values())}")




def add_items_to_inventory(inventory):
    print()
    print("Let's add more items into the inventory ")
    print()    
    new_item_name = input("what is the item name? or enter blank to stop ")
    if new_item_name != "":
        new_item_quantity = int(input("how many did you picked up into the inventory? "))
        while True:
            if new_item_name in inventory:
                inventory[new_item_name] += new_item_quantity
                print()
                display_inventory(inventory)
            else:
                inventory[new_item_name] = new_item_quantity
                print()
                display_inventory(inventory)
            new_item_name = input("what is the item name? or enter blank to stop ")
            if new_item_name == "":
                break
            new_item_quantity = int(input("how many did you picked up into the inventory? "))
    return inventory

    

def main():
    inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
    display_inventory(inventory)
    inventory = add_items_to_inventory(inventory)
    print()
    print("Last inventory: ")
    print(inventory)



if __name__ == "__main__":
    main()