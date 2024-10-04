import function01
import FreeSimpleGUI as sg

label = sg.Text("Type in To-do")
input_box = sg.InputText(tooltip= "Enter Todo",key="Todo")
add_button = sg.Button("Add")
window = sg.Window("My To-Do App", #window class is typically used to create a new window for your application
                   layout= [[label],[input_box,add_button]], 
                   font=('Helvetica',15)) 

while True:
   event, values= window.read()
   print(event)
   print(values)
   match event:
    case "Add":
         todos = function01.get_todos()
         new_todo = values['Todo'] + "\n"
         todos.append(new_todo)
         function01.write_todos(todos)
    case sg.WIN_CLOSED:
         break
     
window.close()