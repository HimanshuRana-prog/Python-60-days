try:    
    width = float(input("Enter the width: "))
    length = float(input("Enter the length: "))
    if width == length:
        exit("Thats look like a square!")
    area = width * length
    print(f"Tis is the {area}")
except ValueError:
    print('Please enter the number')