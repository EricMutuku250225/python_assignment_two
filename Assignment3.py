def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount = (discount_percent / 100) * price
        final_price = price - discount
        return final_price
    else:
        return price

try:
    original_price = float(input("Enter the original price of the item: "))
    discount_percentage = float(input("Enter the discount percentage: "))

    final_price = calculate_discount(original_price, discount_percentage)

    if discount_percentage >= 20:
        print(f"The final price after applying the discount is: {final_price:.2f}")
    else:
        print(f"No discount applied. The original price remains: {original_price:.2f}")
except ValueError:
    print("Please enter valid numbers for the price and discount percentage.")
