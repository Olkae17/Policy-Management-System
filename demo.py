from policyholder import Policyholder
from product import Product
from payment import Payment

# Create products
health = Product("Health Insurance", 300)
life = Product("Life Insurance", 500)

# Create policyholders
Kayode = Policyholder("Kayode Oladele", "olkae@example.com")
Victory = Policyholder("Victory Eni", "eni@example.com")

# Create payments
pay1 = Payment(300)
pay2 = Payment(500)

# Assign products and payments
Kayode.add_product(health)
Kayode.add_payment(pay1)

Victory.add_product(life)
Victory.add_payment(pay2)

# Display info
Kayode.display_info()
print("\n")
Victory.display_info()