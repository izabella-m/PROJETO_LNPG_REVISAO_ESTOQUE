from tkinter import *
from tkinter.ttk import Combobox


# inserir nome do produto,
# quantidade em estoque
# preço unitário
# um campo de seleção se o produto é gelado ou não
def adicionar():
    with open ('estoque.txt', 'a', encoding='UTF-8') as arquivo:
        arquivo.write(txtestoque.get() +',' + qtdestoque.get()+',' + precounitario.get()+',')
        arquivo.close()
var = Tk()

var.title("Estoque")
var.geometry("500x500")


lbl= Label(var, text="Nome do Produto", fg="pink", font=("Helvetica", 16))
lbl.place(x=80, y=10)

txtestoque=Entry(var, text="Nome do Produto", bd=2)
txtestoque.place(x=80, y=40)

lbl1= Label(var, text="Quantidade em estoque", fg="pink", font=("Helvetica", 16))
lbl1.place(x=80, y=80)

qtdestoque=Entry(var, text="Quantidade em estoque", bd=2)
qtdestoque.place(x=80, y=120)

lbl2= Label(var, text="Preço Unitário", fg="pink", font=("Helvetica", 16))
lbl2.place(x=80, y=180)

precounitario=Entry(var, text="Preço Unitário", bd=2)
precounitario.place(x=80, y=220)


data = ("gelado", "não gelado")
lb=Listbox(var, height=4, selectmode='single')
for num in data:
    lb.insert(END,num)
lb.place(x=80, y=250)

btn = Button(var, text='Adicionar', command=adicionar)
btn.place(x=80, y=350)

btn = Button(var, text='Limpar')
btn.place(x=150, y=350)


var.mainloop()
#if nome("")