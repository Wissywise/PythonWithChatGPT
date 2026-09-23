"""Write a Python program in Python for a café shop to calculate coffee prices based on these rules.
Customers under 18 get a 20% discount, those between 18 and 60 enjoys a 10% discount,
and those over 60 receive a generous 50% discount.
Furthermore, if a customer has a loyalty card, they will get an extra 5% discount on top of that."""

# Constant coffee price
COFFEE_PRICE = 30

def calculate_coffee_price(age, has_loyalty_card):
    # Determine age-based discount
    if age < 18:
        discount = 0.20
    elif 18 <= age <= 60:
        discount = 0.10
    else:  # age > 60
        discount = 0.50

    # Apply age discount
    final_price = COFFEE_PRICE * (1 - discount)

    # Apply loyalty discount if applicable
    if has_loyalty_card:
        final_price *= 0.95  # Extra 5% off

    return round(final_price, 2)


# Input section
try:
    age = int(input("Enter customer age: "))
    has_loyalty_card = input("Does the customer have a loyalty card? (yes/no): ").strip().lower() == 'yes'

    price = calculate_coffee_price(age, has_loyalty_card)
    print(f"Final coffee price: {price:.2f}")

except ValueError:
    print("Invalid input. Please enter a valid age.")
