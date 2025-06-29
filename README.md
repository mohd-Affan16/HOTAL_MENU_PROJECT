# Hotel Menu Billing System

This is a simple **Hotel Menu Billing System** written in Python using **Object-Oriented Programming (OOP)** concepts. It allows customers to place orders, calculates the total bill, and generates a formatted receipt.

---

##  Features

-  Displays a pre-defined food menu with prices.
-  Allows user to select items by name or ID.
-  Supports custom quantity input and validates it.
-  Generates a clean and structured bill.
-  Displays current date and time in the bill.

---

## Project Structure

- `MenuItem` class → Represents a food item.
- `Menu` class → Manages and displays menu items.
- `OrderItem` class → Inherits from `MenuItem` and adds quantity.
- `Order` class → Manages customer orders and billing logic.

---

##  How to Run

1. Make sure you have **Python 3.6+** installed.
2. Download or clone this repository.
3. Open terminal or command prompt in the project folder.
4. Run the script:
   ```bash
   python hotel_menu.py
## Example
========================================
                Menu
========================================
ID  Name                          Price
________________________________________
1   Biryani                       ₹150
2   Paneer Butter Masala          ₹180
3   Masala Dosa                   ₹80
4   Chole Bhature                 ₹100
5   Chicken Tikka Masala          ₹150
________________________________________

What do you want to eat?
> biryani
What quantity do you want to order?
> 2
✅ Item added: Biryani x2

Do you want to add another item? (yes/no): yes
========================================
                Menu
========================================
ID  Name                          Price
________________________________________
1   Biryani                       ₹150
2   Paneer Butter Masala          ₹180
3   Masala Dosa                   ₹80
4   Chole Bhature                 ₹100
5   Chicken Tikka Masala          ₹150
________________________________________

What do you want to eat?
> masala dosa
What quantity do you want to order?
> 1
✅ Item added: Masala Dosa x1

Do you want to add another item? (yes/no): no
========================================
                Menu
========================================
ID  Name                          Price
________________________________________
1   Biryani                       ₹150
2   Paneer Butter Masala          ₹180
3   Masala Dosa                   ₹80
4   Chole Bhature                 ₹100
5   Chicken Tikka Masala          ₹150
________________________________________

What do you want to eat?
> masala dosa
What quantity do you want to order?
> 1
✅ Item added: Masala Dosa x1

Do you want to add another item? (yes/no): no
