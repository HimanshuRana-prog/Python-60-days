todos =[]

while True:
    user_actions = input("Type ,add ,edit ,show and exit:  ")
    user_actions = user_actions.strip()

    match user_actions:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show' |  'display': #  (|) bitwise and or
            for items in todos:
                items= items.title()
                print(items)
        case 'edit':
            number = int(input("enter the number of todo edit: "))
            number = number-1
            existing_todo = todos[number]
            print(existing_todo)
        case 'exit':
            break
print("Bye!")

    


    

