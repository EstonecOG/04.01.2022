from tkinter import *
click=0
def clicker(event): #Если используем bind то используем (event)
    global click
    click+=1
    lbl.configure(text=click)
def clicker_minus(event):
    global click
    click-=1
    lbl.configure(text=click)
def txt_to_lbl(event):
    #pass болванка 
    text=txt.get() #From Entry to text 
    lbl.configure(text=text)
    txt.delete(0,END) #Стереть текст  
def valik():
    valika=var.get()
    lbl.configure(text=valika)
    txt.insert(0,valika)#Вставить текст в ящик, куда на какую позицию, 0 - нулевой символ, и так далее
def x2(event):
    global x2
    click==click*2
    lbl.configure(text=click*2)

okno=Tk() #Создаем полотно для вкладки а также метод Tk и скобки
okno.title("Nazvanie okna") #Точка перед переменной имеет функцию метода, можно вписать любой метод из списка
okno.geometry("700x7000") #Метод отвечает за размер окна.
knopka=Button(okno, text="Endla +",font="Arial 20", fg="red", bg="lightblue", height=4, width=20, relief=GROOVE) #С большой буквы!!! Конструкторы пишуться с большой. Этот класс дает класс кнопки переменной. в скобках вводим параметры где находиться кнопка - на вкладке "okno" после названия идут настройки #fg - цвет текста #bg - цвет фона #relief - RAISED, SUNKEN.
knopka1=Button(okno, text="x2",font="Arial 10", fg="red", bg="lightblue", height=2, width=5, relief=GROOVE)
knopka1.bind("<Button-1>", x2)
knopka.bind("<Button-1>", clicker)#Кликабельная кнопка, событие пишеться в ковычках и угловых скобках. LMB
knopka.bind("<Button-3>", clicker_minus) #RMB
lbl=Label(okno, text="Rollin a joint", font="Arial 20", height=4, width=20, fg="green", bg="lightblue")
txt=Entry(okno, fg="red", bg="lightblue", width=20, relief=GROOVE, font="Arial 20", justify=CENTER)#Entry ввод текста для одной строки, justify = выравнивание по центру
txt.bind("<Return>", txt_to_lbl) #Enter
i1=PhotoImage(file="1.gif")
i2=PhotoImage(file="giphy.gif")
i3=PhotoImage(file="giphy (1).gif")
var=StringVar()
var.set(1)
r1=Radiobutton(okno, image=i1, variable=var, value="Odin", command=valik)# 
r2=Radiobutton(okno, image=i2, variable=var, value="Dva", command=valik)
r3=Radiobutton(okno, image=i3, variable=var, value="Tri", command=valik)

knopka1.pack()
txt.pack()
lbl.pack()
knopka.pack() #Метод pack самый легкий метод отображения элементов,!!!(side=LEFT,TOP,RIGHT)
r1.pack(side=LEFT)
r2.pack(side=LEFT)
r3.pack(side=LEFT)
okno.mainloop()#Запуск окна, чтобы оно появилось на экран