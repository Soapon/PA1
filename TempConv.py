#Temperature convertor - 1st Draft
#This program converts temperatures between Celsius, Fahrenheit, and Kelvin.

def C_to_K(input_temp):

    '''
    Convert Celsius to Kelvin.
    >>> C_to_K(0)
    273.15
    >>> C_to_K(100)
    373.15
    '''

    return input_temp + 273.15

def K_to_C(input_temp):
    '''
    Convert Kelvin to Celsius.
    >>> K_to_C(273.15)
    0.0
    >>> K_to_C(373.15)
    100.0
    '''

    return input_temp - 273.15

def F_to_K(input_temp):
    '''
    Convert Fahrenheit to Kelvin.
    >>> F_to_K(32)
    273.15
    >>> F_to_K(212)
    373.15
    '''

    return (input_temp - 32) * 5/9 + 273.15

def K_to_F(input_temp):
    '''
    Convert Kelvin to Fahrenheit.
    >>> K_to_F(273.15)
    32.00
    >>> K_to_F(0)
    -459.67
    '''
    return (input_temp - 273.15) * 9/5 + 32

def check_unit(unit):
    if unit not in ['C', 'F', 'K']:
        print("Invalid unit. Please enter C, F, or K.")
        return ValueError
    return None

def convert_to_K(input_temp, input_unit):
    '''
    Convert temperature to Kelvin.
    >>> convert_temperature(0, 'C')
    273.15
    >>> convert_temperature(32, 'F')
    273.15
    >>> convert_temperature(300, 'K')
    300
    '''
    kelvin_temp = None
    # Convert input to Kelvin first
    if input_unit == 'C':
        kelvin_temp = C_to_K(input_temp)
    elif input_unit == 'F':
        kelvin_temp = F_to_K(input_temp)
    elif input_unit == 'K':
        kelvin_temp = input_temp
    return kelvin_temp


def convert_from_K(kelvin_temp, output_unit):
        # Convert Kelvin to output unit
    if output_unit == 'C':
        return K_to_C(kelvin_temp)
    elif output_unit == 'F':
        return K_to_F(kelvin_temp)
    elif output_unit == 'K':
        return kelvin_temp
    
def check_reality(kelvin_temp):
    if kelvin_temp< 0:
        return ValueError
    
    return None

def convert():
    while True:
        input_temp = float(input("Enter Initial temperature: "))
        while True:
            input_unit = input("Enter Initial unit (C, F, K): ").upper()
            if check_unit(input) is None:
                break
        kelvin_temp = convert_to_K(input_temp, input_unit)
        if check_reality(kelvin_temp) is None:
            break
        print("Warning: Temperature below absolute zero! Not Physically possible.")
        print("Please re-enter temperature and unit.")

    while True:
        output_unit = input("Enter Desired unit (C, F, K): ").upper()
        if check_unit(output_unit) is None:
            break
    converted_temp = convert_from_K(kelvin_temp, output_unit)
    print(f"Converted temperature: {converted_temp:.2f} {output_unit}")

def main():
    while True:
        convert()
        again = input("Do you want to convert another temperature? (y for yes): ").lower()
        if again != 'y':
            break
        
if __name__ == "__main__":
    main()