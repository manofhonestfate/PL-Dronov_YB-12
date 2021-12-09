from tkinter import*
from tkinter import ttk 
from tkinter import messagebox
from tkinter.ttk import Radiobutton
from tkinter.ttk import Combobox
from tkinter import Menu
from tkinter import scrolledtext

def calculator(a, b, c):
    result = 0
    if a == '+':
        result = b + c
    if operat == '-':
        result = b - c
    if a == '/':
        a = b / c
    if a == '*':
        result = b * c
    return result
def result():
    result = "Ответ: {}".format(calculator(calc.get(), int(num1.get()), int(num2.get())))
    messagebox.showinfo(" ",result)

def press1():
     messagebox.showinfo('Вывод:', "Вы выбрали первый вариант")
def press2():
     messagebox.showinfo('Вывод:', "Вы выбрали второй вариант")
def press3():
     messagebox.showinfo('Вывод:', "Вы выбрали третий вариант")
def cr1():
    knopka1 = Button(tab2, text="Вывод:", font=("georgia",12),command=press1)
    knopka1.grid(column=1, row=1)
def cr2():
    knopka2 = Button(tab2, text="Вывод:", font=("georgia",12),command=press2)
    knopka2.grid(column=1, row=1) 
def cr3():
    knopka3 = Button(tab2, text="Вывод:", font=("georgia",12),command=press3)
    knopka3.grid(column=1, row=1)

#корень
io=Tk()
io.title("Дронов Дмитрий Александрович")
io.geometry('500x125')
tab_control = ttk.Notebook(io)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
tab_control.add(tab1, text='Калькулятор')
tab_control.add(tab2, text='Чекбоксы')
tab_control.add(tab3, text='Файлы')
tab_control.pack(expand=1, fill='both')
chk_state = IntVar()
#чекбоксы
rad1 = Radiobutton(tab2, text='Первый', value=1,command=cr1)
rad2 = Radiobutton(tab2, text='Второй', value=2,command=cr2)
rad3 = Radiobutton(tab2, text='Третий', value=3,command=cr3)
rad1.grid(column=0, row=0)
rad2.grid(column=1, row=0)
rad3.grid(column=2, row=0)
#калькулятор
t1=Label(tab1,text="Введите числа:",font=("georgia",12))
t2=Label(tab1,text="=",font=("georgia",16))
calc=Combobox(tab1, width=2, height=3, font=(12))
num1=Entry(tab1,width=16)
num2=Entry(tab1,width=16)
calc['values'] = ("+","-","*","/")
calc.current(0)
otvet=Button(tab1,text="Ответ",font=("Georgia",12),bg="black",fg="white", command=result)
t1.grid(column=0, row=0)
t2.grid(column=3, row=1)
calc.grid(column=1, row=1)
num1.grid(column=0, row=1)
num2.grid(column=2, row=1)
otvet.grid(column=4, row=1)
#файлы
def read():
    add=open("text.txt","r")
    a=add.readline()
    text=Label(tab3,text=a,font=("Georgia",12))
    text.grid(column=0, row=1)
    add.close()
def save():
    save=open("note.txt","w")
    save.write(txt.get(1.0,END))
    txt.delete(1.0,END)
faq=Label(tab3,text="Текст из файла:",font=("Georgia",12))
faq.grid(column=0, row=0)
menu = Menu(io)
new_item = Menu(menu, tearoff=0)
new_item.add_command(label='Загрузить',command=read)
new_item.add_command(label='Сохранить', command=save)
menu.add_cascade(label='Файл', menu=new_item)
io.config(menu=menu) 
txt=scrolledtext.ScrolledText(tab3, width=40, height=10)
txt.grid(column=0, row=2) 
io.mainloop()