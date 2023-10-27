import pandas


# currency formatting function
def currency(x):
    return "${:.2f}".format(x)


# dictionaries to hold order details
all_pizzas = ["a", "b", "c", "d", "e"]
all_pizza_costs = [11.00, 15.50, 14.00, 14.50, 13.50]
all_pizza_toppings = ["a2", "b2", "c2", "d2", "e2"]
all_pizza_toppings_costs = [1.00, 1.00, 2.00, 0.00, 0.50]

pizza_order_dict = {
    "Pizza": all_pizzas,
    "Pizza Price": all_pizza_costs,
    "Toppings": all_pizza_toppings,
    "Topping Price": all_pizza_toppings_costs
}

pizza_order_frame = pandas.DataFrame(pizza_order_dict)
pizza_order_frame = pizza_order_frame.set_index('Pizza')

# Calculate the total order cost (pizza + toppings + surcharge + delivery)
pizza_order_frame['Total'] = (pizza_order_frame['Topping Price']
                              + pizza_order_frame['Pizza Price'])

# calculate order total
total = pizza_order_frame['Total'].sum()

# currency formatting (uses currency function)
add_dollars = ['Pizza Price', 'Topping Price', 'Total']
for var_item in add_dollars:
    pizza_order_frame[var_item] = pizza_order_frame[var_item].apply(currency)

print("****** Order Data ******")
print()

# output table with order data
print(pizza_order_frame)

print()
print("****** Order Summary ******")

# output total order sales
print("Total Cost: ${:.2f}".format(total))
