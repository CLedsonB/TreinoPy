import tkinter
from tkinter import messagebox as mb
import random as rm

root = tkinter.Tk()
root.withdraw()

count = 0

msm = mb.showwarning("Atenção","Seu celular foi hackeado")

if msm == 'ok':
    msm = mb.showwarning('Aviso','Para solucionar é\nnecessario que voce prossiga')
    
if msm == 'ok':
    msm = mb.askquestion('O que acha?','Aceita viver comigo?')

while msm == 'no':
    count += 1
    msm = mb.askquestion('O que acha?','Aceita viver comigo?')
    if count == 3:
        msm = mb.showerror('Hmm','Vai apanhar feio!!')
        break
        
if msm == 'yes':
    msm = mb.showinfo('Sempre soube','Fez uma otima escolha')