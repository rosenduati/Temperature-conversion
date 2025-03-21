# Temperature conversion program
temp = float(input("Enter the temperature: "))
units = input("Is this temperature in Celsius or Fahrenheit (F/C)?")

if units == "F":
    temp = round((temp - 32) * 5/9, 1)
    print(f"The temperature in Celsius is: {temp} c")

elif units == "C":
    temp = round((9 * temp) / 5 +32, 1)
    print(f"The temperature in Fahrenheit is: {temp} F")

else:
    print(f"{units} is invalid")
