# Arrays to store item details
item_codes = ['A1', 'A2', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3', 'D1', 'D2', 'E1', 'E2', 'E3', 'F1', 'F2', 'G1', 'G2']
descriptions = ['Compact', 'Tower', '8 GB', '16 GB', '32 GB', '1 TB HDD', '2 TB HDD', '4 TB HDD', '240 GB SSD', '480 GB SSD', '1 TB HDD', '2 TB HDD', '4 TB HDD', 'DVD/Blu-Ray Player', 'DVD/Blu-Ray Re-writer', 'Standard Version', 'Professional Version']
prices = [75.00, 150.00, 79.99, 149.99, 299.99, 49.99, 89.99, 129.99, 59.99, 119.99, 49.99, 89.99, 129.99, 50.00, 100.00, 100.00, 175.00]

# Basic set of components
basic_components_cost = 200

# Function to display items and get user choice
def display_and_select_items(category, codes, descriptions, prices):
    print(f"\n{category} Options:")
    for i in range(len(codes)):
        print(f"{i + 1}. {descriptions[i]} - ${prices[i]}")
    
    while True:
        try:
            choice = int(input(f"Choose the {category} item number (1-{len(codes)}): "))
            if 1 <= choice <= len(codes):
                return codes[choice - 1], descriptions[choice - 1], prices[choice - 1]
            else:
                print("Please enter a valid option.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Task 1 - Ordering main items
print("Welcome to the Online Computer Shop!")
print("Please select one case, one RAM, and one Main Hard Disk Drive.")

selected_case_code, selected_case_desc, selected_case_price = display_and_select_items("Case", item_codes[:2], descriptions[:2], prices[:2])
selected_ram_code, selected_ram_desc, selected_ram_price = display_and_select_items("RAM", item_codes[2:5], descriptions[2:5], prices[2:5])
selected_hdd_code, selected_hdd_desc, selected_hdd_price = display_and_select_items("Main Hard Disk Drive", item_codes[5:8], descriptions[5:8], prices[5:8])

total_price = basic_components_cost + selected_case_price + selected_ram_price + selected_hdd_price

print("\nChosen Items:")
print(f"Case: {selected_case_desc} - ${selected_case_price}")
print(f"RAM: {selected_ram_desc} - ${selected_ram_price}")
print(f"Main Hard Disk Drive: {selected_hdd_desc} - ${selected_hdd_price}")
print(f"\nTotal Price: ${total_price:.2f}")

# Task 2 - Ordering additional items
additional_items = []
while True:
    choice = input("\nWould you like to purchase additional items? (yes/no): ").lower()
    if choice == 'yes':
        selected_item_code, selected_item_desc, selected_item_price = display_and_select_items("Additional Item", item_codes[8:], descriptions[8:], prices[8:])
        total_price += selected_item_price
        additional_items.append((selected_item_code, selected_item_desc, selected_item_price))
    elif choice == 'no':
        break
    else:
        print("Please enter 'yes' or 'no'.")

# Task 3 - Offering discounts
if len(additional_items) == 1:
    discount = total_price * 0.05
    total_price -= discount
    print(f"\nYou've saved ${discount:.2f} with a 5% discount!")
elif len(additional_items) >= 2:
    discount = total_price * 0.10
    total_price -= discount
    print(f"\nYou've saved ${discount:.2f} with a 10% discount!")

print(f"\nNew Total Price after Discount: ${total_price:.2f}")
