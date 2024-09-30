password = input("Enter the password: ")
result = {}

if len(password)>= 8:
    result['Length'] = True
else:
    result['Length']= False 

digit = False
for i in password:
    if i.isdigit():
        digit = True

result['Digit'] = digit

uppercase = False
for i in password:
    if i.isupper():
        uppercase = True

result['Uppercase'] = uppercase


print(result)
if all(result) == True:#Here all function check if all the condition are true then it return true else it return false any of the condition is false
    print("Strong ") 
else:
    print("Weak Password")
    