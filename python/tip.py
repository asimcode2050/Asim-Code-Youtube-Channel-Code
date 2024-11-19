
bill_amount = float(input("Enter the total bill amount: $"))
tip_percentage = float(input("Enter the tip percentage (e.g., 15 for 15%): "))
tip_amount = bill_amount * (tip_percentage / 100)
total_amount = bill_amount + tip_amount
print(f"Tip Amount: ${tip_amount:.2f}")
print(f"Total Amount (Bill + Tip): ${total_amount:.2f}")
