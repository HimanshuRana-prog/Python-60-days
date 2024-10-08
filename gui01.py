import function01
import FreeSimpleGUI as sg
import time

sg.theme("black")

clock = sg.Text('',key='clock')

label = sg.Text("Type in To-do")
input_box = sg.InputText(tooltip= "Enter Todo",key="Todo")
add_button = sg.Button(button_color="white",size= 2,image_source = "add.png",mouseover_colors= "red",tooltip="Add todo",key="Add")
list_box = sg.Listbox(values= function01.get_todos(),
                      key = 'todos',enable_events= True,size= [45, 10])
edit_button = sg.Button("Edit",button_color= "white")
complete_button = sg.Button(button_color= "white",size=2,image_source="complete.png",mouseover_colors = "red",tooltip= "complete todo",key = "Complete")
exit_button = sg.Button("Exit",button_color= "white")

layout = [[label],
          [input_box,add_button],
          [list_box,edit_button,complete_button],
          [exit_button]]

window = sg.Window("My To-Do App", #window class is typically used to create a new window for your application
                   layout= [[clock],[label],
                   [input_box,add_button],
                   [list_box,edit_button,complete_button],
                   [exit_button]], font=('Helvetica',15),button_color='Black') 

while True:
   event, values= window.read(timeout=200)
   window['clock'].update(value = time.strftime("%b %d, %Y %H:%M:%S"))
   
   match event:
    case "Add":
        todos = function01.get_todos()
        new_todo = values['Todo'] + "\n"
        todos.append(new_todo)
        function01.write_todos(todos)
        window['todos'].update(values = todos)

    case "Edit":
        try:
            todo_to_edit = values['todos'][0]
            new_todo = values['Todo']

            todos = function01.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            function01.write_todos(todos)
            window['todos'].update(values = todos)
        except IndexError:
            sg.popup("Please Select an item First: ",font=('Helvetica',20)) #opup is a type of window that appears over your main application window to display error message
    
    case 'Complete':
        try:
            todo_to_complete = values['todos'][0]
            todos = function01.get_todos()
            todos.remove(todo_to_complete)

            function01.write_todos(todos)
            window['todos'].update(values = todos)
        except IndexError:
            sg.popup("Please select the Item:", font=('Helvetica',20))
                     
                     
    case "Exit":
           break


    case 'todos':
        window['Todo'].update(value=values['todos'][0])

    case sg.WIN_CLOSED:
        break

window.close()