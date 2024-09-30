def get_todos(filepath):
    with open(filepath,'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(filepath,todos_arg):
    with open(filepath,'w') as file:
        file.writelines(todos_arg)



while True:
    user_actions = input("Type ,add ,edit,complete ,show and exit:  ")
    user_actions = user_actions.strip()

    
    if user_actions.startswith('add'):
        todo = user_actions[4:] 
        
        todos = get_todos("todos.txt")

        todos.append(todo + '\n')

        write_todos("todos.txt",todos)

    elif user_actions.startswith('show') : #  (|) bitwise and or
            
        todos = get_todos("todos.txt")

        
        for index,items in enumerate(todos):
            items = items.strip('\n')
            print(f"{index+1}:){items}")
    elif user_actions.startswith('edit'):
        try:    
            number = int(int(user_actions[5:]))
            number = number - 1

            todos = get_todos()
            
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            
            write_todos("todos.txt",todos)

        except ValueError:
            print("Your code is not valid")
            continue


    elif user_actions.startswith('complete'):
        try:
            number = int(user_actions[9:])

            todos = get_todos("todos.txt")
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            write_todos("todos.txt",todos)

            message = f"Todo {todo_to_remove} was removed from the list."
            print(message)
        except IndexError:
            print("There is no item with that number")
            continue
    
        
    elif user_actions.startswith('exit'):
        break
    else:
        print("command is not vaild")
print("Bye!")

    

    

