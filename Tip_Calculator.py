print("Welcome to Tip Calculator")
people = int(input("Enter the number of people :\n"))
bill = float(input("Enter the bill amount :\n"))
tip = int(input("Tip to add in bill :\n"))
sum =(bill/people)*tip
print(f"Each Person should Pay :{sum}")