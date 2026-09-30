# bill_splitter.py
print("Welcome To The Bill Split Calculator")

# Get user input
total_bill = float(input("What is the total bill?: "))
percentage_tip = int(input("What % tip would you like to give?: "))
number_of_people = int(input("How many people are splitting the bill?: "))

# Calculate tip and total
tip_amount = total_bill * (percentage_tip / 100)
total_with_tip = total_bill + tip_amount

# Calculate amount per person
payment_per_person = round(total_with_tip / number_of_people, 2)

# Output results
print(f"\nTip amount: ${tip_amount:.2f}")
print(f"Total bill including tip: ${total_with_tip:.2f}")
print(f"Each person owes: ${payment_per_person:.2f}")