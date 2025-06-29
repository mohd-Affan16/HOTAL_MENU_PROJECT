from datetime import datetime
class Menuitem:
    def __init__(self,id,name,price):
        self.id=id
        self.name=name
        self.price=price
class Menu:
    def __init__(self):
        self.item=[
            Menuitem('1',"Biryani",150),
            Menuitem('2',"Paneer butter masala",180),
            Menuitem('3',"masala dosa",80),
            Menuitem('4',"chole bhature",100),
            Menuitem('5',"Chicken Tikka Masala",150)
        ]
    def display(self):
        print('=' * 40)
        print('Menu'.rjust(20))  
        print('=' * 40)
        print('Name'.ljust(30)+'price')
        print('_' * 40)
        for item in self.item:
            print(f"{item.id.ljust(3)}{item.name.ljust(31)}₹{item.price}")
        print('_' * 40)

class Orderitem(Menuitem):
    def __init__(self,id,quantity,name,price):
        super().__init__(id,name,price)
        self.quantity=quantity

class Order:
    def __init__(self):
      self.order_list=[]
    def add_item(self,menu_item):
        choice=input('what do you what to eat??\n').strip().lower()
        found=False
        for item in menu_item:
            if choice== item.name.lower() or choice == item.id:
                quantity=(input('what quantity do you want to order\n'))
                if quantity.isdigit() and int(quantity)>0:
                     quantity=int(quantity)
                     self.order_list.append(Orderitem(item.id,quantity,item.name,item.price))
                     print('item added')
                else:
                    print('invalid quantity')
                found=True
                break
        if not found:
            print('item not found')
    def generate_bill(self):
        current_time=datetime.now()
        print('='*50)
        print('The Azure Haven Hotel'.rjust(35))
        print(current_time.strftime("Date: %d-%m-%Y at %I:%M %p"))
        print('='*50)
        print('Name\t\t\tQty\tPrice \tAmount')
        print('-'*50)
        total=0
        for item in self.order_list:
            amount=item.quantity*item.price
            total+=amount
            print(f"{item.name.ljust(25)}{str(item.quantity).ljust(9)}₹{str(item.price).ljust(9)}₹{str(amount)}")
        print('-'*50)
        print(f"{'Total Amount'.ljust(42)}  ₹{total}")
        print('-'*50)
menu = Menu()
order = Order()

while True:
    menu.display()
    order.add_item(menu.item)

    choice = input("Do you want to add another item? (yes/no): ").lower()
    if choice != 'yes':
        order.generate_bill()
        break


        