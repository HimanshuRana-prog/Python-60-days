feet_inch = input("Enter the Feet and inches: ")
def parse(feet_inch):
    parts = feet_inch.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])
    return {"feet": feet,"inches": inches}

    

def check_height(feet,inches):
    meters = feet * 0.3048 + inches * 0.0254
    return  meters

parsed = parse(feet_inch)
result = check_height(parsed['feet'] , parsed['inches'])

print(f"{parsed['feet']} feet and {parsed['inches']} is equal to {result} ")

if result < 1:
    print("Kid cannot use slide")
else:
    print("Kid can use the slide")
