# q3_shopping_cart.py

# ---------------- PART A ----------------

# Buggy function
def add_item_bug(item, cart=[]):
    cart.append(item)
    return cart


print("Buggy Function Output:")
print(add_item_bug("apple"))
print(add_item_bug("banana"))
print(add_item_bug("milk", cart=["bread"]))
print(add_item_bug("eggs"))


# ---------------- PART B ----------------

# Correct function
def add_item(item, cart=None):

    if cart is None:
        cart = []

    cart.append(item)

    return cart


print("\nCorrect Function Output:")
print(add_item("apple"))
print(add_item("banana"))


# ---------------- PART C ----------------

# Create cart
def create_cart(owner, discount=0):

    return {
        "owner": owner,
        "items": [],
        "discount": discount
    }


# Add items to cart
def add_to_cart(cart, name, price, qty=1):

    item = {
        "name": name,
        "price": price,
        "qty": qty
    }

    cart["items"].append(item)


# Tuple immutability
def update_price(price_tuple, new_price):

    # Tuples are immutable
    # This will raise TypeError

    price_tuple[0] = new_price


# Calculate total
def calculate_total(cart):

    total = 0

    for item in cart["items"]:

        total += item["price"] * item["qty"]

    # Apply discount
    discount_amount = (cart["discount"] / 100) * total

    final_total = total - discount_amount

    return final_total


# Customer 1
cart1 = create_cart("Aarav", 10)

add_to_cart(cart1, "Laptop", 50000, 1)
add_to_cart(cart1, "Mouse", 1000, 2)

# Customer 2
cart2 = create_cart("Riya", 5)

add_to_cart(cart2, "Phone", 20000, 1)

print("\nCart 1:")
print(cart1)

print("\nCart 2:")
print(cart2)

print("\nCart 1 Total:", calculate_total(cart1))
print("Cart 2 Total:", calculate_total(cart2))


# Tuple test
price_data = (500,)

try:
    update_price(price_data, 700)

except TypeError as e:
    print("\nTuple Error:", e)


# ---------------- DISCUSSION POINTS ----------------

# Why is discount=0 safe but cart=[] dangerous?
# Because integers are immutable, but lists are mutable.

# Difference between rebinding and mutating:
# Rebinding means assigning a new object.
# Mutating means changing the existing object.

# Mutable:
# list, dict, set

# Immutable:
# tuple, str, int

# When a list is passed to a function and modified,
# changes reflect outside because lists are mutable
# and passed by reference.