#Syntax from where we can import data
# from function01 import get_todos , write_todos
import function01

while True:
    user_actions = input("Type ,add ,edit,complete ,show and exit:  ")
    user_actions = user_actions.strip()

    
    if user_actions.startswith('add'):
        todo = user_actions[4:] 
        todos = function01.get_todos()

        todos.append(todo + '\n')

        function01.write_todos(todos)

    elif user_actions.startswith('show') : #  (|) bitwise and or
            
        todos = function01.get_todos()

        
        for index,items in enumerate(todos):
            items = items.strip('\n')
            print(f"{index+1}:){items}")
    elif user_actions.startswith('edit'):
        try:    
            number = int(int(user_actions[5:]))
            number = number - 1

            todos = function01.get_todos()
            
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            
            function01.write_todos(todos)

        except ValueError:
            print("Your code is not valid")
            continue


    elif user_actions.startswith('complete'):
        try:
            number = int(user_actions[9:])

            todos = function01.get_todos()
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            function01.write_todos(todos)

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

    

    

