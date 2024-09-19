weight = float(input("weight: "))
unit = upper(left(input("kilograms (K) or pounds (P)? "),1))

if unit == "K":
	weight = weight * 2.205
	unit = "Kgs"
elif unit == "P":
	weight = weight / 2.205
	unit = "Lbs"
else:
	print(f"{unit} is not a valid unit.")
	break
print(f"The new weight is {round(weight,1)} {unit}.")
