import PySimpleGUI as sg
import random
from playsound import playsound
# voodoo magic
QT_ENTER_KEY1 = 'special 16777220'
QT_ENTER_KEY2 = 'special 16777221'

#score tracker
tries = 0
correct = 0

# All the stuff inside your window.
layout = [  [sg.Text('Type the note you hear')],
            [sg.Text('Note:'), sg.InputText(key='-IN-')],
            [sg.Button('Play Again'), sg.Button('Play C')],
            [sg.Text('Answer:'), sg.Text(key='-OUTPUT-'), sg.Text('0/0', key='-SCORE-', justification='right')] ]
file_to_note = {
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
    'aflat.mp3':['g#','ab']
}
note_to_file = {
    'a':'a.mp3',
    'bb':'bflat.mp3',
    'a#':'bflat.mp3',
    'b':'b.mp3',
    'cb':'b.mp3',
    'c':'c.mp3',
    'b#':'c.mp3',
    'c#':'csharp.mp3',
    'db':'csharp.mp3',
    'd':'d.mp3',
    'eb':'eflat.mp3',
    'd#':'eflat.mp3',
    'e':'e.mp3',
    'fb':'e.mp3',
    'f':'f.mp3',
    'e#':'f.mp3',
    'f#':'fsharp.mp3',
    'gb':'fsharp.mp3',
    'g':'g.mp3',
    'g#':'aflat.mp3',
    'ab':'aflat.mp3'
}

# Create the Window
window = sg.Window('Pitch Trainer', layout, return_keyboard_events=True)

# pick a note to start
note = random.choice(list(file_to_note.keys()))
playsound(note, False) # play it

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read() #get events and values
    if event == sg.WIN_CLOSED: # if user closes window
        break

    if event in ('\r', QT_ENTER_KEY1, QT_ENTER_KEY2): # check answer
        if values['-IN-'] in file_to_note[note]: # correct
            window['-OUTPUT-'].update('Correct!') # change text to give dopamine
            correct += 1
            
        else:
            message = 'Nope! You chose', values['-IN-'], 'It was a ' + '/'.join(file_to_note[note])
            window['-OUTPUT-'].update(message)
            playsound(note_to_file[values['-IN-']])
            playsound(note)
            
        tries += 1
        window['-SCORE-'].update((str(correct) + '/' + str(tries)))
        note = random.choice(list(file_to_note.keys())) # pick new note
        window['-IN-'].update('')
        playsound(note)
        

    if event == 'Play Again': # play sound again
        playsound(note)
    if event == 'Play C': #play c (for a baseline if wus)
        playsound('c.mp3')
window.close()