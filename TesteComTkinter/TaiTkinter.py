import tkinter
from tkinter import messagebox as mb
import os

root = tkinter.Tk()
root.withdraw()

# aviso pra dizer 5 fatos

msm = mb.showinfo('AVISO!!!','5 fatos sobre\nTai  (>.<)')

# lista de fatos

lista = ['É a pessoa mais linda',
            'Dona do meu coração',
            'Tão meiga e doce <3',
            'Seu amor e cuidado\nAlegram o meu coração',
            'A melhor pessoa\nque pudia tá\nao meu lado']

for text in lista:
    msm = mb.showwarning('AMOR DA MINHA VIDA',text)
    
msm = mb.showerror('FIM','E voltamos outro\nDia com a parte 2')