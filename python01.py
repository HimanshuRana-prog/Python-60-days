todos =[]

while True:
    user_actions = input("Type ,add ,edit ,show and exit:  ")
    user_actions = user_actions.strip()

    match user_actions:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show' |  'display': #  (|) bitwise and or
            for index,items in enumerate(todos):
               print(f"{index+1}:){items}")
        case 'edit':
            number = int(input("enter the number of todo edit: "))
            number = number-1
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo
        case 'complete':
            number = int(input("enter the number of todo complete: "))
            todos.pop(number-1)
            
        case 'exit':
            break
print("Bye!")

    

    

