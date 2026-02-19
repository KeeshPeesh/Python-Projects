import math

print("Temperature Converter")
print("Units: C = Celsius, F = Fahrenheit, K = Kelvin")

running = True

while running:
    def convert_temperature(value, from_unit, to_unit):
        if from_unit == to_unit:
            return value
        elif from_unit == "C":
            if to_unit == "F":
                return (value * 9/5) + 32
            elif to_unit == "K":
                return value + 273.15
        elif from_unit == "F":
            if to_unit == "C":
                return (value - 32) * 5/9
            elif to_unit == "K":
                return (value - 32) * 5/9 + 273.15
        elif from_unit == "K":
            if to_unit == "C":
                return value - 273.15
            elif to_unit == "F":
                return (value - 273.15) * 9/5 + 32
            
    try:
        temp_value = float(input("Enter the temperature value: "))
        from_unit = input("Convert from (C/F/K): ").upper()
        to_unit = input("Convert to (C/F/K): ").upper()

        if from_unit in ["C", "F", "K"] and to_unit in ["C", "F", "K"]:
            converted_value = convert_temperature(temp_value, from_unit, to_unit)
            print(f"{temp_value} {from_unit} is equal to {converted_value:.2f} {to_unit}")
        else:
            print("Invalid units. Please enter C, F, or K.")
            
    except ValueError:
        print("Invalid input. Please enter a numeric temperature value.")
        
    continue_choice = input("Do you want to convert another temperature? (yes/no): ").lower()
    if continue_choice != 'yes':
        running = False