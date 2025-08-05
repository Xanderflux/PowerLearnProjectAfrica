def calculate_discount(price, discount_percent):
    """Calculate the final price after applying a discount if discount is 20% or higher."""
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Prompt the user for input
original_price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate and display the final price
final_price = calculate_discount(original_price, discount_percent)
if final_price != original_price:
    print(f"The final price after applying a {discount_percent}% discount is: {final_price}")
else:
    print(f"No discount applied. The original price is: {original_price}")

