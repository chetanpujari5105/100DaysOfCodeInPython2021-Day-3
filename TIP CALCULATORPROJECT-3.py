#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python
print("welcome to tip calculator")
bill = float(input("enter your total bill? $"))
tip = int(input(("how much percentage you want to pay 10,12 or 15")))
people = int(input(("how many people want to split the bill")))
tip_cal = tip / 100
total_tip_amount = bill * tip_cal
toal_bill = bill + total_tip_amount
each_person_pay = toal_bill / people
final_amount = round(each_person_pay,2)
print(f"your total bill is {round(toal_bill)} and for each is $ {(each_person_pay)}") 
