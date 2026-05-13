import re

password = input("Enter password: ")

strength = 0

# Length check
if len(password) >= 8:
    strength += 1
else:
    print("Password should be at least 8 characters")

# Uppercase check
if re.search(r"[A-Z]", password):
    strength += 1
else:
    print("Add uppercase letters")

# Lowercase check
if re.search(r"[a-z]", password):
    strength += 1
else:
    print("Add lowercase letters")

# Number check
if re.search(r"\d", password):
    strength += 1
else:
    print("Add numbers")

# Special character check
if re.search(r"[!@#$%^&*]", password):
    strength += 1
else:
    print("Add special characters")

# Final result
if strength == 5:
    print("Strong Password")
elif strength >= 3:
    print("Medium Password")
else:
    print("Weak Password")