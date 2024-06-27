from time import strftime
from tkinter import Label, Tk


def atualizar_relogio():
    horario_atual = strftime("%H:%M:%S %p")
    relogio.config(text=horario_atual)
    relogio.after(1000, atualizar_relogio)


root = Tk()
root.title("Relogio Digital")

relogio = Label(
    root, font=("Comic Sans", 30, "bold"), background="light green", foreground="black"
)

relogio.pack(anchor="center")

atualizar_relogio()
root.mainloop()
