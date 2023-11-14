print("Welcome to Tip Calculator")
people = int(input("Enter the number of people :\n"))
bill = float(input("Enter the bill amount :\n"))
tip = int(input("Tip to add in bill :\n"))
bill_with_tip = tip/100 * bill + bill
sum = bill_with_tip/people
print(f"Each Person should Pay :{sum}")