FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9 
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    new_temp = FAHRENHEIT_TO_CELSIUS_FACTOR * fahrenheit
    return new_temp
def convert_to_fahrenheit(celsius):
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    new_temp = CELSIUS_TO_FAHRENHEIT_FACTOR * celsius
    return new_temp

while True:
    try:
        temp = int(input("Enter the temprature to convert: "))
        break
    except:
        print("Please,Enter a valid number.")

while True:
    cel_or_faher = input("Is the temprature in Celsius or Fahrenheit? (C/F): ").capitalize()
    if cel_or_faher == "C":
        print(f"{temp}°F is {convert_to_fahrenheit(temp)}°C")
        break
    elif cel_or_faher == "F":
        print(f"{temp}°C is {convert_to_celsius(temp)}°F")
        break
    else:
        print("Please,Enter a correct degree type.")

        
