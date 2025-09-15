from pyscript import display
# Restaurant Order System using Python Data Types

# 1. String data type
restaurant_name = "Manhattan's Cafe"  # string
owner_name = "Ezekiel Atienza Lim"  # string

# 2. Integer data type
year_established = 2021  # integer

# 3. Float data type
tax_rate = 0.02  # float (2% tax)
popular_item_price = 150.00  # float (menu item price)

# 4. Boolean data type
has_delivery = True  # boolean

# 5. List data type
product_names = ["Matcha Latte", "Black Coffee", "Carrot Bread", "Matcha Macadamia",
    "Sparkling Water"]  # list

# 6. Tuple data type
business_hours = ("11:00 AM", "10:00 PM")  # tuple

# 7. Dictionary data type
menu_prices = {  # dictionary
    "Matcha Latte": 150.00,
    "Black Coffee": 125.00,
    "Carrot Bread": 100.00,
    "Matcha Macadamia": 130.00,
    "Sparkling Water": 20.00,
}

# 8. Set data type
common_allergens = {"gluten", "dairy", "eggs","nuts","carrots"}  # set

# ------------------- DISPLAY -------------------

# Display restaurant info
display(restaurant_name, target="name1")
display(f"Owner: {owner_name}", target="owner")
display(f"Since {year_established}", target="since")
display("Menu Pricelist", target="heading1")

# Display menu items
display(product_names[0], target="prod1")
display(f"₱{menu_prices['Matcha Latte']:.2f}", target="price1")

display(product_names[1], target="prod2")
display(f"₱{menu_prices['Black Coffee']:.2f}", target="price2")

display(product_names[2], target="prod3")
display(f"₱{menu_prices['Carrot Bread']:.2f}", target="price3")

display(product_names[3], target="prod4")
display(f"₱{menu_prices['Matcha Macadamia']:.2f}", target="price4")

display(product_names[4], target="prod5")
display(f"₱{menu_prices['Sparkling Water']:.2f}", target="price5")

# Display opening hours
display(f"Open: {business_hours[0]} - {business_hours[1]}", target="openingHours")

# Display delivery availability
if has_delivery:
    display("Delivery Available", target="orderType")
else:
    display("Dine-in Only", target="orderType")

# Display allergens
display(f"Common Allergens: {', '.join(common_allergens)}", target="allergens")

# Display popular item price
display(f"Popular Item Price: ₱{popular_item_price:.2f}", target="popularItem")

