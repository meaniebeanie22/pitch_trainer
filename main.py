import PySimpleGUI as sg
import random
from playsound import playsound

# All the stuff inside your window.
layout = [  [sg.Text('Type the note you hear')],
            [sg.Text('Note:'), sg.InputText()],
            [sg.Button('Submit')],
            [sg.Text('Answer:'), sg.Text(key='-OUTPUT-')] ]
note_dic = {
    'a.mp3':['a'],
    'bflat.mp3':['bb','a#'],
    'b.mp3':['b','cb'],
    'c.mp3':['c','b#'],
    'csharp.mp3':['c#','db'],
    'd.mp3':['d'],
    'eflat.mp3':['eb','d#'],
    'e.mp3':['e','fb'],
    'f.mp3':['f','e#'],
    'fsharp.mp3':['f#','gb'],
    'g.mp3':['g'],
    'gsharp.mp3':['g#','ab']
}

# Create the Window
window = sg.Window('Pitch Trainer', layout)

# pick a note to start
note = random.choice(list(note_dic.keys()))
playsound(note, False) # play it

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read() #get events and values
    if event == sg.WIN_CLOSED: # if user closes window
        break
    if event == 'Submit': # check answer
        if values[0] in note_dic[note]: # correct
            window['-OUTPUT-'].update('Correct!') # change text to give dopamine
            note = random.choice(list(note_dic.keys())) # pick new note
            playsound(note, False)
            
        else: # nope
            window['-OUTPUT-'].update('Nope!') 

window.close()