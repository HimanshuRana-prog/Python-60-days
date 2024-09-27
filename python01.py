todos =[]

while True:
    user_actions = input("Type ,add ,edit,complete ,show and exit:  ")
    user_actions = user_actions.strip()

    
    if 'add' in user_actions or 'new' in user_actions:
        todo = user_actions[4:]
        
        with open('todos.txt','r') as file:
            todos = file.readlines()

        todos.append(todo)

        with open('todos.txt','w') as file:
            file.writelines(todos)

    elif 'show' in user_actions : #  (|) bitwise and or
            
        with open('todos.txt','r') as file:
            todos = file.readlines()

        
        for index,items in enumerate(todos):
            items = items.strip('\n')
            print(f"{index+1}:){items}")
    elif 'edit' in user_actions:
        number = int(int(user_actions[5:]))
        number = number - 1

        with open('todos.txt','r') as file:
            todos = file.readlines()
        
        new_todo = input("Enter new todo: ")
        todos[number] = new_todo + '\n'

        
        with open('todos.txt','w') as file:
            file.writelines(todos)


    elif 'complete' in user_actions:
        number = int(user_actions[9:])

        with open('todos.txt','r') as file:
            todos = file.readlines()
        index = number -1
        todo_to_remove = todos[index].strip('\n')
        todos.pop(index)


        with open('todos.txt','w') as file:
            file.writelines(todos)

        message = f" Todo {todo_to_remove} was removed from the list"
        print(message)
        
    elif 'exit'in user_actions:
        break
    else:
        print("command is not vaild")
print("Bye!")

    

    

