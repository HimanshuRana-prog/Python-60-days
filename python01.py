todos =[]

while True:
    user_actions = input("Type ,add ,edit ,show and exit:  ")
    user_actions = user_actions.strip()

    match user_actions:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show' |  'display': #  (|) bitwise and or
<<<<<<< HEAD
            for items in todos:
                items= items.title()
                print(items)
=======
            for index,items in enumerate(todos):
               print(f"{index+1}:){items}")
>>>>>>> for_loop_added
        case 'edit':
            number = int(input("enter the number of todo edit: "))
            number = number-1
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo
<<<<<<< HEAD
=======
        case 'complete':
            number = int(input("enter the number of todo complete: "))
            todos.pop(number-1)
>>>>>>> for_loop_added
            
        case 'exit':
            break
print("Bye!")

    

    

