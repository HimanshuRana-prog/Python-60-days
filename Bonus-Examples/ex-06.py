feet_inch = input("Enter the Feet and inches: ")
def check_height(feet_inch):
    parts = feet_inch.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])

    meters = feet * 0.3048 + inches * 0.0254
    return  meters

result = check_height(feet_inch)

if result < 1:
    print("Kid cannot use slide")
else:
    print("Kid can use the slide")
