# functions go here

# checks users enter an integer to a given question
def num_check(question):

    while True:

        try:
            response = int(input(question))
            return response

        except ValueError:
            print("Please enter an integer.")


# main routine goes here
pizzas_sold = 0

while True:

    name = input("Enter your name / xxx to quit: ")

    if name == "xxx":
        break

    phone_number = num_check("Phone number: ")

    pizzas_sold += 1

print("You have sold ")
