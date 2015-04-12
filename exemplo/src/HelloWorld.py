'''
Created on 06/04/2015

@author: Marcus
'''
# Esse programa inicialmente foi criado com principio de fazer um hello word
# segunda implementação foi fazer um teste para criar um metodo em que abre uma interface com relogio

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
