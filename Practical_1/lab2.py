# Vendor Details Program

name = input("Enter Vendor Name: ")
year = input("Enter Year of Association: ")
contact = input("Enter Contact Number: ")
email = input("Enter Email ID: ")

monthly_purchase = float(input("Enter Monthly Purchase Amount: "))

annual_purchase = monthly_purchase * 12

print("\n------ Vendor Details ------")
print("Vendor Name:", name)
print("Year of Association:", year)
print("Contact Number:", contact)
print("Email ID:", email)

print("\nMonthly Purchase:", monthly_purchase)
print("Annual Purchase:", annual_purchase)