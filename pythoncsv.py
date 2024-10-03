import csv

with open("waether.csv",'r') as file:
    data = list(csv.reader(file)) #This will give iterator's
    
city = input("Enter the city: ")

for row in data:
    if row[0] == city:
        print(row[1])
    
    
