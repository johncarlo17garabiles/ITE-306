#Rate Per Day
RatePerDay = 15000

#Sound System Fee
SoundSystemFee = 4500

#Stage Decor Fee
StageDecorFee = 3000

#Catering Fee
CateringFee = 35000

#Expanded Value Added Tax
EVAT = .12

#ask the user to enter/input the number of day/s
NumOfDays = int(input("Enter The Number Of Day/s: "))

#Gets the value for Amount by multiplying RatePerDay and NumOfDays
Amount = RatePerDay * NumOfDays

#Gets the value for TotalAmount by adding Amount, SoundSystemFee, StageDecorFee, and CateringFee
TotalAmount = Amount + SoundSystemFee + StageDecorFee + CateringFee

#Gets the Tax by multiplying The TotalAmount, and EVAT
Tax = TotalAmount * EVAT

#Adding TotalAmount and Tax is equal to Bill
Bill = TotalAmount + Tax

#print the bill
print(Bill)


