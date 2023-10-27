# main routine starts here

# set maximum number of orders below
MAX_ORDERS = 5

# loop to sell pizzas
orders_sold = 0
while orders_sold < MAX_ORDERS:
    name = input("Please enter your name or 'xxx' to quit: ")

    if name == 'xxx':
        break

    orders_sold += 1

# output number of pizzas sold
if orders_sold == MAX_ORDERS:
    print("You can only order a maximum of 5 pizzas")
else:
    print("You have placed {} order/s. You can place {} more order/s".format(orders_sold, MAX_ORDERS - orders_sold))
