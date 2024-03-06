# Defining the function calculate_function
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        final_price = price - (price * discount_percent / 100)
        return final_price
    else:
        return price

# Prompting the user to enter the original price and discount percentage
original_price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculating the final price using the calculate_discount function
final_price = calculate_discount(original_price, discount_percent)

# Printing the final price after applying the discount, or the original price if no discount was applied
if final_price == original_price:
    print("No discount applied. Original price:", original_price)
else:
    print("Final price after applying the discount:", final_price)