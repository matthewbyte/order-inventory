orders = []

def add_order(customer_name, order_id, order_amount):
    for i in orders:
        print(i)

def display_orders(orders):
    for i in orders:
        if i['AMOUNT'] >= 200:
            print(i)
        else:
            print("Amount is less than 200!!, system only prints orders higher than 200")

def update_order_amount(order_id, new_amount):
    for i in orders:
        if order_id == i['ID']:
            i["AMOUNT"] = new_amount
            print("amount updated")

def search_order(customer_name):
    for i in orders:
        if customer_name == i["NAME"]:
            print("displaying details")
            print(i)

def adjust_order():
    while True:
        print("")
        order_id = int(input("Enter id: "))
        for i in orders:
            if order_id == i["ID"]:
                print("")
                adjust_amount = int(input("Enter amount to adjust by: "))
                amount = adjust_amount + i['AMOUNT']
                amount1 = i['AMOUNT'] - adjust_amount
                if adjust_amount <= 0:
                    print("can't adjust amount because it's less than 0")
                    break

                ask1 = input("Increase amount(+) or reduce(-) by " + str(adjust_amount) + "(+/-): ")
                if ask1 == "+":
                    i['AMOUNT'] = amount
                elif ask1 == "-":
                    i['AMOUNT'] = amount1
                print("")
                print("PRINTING ADJUSTED ORDERS...")
                print(i)

                print("")
                ask = input("Adjust another order(yes/no): ").upper()
                if ask == "NO" or ask == "N":
                    return

def high_value_alert(threshold=1000):
    for i in orders:
        if i['AMOUNT'] > threshold:
            print("Alert!! High value order detected")
            print("Printing high value order......")
            print(i)

def total_revenue(orders):
    revenue = sum(i['AMOUNT'] for i in orders)
    print("Total revenue =", revenue)

# Add order loop

while True:
    print("ORDER INVENTORY")
    print("")
    print("1. Add order")
    print("2. Update an existing order")
    print("3. Display all orders")
    print("4. Search for an order by customer name")
    print("5. Adjust the total amount of an order")
    print("6. Alert high-value orders")
    print("7. Calculate total revenue")
    print("8. Exit the program")

    choice = input("Enter option: ")
    if choice == "8":
        print("Exiting program....")
        break

    elif choice == "1":
        while True:
            print("")
            customer_name = input("Enter name: ")
            order_id = int(input("Enter id number: "))
            order_amount = float(input("Enter amount: "))

            details = {"NAME": customer_name, "ID": order_id, "AMOUNT": order_amount}

            orders.append(details)

            add_order(customer_name, order_id, order_amount)

            print("")
            ask = input("Add order (y/n): ")
            if ask == "no" or ask == "n":
                break

    elif choice == "2":
        while True:
            print("")
            print("Update order")
            order_id = int(input("Enter id: "))
            new_amount = float(input("Enter new amount: "))
            update_order_amount(order_id, new_amount)

            ask = input("Update another order (y/n): ")
            if ask == "no" or ask == "n":
                break

    elif choice == "3":
        print("")
        display_orders(orders)
        while True:
            print("")
            ask = input("Return to menu (return/r): ")
            if ask == "return" or ask == "r":
                break

    elif choice == "4":
        while True:
            print("")
            print("Search order")
            customer_name = input("Enter name: ")
            search_order(customer_name)

            print("")
            ask = input("Search for another order(y/n): ")
            if ask == "no" or ask == "n":
                break

    elif choice == "5":
        print("")
        adjust_order()

    elif choice == "6":
        print("")
        high_value_alert(threshold=1000)
        print("")
        while True:
            ask = input("Return to menu (return/r): ")
            if ask == "return" or ask == "r":
                break

    elif choice == "7":
        print("")
        total_revenue(orders)
        print("")
        while True:
            ask = input("Return to menu (return/r): ")
            if ask == "return" or ask == "r":
                break