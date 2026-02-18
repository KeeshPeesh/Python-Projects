import math

print("Temperature Converter")
print("Units: C = Celsius, F = Fahrenheit, K = Kelvin")

running = True

while running:
    try:
        temp = float(input("Enter temperature value: "))
    except ValueError:
        print("Invalid number. Please enter a numeric value.")
        
    from_unit = input("Enter input unit (C/F/K): ").upper()
    to_unit = input("Enter output unit (C/F/K): ").upper()
    
    #Valudate Units
    if from_unit not in ["C", "F", "K"] or to_unit not in ["C", "F", "K"]:
        print("Invalid unit. Please use C, F, or K.")
        continue
    
    #Kelvin cannot be negative
    if from_unit == "K" and temp < 0:
        print("Invalid: Kelvin cannot be negative.")
        continue
    
    #Convert input to Celsius
    if from_unit == "C":
        celcius = temp
    elif from_unit == "F":
        celcius = (temp - 32) * 5/9
    elif from_unit == "K":
            celcius = temp - 273.15
    
    #Convert celcius to target Unit
    if to_unit == "C":
        result = celcius
    elif to_unit == "F":
        result = (celcius * 9/5) + 32
    elif to_unit == "K":
        result = celcius + 273.15
        
    print(f"Result: {result:.2f} {to_unit}")
    
    choice = input("Convert Again? (Yes/No): ").lower()
    if choice == "no":
        running = False
