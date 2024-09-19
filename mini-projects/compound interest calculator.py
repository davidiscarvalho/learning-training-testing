principle = 0
rate = 0
time = 0

while True:
	principle = input("entrer the principle amount: )
	if principle <0:
		print("Principle cannot be equal to zero")
	else:
		break
while True:
	rate = input("entrer the interest rate: )
	if rate <=0:
		print("interest Rate cannot be equal to zero")
	else:
		break
while True:
	time = input("entrer the time in years: )
	if time <=0:
		print("time cannot be less or equal to zero")
	else:
		break

total = principle * pow((1+ rate/100), time)
print(f"Balance after {time} year/s: €{total:.2f}")