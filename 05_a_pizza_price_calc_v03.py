# calculate the pizza price based on pizza number
pizza_selection = []
pizza_price_calc = []


def calc_pizza_price(var_pizza_type):

    # Cheese pizza is $11.00
    if var_pizza_type == 1:
        price = 11.00
        pizza_selection.append("Cheese Pizza")
        pizza_price_calc.append(price)

    # Cheesy garlic pizza is $11.50
    elif var_pizza_type == 2:
        price = 11.50
        pizza_selection.append("Cheesy Garlic Pizza")
        pizza_price_calc.append(price)

    # Ham & cheese pizza is $12.50
    elif var_pizza_type == 3:
        price = 12.50
        pizza_selection.append("Ham & Cheese Pizza")
        pizza_price_calc.append(price)

    # Hawaiian pizza is $13.50
    elif var_pizza_type == 4:
        price = 13.50
        pizza_selection.append("Hawaiian Pizza")
        pizza_price_calc.append(price)

    # Hot & spicy veggie pizza is $15.50
    elif var_pizza_type == 5:
        price = 15.50
        pizza_selection.append("Hot & Spicy Veggie Pizza")
        pizza_price_calc.append(price)

    # Margherita pizza is $11.50
    elif var_pizza_type == 6:
        price = 11.50
        pizza_selection.append("Margherita Pizza")
        pizza_price_calc.append(price)

    # Meatlovers pizza is $15.00
    elif var_pizza_type == 7:
        price = 15.00
        pizza_selection.append("Meatlovers Pizza")
        pizza_price_calc.append(price)

    # Pepperoni pizza is $12.00
    elif var_pizza_type == 8:
        price = 12.00
        pizza_selection.append("Pepperoni Pizza")
        pizza_price_calc.append(price)

    # Spinach pizza is $14.00
    elif var_pizza_type == 9:
        price = 14.00
        pizza_selection.append("Spinach Pizza")
        pizza_price_calc.append(price)

    # Veggie pizza is $14.50
    else:
        price = 14.50
        pizza_selection.append("Veggie Pizza")
        pizza_price_calc.append(price)

    return price


# loop for testing
while True:

    # get pizza using integers
    pizza_type = int(input("Pizza: "))

    # calculate pizza cost
    pizza_cost_calc = calc_pizza_price(pizza_type)
    print("Pizza: {}, Pizza Price: ${}".format(pizza_selection, pizza_price_calc))
