# Vendor Purchase Report

name = input("Enter Vendor Name: ")
year = input("Enter Year of Association: ")
contact = input("Enter Contact Number: ")
email = input("Enter Email ID: ")

monthly = float(input("Enter Monthly Purchase Amount: "))
annual = monthly * 12

print("\n--- Vendor Annual Purchase Report ---")
print("Vendor Name:", name)
print("Year of Association:", year)
print("Contact:", contact)
print("Email:", email)
print("Monthly Purchase:", monthly)
print("Annual Purchase:", annual)