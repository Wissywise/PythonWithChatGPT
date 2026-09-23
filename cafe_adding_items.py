# What’s the difference between combining discounts and applying them sequentially?
# If coffee costs $10 and the customer is over 60 with a loyalty card:


"""Combined method:
50 % + 5 % = 55 % → Pay $4.50

 Sequential method:
50 % off → $5.00
Then
5 % off → $4.75 """

# So sequential discounts usually give a slightly higher final price than combining them.

# If you 'd like, I can also add item quantity or multiple drinks to make it more realistic for a café system.

# add item quantity or multiple drinks to make it more realistic for a café system, great idea — let’s make it more
# like a real café ordering system.This version allows: Multiple drinks Different prices per drink Quantity per drink
# Sequential discounts(age first, then loyalty) A full receipt - style summary


def get_age_discount(age):
    if age < 18:
        return 0.20
    elif 18 <= age <= 60:
        return 0.10
    else:
        return 0.50


def calculate_total(order, age, has_loyalty_card):
    subtotal = sum(price * quantity for price, quantity in order)

    # Apply age discount
    age_discount = get_age_discount(age)
    discounted_total = subtotal * (1 - age_discount)

    # Apply loyalty discount sequentially
    if has_loyalty_card:
        discounted_total *= 0.95  # Extra 5% off

    return subtotal, round(discounted_total, 2)


# --- Main Program ---
try:
    print("Welcome to the Café Shop ☕")
    age = int(input("Enter customer's age: "))
    loyalty_input = input("Does the customer have a loyalty card? (yes/no): ").strip().lower()
    has_loyalty_card = loyalty_input == "yes"

    order = []

    while True:
        drink_name = input("\nEnter drink name (or type 'done' to finish): ").strip()
        if drink_name.lower() == "done":
            break

        price = float(input(f"Enter price for {drink_name}: $"))
        quantity = int(input(f"Enter quantity of {drink_name}: "))

        order.append((price, quantity))

    if not order:
        print("No items ordered.")
    else:
        subtotal, final_total = calculate_total(order, age, has_loyalty_card)

        print("\n------ RECEIPT ------")
        print(f"Subtotal: ${round(subtotal, 2)}")

        age_discount = get_age_discount(age) * 100
        print(f"Age Discount: {age_discount}%")

        if has_loyalty_card:
            print("Loyalty Discount: 5% (applied after age discount)")

        print(f"Final Total: ${final_total}")
        print("---------------------")

except ValueError:
    print("Invalid input. Please enter correct numeric values.")

"""✅ What this version improves: Supports multiple drinks Supports quantities Calculates subtotal before discounts 
Applies discounts sequentially Prints a clean receipt Uses functions for cleaner structure If you 'd like, I can also:
Add predefined menu items(Latte, Cappuccino, Espresso) Add tax calculation Add input validation loops(so it doesn’t
crash on wrong input) Store daily sales totals Just tell me how advanced you want the café system to be """