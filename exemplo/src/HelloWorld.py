'''
Created on 06/04/2015

@author: Marcus
'''

import Tkinter
from time import strftime
relogio = Tkinter.Label()
relogio.pack()
relogio['font'] = 'Helvetica 120 bold'
relogio['text'] = strftime('%H:%M:%S')
def tictac():
    agora = strftime('%H:%M:%S')
    if agora != relogio['text']:
        relogio['text'] = agora
    relogio.after(100, tictac)


if __name__ == '__main__':
    variavel = 'Hello World'
    print variavel
    tictac()
    relogio.mainloop()
