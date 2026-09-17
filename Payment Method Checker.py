#Payment Method Checker
valid_payment = ["cash", "gcash", "card"]

method = input("Enter your payment method: ").lower()
if method in valid_payment:
    print("Valid payment method")
else:
    print("Invalid payment method")