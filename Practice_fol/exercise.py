# If i want to share this .py file to somone and he didn't have python then we have to covert file into .exe
import FreeSimpleGUI as sg

label01 = sg.Text("Enter Feet:")
input01 = sg.Input()

label02 = sg.Text("Enter Inches:")
input02 = sg.Input()

convert_button = sg.Button("Convert")

window = sg.Window("Convertor",
                   layout = [[label01,input01],
                                         [label02,input02],
                                         [convert_button]])
window.read()
window.close()