import PySimpleGUI as sg

# All the stuff inside your window.
layout = [  [sg.Text('Type the note you hear')],
            [sg.Text('Note:'), sg.InputText()],
            [sg.Button('Submit')] ]
note_dic = {''}

# Create the Window
window = sg.Window('Window Title', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    print('You entered ', values[0])

window.close()