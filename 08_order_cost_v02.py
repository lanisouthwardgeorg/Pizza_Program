import pandas


# currency formatting function
def currency(x):
    return "${:.2f}".format(x)


# dictionaries to hold order details
all_names = ["a", "b", "c", "d", "e"]
all_pizza_costs = [11.00, 15.50, 14.00, 14.50, 13.50]
all_pizza_toppings = [1.00, 1.00, 2.00, 0.00, 0.50]
surcharge = [0.25, 0.00, 0.25, 0.00, 0.00]
delivery_charge = [4.00, 4.00, 4.00, 0.00, 0.00]

pizza_order_dict = {
    "Name": all_names,
    "Pizza Price": all_pizza_costs,
    "Topping Price": all_pizza_toppings,
    "Surcharge": surcharge,
    "Delivery Cost": delivery_charge
}

pizza_order_frame = pandas.DataFrame(pizza_order_dict)
pizza_order_frame = pizza_order_frame.set_index('Name')

# Calculate the total order cost (pizza + toppings + surcharge + delivery)
pizza_order_frame['Total'] = (pizza_order_frame['Delivery Cost']
                              + pizza_order_frame['Surcharge']
                              + pizza_order_frame['Topping Price']
                              + pizza_order_frame['Pizza Price'])

# calculate order total
total = pizza_order_frame['Total'].sum()

# currency formatting (uses currency function)
add_dollars = ['Pizza Price', 'Topping Price', 'Surcharge', 'Delivery Cost', 'Total']
for var_item in add_dollars:
    pizza_order_frame[var_item] = pizza_order_frame[var_item].apply(currency)

print("****** Order Data ******")
print()

# output table with order data
print(pizza_order_frame)

print()
print("****** Order Summary ******")

# output total order sales
print("Total Pizza Sales: ${:.2f}".format(total))
