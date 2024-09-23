todos =[]

while True:
    user_actions = input("Type ,add ,show and exist:  ")

    match user_actions:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show':
            print(todos)
        case 'exist':
            break
print("Bye!")

    


    

