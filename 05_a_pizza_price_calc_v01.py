# calculate the pizza price based on pizza name
def calc_pizza_price(var_pizza):

    # Cheese pizza is $11.00
    if var_pizza == "cheese":
        price = 11.00

    # Cheesy garlic pizza is $11.50
    elif var_pizza == "cheesy":
        price = 11.50

    # Ham & cheese pizza is $12.50
    elif var_pizza == "ham":
        price = 12.50

    # Hawaiian pizza is $13.50
    elif var_pizza == "hawaiian":
        price = 13.50

    # Hot & spicy veggie pizza is $15.50
    elif var_pizza == "hot":
        price = 15.50

    # Margherita pizza is $11.50
    elif var_pizza == "margherita":
        price = 11.50

    # Meatlovers pizza is $11.50
    elif var_pizza == "meatlovers":
        price = 15.00

    # Pepperoni pizza is $12.00
    elif var_pizza == "pepperoni":
        price = 12.00

    # Spinach pizza is $14.00
    elif var_pizza == "spinach":
        price = 14.00

    # Veggie pizza is $14.50
    else:
        price = 14.50

    return price


# loop for testing
while True:

    # get pizza
    pizza = input("Choose pizza ")

    # calculate pizza cost
    pizza_cost = calc_pizza_price(pizza)
    print("Pizza: {}, Pizza Price: ${:.2f}".format(pizza, pizza_cost))
