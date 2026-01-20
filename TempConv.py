#Temperature convertor
#This program converts temperatures between Celsius, Fahrenheit, and Kelvin.
#By: Sophia Ren
#1/16/2025

#Function to convert Celsius to Kelvin
def C_to_K(input_temp):

    '''
    Convert Celsius to Kelvin.
    >>> C_to_K(0)
    273.15
    >>> C_to_K(100)
    373.15
    '''
    return input_temp + 273.15

#Function to convert Kelvin to Celsius
def K_to_C(input_temp):
    '''
    Convert Kelvin to Celsius.
    >>> K_to_C(273.15)
    0.0
    >>> K_to_C(373.15)
    100.0
    '''

    return round(input_temp - 273.15, 2)

#Function to convert Fahrenheit to Kelvin
def F_to_K(input_temp):
    '''
    Convert Fahrenheit to Kelvin.
    >>> F_to_K(32)
    273.15
    >>> F_to_K(212)
    373.15
    '''

    return (input_temp - 32) * 5/9 + 273.15

#Function to convert Kelvin to Fahrenheit
def K_to_F(kelvin_temp):
    '''
    Convert Kelvin to Fahrenheit.
    >>> K_to_F(273.15)
    32.0
    >>> K_to_F(0)
    -459.67
    '''
    return round((kelvin_temp - 273.15) * 9/5 + 32.00, 2)

#Function to check if unit is valid
def check_unit(unit):
    '''
    >>> check_unit('C')

    >>> check_unit('X')
    Invalid unit. Please enter C, F, or K.
    <class 'ValueError'>
    '''
    if unit not in ['C', 'F', 'K']:
        print("Invalid unit. Please enter C, F, or K.")
        return ValueError
    else:
        return None

#Function to convert input temperature to Kelvin
def convert_to_K(input_temp, input_unit):
    '''
    Convert temperature to Kelvin.
    >>> convert_to_K(0, 'C')
    273.15
    >>> convert_to_K(32, 'F')
    273.15
    >>> convert_to_K(300, 'K')
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

#Function to convert from Kelvin to desired output unit
def convert_from_K(kelvin_temp, output_unit):
    '''
    >>> convert_from_K(273.15, 'C')
    0.0
    >>> convert_from_K(273.15, 'F')
    32.0
    >>> convert_from_K(300, 'K')
    300
    '''
        # Convert Kelvin to output unit
    if output_unit == 'C':
        return K_to_C(kelvin_temp)
    elif output_unit == 'F':
        return K_to_F(kelvin_temp)
    elif output_unit == 'K':
        return round(kelvin_temp, 2)
#Function to check if temperature is above absolute zero   
def check_reality(kelvin_temp):
    '''
    >>> check_reality(0)

    >>> check_reality(-5)
    <class 'ValueError'>
    >>> check_reality(273.15)

    '''
    if kelvin_temp< 0:
        return ValueError
    return None
#Function to handle the conversion process
def convert():
    while True:
        #Getting valid input temperature and unit from user
        input_temp = input("Enter Initial temperature: ")
        try:
            input_temp = float(input_temp)
        except ValueError:
            print("Invalid temperature. Please enter a numeric value.")
            continue
        input_false = True
        #Loop until valid unit is entered
        while input_false == True:
            input_unit = input("Enter Initial unit (C, F, K): ").upper()
            if check_unit(input_unit) is None:
                input_false = False
        #Convert input temperature to Kelvin
        kelvin_temp = convert_to_K(input_temp, input_unit)
        if check_reality(kelvin_temp) is None:
            break
        #If temperature is below absolute zero, prompt user to re-enter both value and unit
        print("Warning: Temperature below absolute zero! Not Physically possible.")
        print("Please re-enter temperature and unit.")
    #Getting valid output unit from user
    while True:
        output_unit = input("Enter Desired unit (C, F, K): ").upper()
        if check_unit(output_unit) is None:
            break
    #Convert from Kelvin to desired output unit
    converted_temp = convert_from_K(kelvin_temp, output_unit)
    print(f"Converted temperature: {converted_temp:.2f} {output_unit}")

#Main function to run the conversion process
def main():
    while True:
        #The actual conversion process
        convert()
        #Repeating the process if user desires
        again = input("Do you want to convert another temperature? (y for yes, anything else for no): ").lower()
        if again != 'y' and again != 'yes':
            break
#Running the main function        
if __name__ == "__main__":
    main()