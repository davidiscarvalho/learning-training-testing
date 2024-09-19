temp = float(input("temperature: "))
unit = upper(left(input("celcius (c) or Fahrenheit (F)? "),1))


if unit == "C":
	temp = (temp * 9/5) +32
	unit = "˚ F"
elif unit == "F":
	temp = (temp -32) * 5/9
	unit = "˚ C"
else:
	print(f"{unit} is not a valid unit.")
	break
print(f"The new temperature is {round(weight,1)} {unit}.")