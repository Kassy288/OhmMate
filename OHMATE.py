def voltage(current, resistance):
    return current * resistance

def resistance(current, voltage):
    if current == 0:
        return None
    else:
         return voltage / current

def current(resistance, voltage):
    return voltage / resistance
    
#define a function to calculate the total resistance of resisistance
def equivalent_resistance():
    try:
        resistors = input(
            "Enter resistor values separated by spaces (Ω): "
        )

        resistors = [float(r) for r in resistors.split()]

        if not resistors:
            print("Error: Enter at least one resistor.")
            return

        if any(r <= 0 for r in resistors):
            print("Error: Resistance values must be positive.")
            return

        connection = input(
            "Choose connection (series/parallel): "
        ).strip().lower()

        if connection == "series":
            total = sum(resistors)
            formula = "Rₜ = R₁ + R₂ + ... + Rₙ"

        elif connection == "parallel":
            total = 1 / sum(1 / r for r in resistors)
            formula = "1/Rₜ = 1/R₁ + 1/R₂ + ... + 1/Rₙ"

        else:
            print("Invalid connection type.")
            return

        print(f"\nConnection: {connection.title()}")
        print(f"Resistors: {resistors} Ω")
        print(f"Equivalent resistance: {total:.4f} Ω")

    except ValueError:
        print("Error: Enter valid numbers only.")
        


# define a function to calculate power 
def power(resistance_value, voltage_value, current_value):
	if  resistance_value is None:
	 	power = current_value * voltage_value
	 	return power
	elif current_value is None :
		power = voltage_value**2/resistance_value
		return power 
	elif voltage_value is None:
		power = current_value**2 * resistance_value
		return power
	else :
		print("Invalid input")
		



while True:

    print("""
OHMMATE 

I  - Current
V  - Voltage
R  - Resistance
P  - Power
Rt - Total resistance
X  - Exit

""")

    user_input = input("Select an operation: ").strip().lower()

    if user_input == "x":
        print("Thank you for using OhmMate!")
        break

    try:

        if user_input == "i":

            voltage_value = float(input("Enter voltage (V): "))
            resistance_value = float(input("Enter resistance (Ω): "))

            if resistance_value <= 0:
                print("Error: Resistance must be positive.")
            else:
                result = current(resistance_value, voltage_value)
                print(f"Current: {result:.4f} A")

        elif user_input == "v":

            current_value = float(input("Enter current (A): "))
            resistance_value = float(input("Enter resistance (Ω): "))

            result = voltage(current_value, resistance_value)
            print(f"Voltage: {result:.4f} V")

        elif user_input == "r":

            voltage_value = float(input("Enter voltage (V): "))
            current_value = float(input("Enter current (A): "))

            if current_value == 0:
                print("Error: Current cannot be zero.")
            else:
                result = resistance(current_value, voltage_value)
                print(f"Resistance: {result:.4f} Ω")

        elif user_input == "p":

            print("""
Choose the two quantities you know:

CR - Current and Resistance
VR - Voltage and Resistance
CV - Current and Voltage
""")

            power_input = input("Select an option: ").strip().lower()

            if power_input == "cr":

                current_value = float(input("Enter current (A): "))
                resistance_value = float(input("Enter resistance (Ω): "))

                result = power(resistance_value, None, current_value)
                print(f"Power: {result:.4f} W")

            elif power_input == "vr":

                voltage_value = float(input("Enter voltage (V): "))
                resistance_value = float(input("Enter resistance (Ω): "))

                if resistance_value == 0:
                    print("Error: Resistance cannot be zero.")
                else:
                    result = power(resistance_value, voltage_value, None)
                    print(f"Power: {result:.4f} W")

            elif power_input == "cv":

                current_value = float(input("Enter current (A): "))
                voltage_value = float(input("Enter voltage (V): "))

                result = power(None, voltage_value, current_value)
                print(f"Power: {result:.4f} W")

            else:
                print("Invalid power option.")

        elif user_input == "rt":

            equivalent_resistance()

        else:
            print("Invalid operation type.")

    except ValueError:
        print("Error: Enter valid numbers only.")

    input("\nPress Enter to return to the main menu...")