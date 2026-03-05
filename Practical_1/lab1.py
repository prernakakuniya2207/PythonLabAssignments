# Lab Assignment 1
# Ohm's Law and Nature of Current

voltage = float(input("Enter Voltage (V): "))
resistance = float(input("Enter Resistance (R): "))

current = voltage / resistance

print("\nCurrent (I) =", current, "Ampere")

if current < 0.5:
    print("Nature of Current: Low current")
elif current <= 2:
    print("Nature of Current: Normal current")
else:
    print("Nature of Current: High current")