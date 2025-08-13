print("Welcome to the Tip Calculator!")

bill = int(input("What was the total bill ?"))
tip = int(input("how much tip whould you like to give ? 10$ , 12$ or 15$"))
peoples = int(input("how many peoples to split the bill?"))

tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / peoples
final_amount = round(bill_per_person ,2)

print(f"Each person should pay: ${final_amount}" )