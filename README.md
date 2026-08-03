Outline Restaurant – Order Management System

A simple Python console application that simulates a food ordering system for Safa's Restaurant. The program displays a menu with five items (Pasta, Burger, Salad, Biryani, Pizza) along with their prices, then allows the customer to place an order interactively.

Key Features:

Displays a clean, formatted menu with item names and prices
Lets the customer order multiple items in a loop, rather than being limited to a fixed number
Validates each entered item against the menu and lets the customer know if it's unavailable
Automatically calculates and tracks the running total as items are added
Asks after each item whether the customer wants to continue ordering
Prints a final order summary listing every item ordered with its price
Displays the total bill amount at the end

How it works:

The program greets the customer and shows the menu.
The customer types the name of an item to order.
If the item exists in the menu, it's added to the order and the price is added to the total.
The customer is asked if they'd like to add another item — this repeats until they respond with anything other than "Yes".
A summary of all ordered items and the total amount payable is displayed at the end.
