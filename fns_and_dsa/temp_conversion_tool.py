# Definition of global variables
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

# Function to convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

# Function to convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

# Main program logic
def main():
    try:
        # Prompt user for temperature input
        temp_input = input("Enter the temperature value: ").strip() 
        
        # Try to convert the input to float, raise an error if not numeric
        temperature = float(temp_input)

        # Ask for temperature unit
        unit = input("Is this in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit == 'C':
            converted = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is equal to {converted:.2f}°F.")
        elif unit == 'F':
            converted = convert_to_celsius(temperature)
            print(f"{temperature}°F is equal to {converted:.2f}°C.")
        else:
            raise ValueError("Invalid temperature unit. Please enter 'C' or 'F'.")
    
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")

# Call main only when script is executed directly
if __name__ == "__main__":
    main()
