# FreeSimpleGUI: This is an alias for PySimpleGUI, allowing you to use sg to access its functions.
# extract_archive: This function is imported from a module named zip_extractor, which presumably 
# handles the extraction logic for the archives.
import FreeSimpleGUI as sg
from zip_extractor import extract_archive

sg.theme("Black") #Sets the theme for the GUI to "Black", affecting the appearance of the window

first_01 = sg.Text("Select Archive:")
input1 = sg .Input()
choose_1 = sg.FileBrowse("Choose",key= 'Archive')

second_02 = sg.Text("Select dest dir:")
input02 = sg .Input()
choose_2 = sg.FileBrowse("Choose",key='folder')

exit_button = sg.Button("Exit")
extract_button = sg.Button("Extract") #button that the user clicks to start the extraction process.
output_label = sg.Text(key = "output",text_color="green") #A text label that will display messages (e.g., extraction status)

window = sg.Window("Archive Extractor",layout = [[first_01,input1,choose_1],
                                                 [second_02,input02,choose_2],
                                                 [extract_button,output_label,exit_button]])
while True:
    event,values = window.read()
    match event:
        case "Exit":
            break
        case sg.WIN_CLOSED:
            break
    print(event,values)
    archivepath = values['Archive']
    dest_dir = values['folder']
    extract_archive(archivepath,dest_dir)
    window['output'].update(value = "Extraction completed")

window.close()