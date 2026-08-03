# ------------------------------
# Safa's Restaurant - Order System
# ------------------------------

# Menu dictionary: item name -> price
menu = {
    'Pasta': 50,
    'Burger': 100,
    'Salad': 20,
    'Biryani': 150,
    'Pizza': 200
}

# Greet Customer
print("Welcome to Safa's Restaurant")
print("\nPasta  : Rs50")
print("Burger : Rs100")
print("Salad  : Rs20")
print("Biryani: Rs150")
print("Pizza  : Rs200")

total_order = 0        # Total bill amount
ordered_items = []      # Keep track of items customer ordered

# ------------------------------
# Loop to keep taking orders until customer says "No"
# (This replaces the old fixed "item_1, item_2" approach,
#  so customer can order as many items as they want)
# ------------------------------
while True:
    item = input("\nEnter name of the item you want to order: ").strip().title()

    if item in menu:
        total_order += menu[item]
        ordered_items.append(item)
        print(f"Your item '{item}' has been added.")
    else:
        # Bug fix: pehle "not found" wala message tha jo galat variable
        # print kar raha tha (item_2), ab sahi item show hota hai
        print(f"Sorry, '{item}' is not available on the menu.")

    another_item = input("Do you want to add another item? (Yes/No): ").strip().lower()

    # Bug fix: agar user "Yes" ke ilawa kuch bhi likhe (No, no, N, etc.)
    # to loop yahin ruk jaye ga, aur "item_2 not defined" wala error
    # ab kabhi nahi aayega, kyunki hum ek hi variable "item" reuse kar rahe hain
    if another_item != "yes":
        break

# ------------------------------
# Final Bill Summary
# ------------------------------
print("\n----- Order Summary -----")
if ordered_items:
    for i in ordered_items:
        print(f"- {i}: Rs{menu[i]}")
else:
    print("No items were ordered.")

print(f"\nTotal amount of order to pay is: Rs{total_order}")
print("Thank you for ordering from Safa's Restaurant!")