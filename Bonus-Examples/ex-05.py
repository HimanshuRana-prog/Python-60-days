def get_avg(): #Here we are defining function
    with open("text-folder/data.txt",'r') as file: #Then we are reading a file name as data.txt
        data = file.readlines()
    values = data[1:] # Here we starting value from 1 beacuse 0 has string 
    values = [float(i) for i in values] # we convert string into float
    average_local = sum(values) / len(values) # we are finding the avg
    return average_local # return 

average = get_avg()
print(average)