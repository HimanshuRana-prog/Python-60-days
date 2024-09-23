todos =[]

while True:
    user_actions = input("Type ,add ,show and exist:  ")

    match user_actions:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show':
            for items in todos:
                print(items)
        case 'exist':
            break
print("Bye!")

    

    

