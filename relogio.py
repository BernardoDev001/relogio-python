from tkinter import *
from time import strftime

janela = Tk()
janela.title("Relógio Digital")

def atualizar_hora():
    hora_atual = strftime('%H:%M:%S %p')
    label.config(text=hora_atual)
    label.after(1000, atualizar_hora)

label = Label(janela, font=('calibri', 40, 'bold'), background='black', foreground='white')
label.pack(anchor='center')

atualizar_hora()
janela.mainloop()