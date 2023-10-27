# calculate the topping price based on topping number
topping_selection = []
topping_price_calc = []


def calc_topping_price(var_topping_type):

    # Cheese topping is $2.00
    if var_topping_type == 1:
        price = 2.00
        topping_selection.append("Cheese")
        topping_price_calc.append(price)

    # Chilli topping is $0.50
    elif var_topping_type == 2:
        price = 0.50
        topping_selection.append("Chilli")
        topping_price_calc.append(price)

    # Ham topping is $2.00
    elif var_topping_type == 3:
        price = 2.00
        topping_selection.append("Ham")
        topping_price_calc.append(price)

    # Mushroom topping is $1.00
    elif var_topping_type == 4:
        price = 1.00
        topping_selection.append("Mushroom")
        topping_price_calc.append(price)

    # Olives topping is $1.00
    elif var_topping_type == 5:
        price = 1.00
        topping_selection.append("Olives")
        topping_price_calc.append(price)

    # Onions topping is $1.00
    elif var_topping_type == 6:
        price = 1.00
        topping_selection.append("Onions")
        topping_price_calc.append(price)

    # Pineapple topping is $1.00
    elif var_topping_type == 7:
        price = 1.00
        topping_selection.append("Pineapple")
        topping_price_calc.append(price)

    # Tomatoes topping is $1.00
    else:
        price = 1.00
        topping_selection.append("Tomatoes")
        topping_price_calc.append(price)

    return price


# loop for testing
while True:

    # get topping using integers
    topping_type = int(input("Topping: "))

    # calculate topping cost
    topping_cost_calc = calc_topping_price(topping_type)
    print("Pizza: {}, Topping Price: ${}".format(topping_selection, topping_price_calc))
