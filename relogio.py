from tkinter import *
from time import strftime
from datetime import datetime
import pytz 

janela = Tk()
janela.title("Relógio Digital")

fuso_usa = False

def atualizar_hora():
   if fuso_usa:
      tz = pytz.timezone('America/New_York')
      hora_atual = datetime.now(tz).strftime('%H:%M:%S %p')
   else: 
      hora_atual = strftime('%H:%M:%S %p')
   label.config(text=hora_atual)
   label.after(1000, atualizar_hora)
def mudar_fuso():
   global fuso_usa
   fuso_usa = not fuso_usa
   if fuso_usa:
      botao.config(text="mudar para  Brasil")
   else:
      botao.config(text="mudar para EUA")


label = Label(janela, font=('calibri', 40, 'bold'), background='black', foreground='white')
label.pack(anchor='center')

botao = Button(janela, text="mudar para EUA", command=mudar_fuso)
botao.pack()


atualizar_hora()
janela.mainloop()