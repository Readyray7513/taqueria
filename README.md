# Restaurant Order System

## Overview
This program simulates a simple restaurant ordering system. It presents a menu of items with prices and allows the user to place an order by typing the name of the dish. The program calculates and displays the total cost of the order after each selection.

## Features
- A predefined menu with items and their corresponding prices is provided.
- The user can input their order, and the program adds the price of the selected dish to the total.
- After each order, the updated total is displayed.
- The system continues to take orders until an end-of-file (EOF) signal is given.

## Example Usage
```
$ python order_system.py
Hello, what would you like to order today? taco
Total: $3.00
Hello, what would you like to order today? burrito
Total: $10.50
Hello, what would you like to order today? nachos
Total: $21.50
```

## How to Run
1. Run the program by executing:
   ```
   python order_system.py
   ```
2. Enter the name of the dish you would like to order.
3. The program will keep track of the total and display it after each order.
4. To end the program, you can signal EOF (Ctrl+D or Ctrl+Z, depending on your system).

## Notes
- The menu items are case-insensitive and the input is automatically converted to lowercase to match the menu keys.
- The program exits gracefully when an EOF signal is given.
