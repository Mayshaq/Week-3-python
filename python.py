def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        discounted_price = price - discount_amount
        return discounted_price
    else:
        return price

# Prompt user for input
try:
    original_price = float(input("Enter the original price of the item: "))
    discount_percentage = float(input("Enter the discount percentage: "))

    # Calculate the final price
    result_price = calculate_discount(original_price, discount_percentage)

    # Display the result
    if result_price < original_price:
        print(f"The final price after a {discount_percentage}% discount is: ${result_price:.2f}")
    else:
        print(f"No discount applied. The original price is: ${original_price:.2f}")
except ValueError:
    print("Please enter valid numbers for the price and discount percentage.")
