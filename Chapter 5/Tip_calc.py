Total_amount=float(input("What was your total bill? "))
Tip_percent=int(input("How much tip would you like to give? 10, 12, or 15"))
Amount=Total_amount+(Total_amount*(Tip_percent/100))
People=int(input("How many people to split the bill? "))
Each_pay=Amount/People
print(f"Each person has to pay ${Each_pay}")