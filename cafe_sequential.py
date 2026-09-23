"""Here’s the version where discounts are applied sequentially (one after the other), instead of combining the
percentages first. In this version: The age discount is applied first.
Then the 5% loyalty discount is applied to the already discounted price."""

def calculate_price(base_price, age, has_loyalty_card):
    price = base_price

    # Apply age-based discount first
    if age < 18:
        price *= 0.80   # 20% off
    elif 18 <= age <= 60:
        price *= 0.90   # 10% off
    else:  # age > 60
        price *= 0.50   # 50% off

    # Apply loyalty discount on the new price
    if has_loyalty_card:
        price *= 0.95   # Extra 5% off

    return round(price, 2)


# --- Main Program ---
try:
    base_price = float(input("Enter the base price of the coffee: $"))
    age = int(input("Enter customer's age: "))
    loyalty_input = input("Does the customer have a loyalty card? (yes/no): ").strip().lower()

    has_loyalty_card = loyalty_input == "yes"

    final_price = calculate_price(base_price, age, has_loyalty_card)

    print(f"\nFinal price to pay: ${final_price}")

except ValueError:
    print("Invalid input. Please enter correct numeric values for price and age.")

"""🔎 What’s the difference?

If coffee costs $10 and the customer is over 60 with a loyalty card:

Combined method:
50% + 5% = 55% → Pay $4.50

Sequential method:
50% off → $5.00
Then 5% off → $4.75

So sequential discounts usually give a slightly higher final price than combining them.

If you'd like, I can also add item quantity or multiple drinks to make it more realistic for a café system """