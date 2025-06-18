from tkinter import *
from tkinter import ttk
import math
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import filedialog
from PIL import Image, ImageTk
import requests
from io import BytesIO
import random


#cores

co1 = '#feffff'
co2 = '#6f9fbd'
co3 = '#38576b'

fundo = "#F8F8F8"
co10 = "#2c343c"
cor11 = "#3c3c3c"


cor1= '#ffab40'
cor2= '#ff333a'
cor3= '#6bd66f'
cor4= '#ab8918'

#janela

janela = Tk()
janela.title('Davi a calculadora')
janela.geometry('235x289')
janela.configure(bg=co1)



Style = ttk.Style(janela)
Style.theme_use("clam")


#frame

ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=280)


Frame_score= Frame(janela, width=300, height=56, bg=co3, pady=0, padx=0, relief="flat",)
Frame_score.grid(row=1,column=0, sticky=NW)

Frame_cientifica= Frame(janela, width=300, height=86, bg=co3, pady=0, padx=0, relief="flat",)
Frame_cientifica.grid(row=2,column=0, sticky=NW)

Frame_quadros= Frame(janela, width=300, height=340, bg=fundo, pady=0, padx=0, relief="flat",)
Frame_quadros.grid(row=3,column=0, sticky=NW)

#funções


def entering_valures(event):
    global all_valures
    all_valures = all_valures + str(event)
    value_text.set(all_valures)


def calculate():
    global all_valures
    global texto
    texto = all_valures

    modulos = ['math.tan', 'math.sim', 'math.cos', 'math.sqrt', 'math.log',  'math.tam10', 'math.e', 'math.pow', 'math.pi', 'math.radians' ]
   

    for i in modulos:
        if i == 'math.tan':
            texto = texto.replace("tan", i)
        if i == 'math.sim':
            texto = texto.replace("sim", i)
        if i == 'math.cos':
            texto = texto.replace("cos", i)
        if i == 'math.sqrt':
            texto = texto.replace("log", i)
        if i == 'math.log10':
            texto = texto.replace("log10", i)
        if i == 'math.e':
            texto = texto.replace("e", i)
        if i == 'math.pow':
            texto = texto.replace("pow", i)
        if i == 'math.pi':
            texto = texto.replace("pi", i)
        if i == 'math.radian':
            texto = texto.replace("radians", i)

    result = str(eval(texto))
   
    print(result)
    print(texto)


    value_text.set(result)
    all_valures = ""

def sream_clear():
    global all_valures
    all_valures = ""
    value_text.set("")

def abrir_imagem():
    img = Image.open("Seu_caminho_de_foto_png")
    img = img.resize((200, 200))
    img_tk = ImageTk.PhotoImage(img)

    for _ in range(1):
        creditos = Toplevel(janela)
        creditos.title("Susto")
        creditos.geometry("150x100")

        # Pega a largura e altura da tela
        largura_tela = creditos.winfo_screenwidth()
        altura_tela = creditos.winfo_screenheight()

        # Gera posição aleatória para a janela dentro da tela
        x = random.randint(0, largura_tela - 400)
        y = random.randint(0, altura_tela - 400)
        creditos.geometry(f"+{x}+{y}")

        label = Label(creditos, image=img_tk)
        label.image = img_tk
        label.pack()






creditos = tk.Toplevel(janela)


creditos.title('Créditos IRADOS B)')
creditos.geometry('200x200')
creditos.configure(bg=co1)


all_valures = ""

value_text = StringVar()

app_sream = Label(Frame_score, width=16, height=2, textvariable= value_text, padx=7, relief="flat", anchor="e", bd=0, justify=RIGHT, font=('Ivy 18'), bg="#1c1c2c", fg=co1)
app_sream.place(x=0, y=0)

#buttons
b_tan = Button(Frame_cientifica, text = "tan", width=6, height=1, bg=co10, fg=fundo, font=('lvy 10 bold'), relief=RAISED, overrelief=RIDGE, command=lambda:entering_valures('tan'))
b_tan.place(x=0,y=1)
b_sin = Button(Frame_cientifica, text = "sin", width=6, height=1, bg=co10, fg=fundo, font=('lvy 10 bold'), relief=RAISED, overrelief=RIDGE, command=lambda:entering_valures('sin'))
b_sin.place(x=59,y=1)
b_cos = Button(Frame_cientifica, text = "cos", width=6, height=1, bg=co10, fg=fundo, font=('lvy 10 bold'), relief=RAISED, overrelief=RIDGE, command=lambda:entering_valures('cos'))
b_cos.place(x=118,y=1)
b_sqrt = Button(Frame_cientifica, text = "sqrt", width=6, height=1, bg=co10, fg=fundo, font=('lvy 10 bold'), relief=RAISED, overrelief=RIDGE, command=lambda:entering_valures('sqrt'))
b_sqrt.place(x=177,y=1)
b_log = Button(Frame_cientifica, text = "log", width=6, height=1, bg=co10, fg=fundo, font=('lvy 10 bold'), relief=RAISED, overrelief=RIDGE, command=lambda:entering_valures('log'))
b_log.place(x=0,y=30)
b_log10 = Button(Frame_cientifica, text = "log10", width=6, height=1, bg=co10, fg=fundo, font=('lvy 10 bold'), relief=RAISED, overrelief=RIDGE, command=lambda:entering_valures('log10'))
b_log10.place(x=59,y=30)
b_euler = Button(Frame_cientifica, text = "e", width=6, height=1, bg=co10, fg=fundo, font=('lvy 10 bold'), relief=RAISED, overrelief=RIDGE, command=lambda:entering_valures('e'))
b_euler.place(x=118,y=30)
b_pow = Button(Frame_cientifica, text = "pow", width=6, height=1, bg=co10, fg=fundo, font=('lvy 10 bold'), relief=RAISED, overrelief=RIDGE, command=lambda:entering_valures('pow'))
b_pow.place(x=177,y=30)
b_12 = Button(Frame_cientifica, text = "pi", width=6, height=1, bg=co10, fg=fundo, font=('lvy 10 bold'), relief=RAISED, overrelief=RIDGE, command=lambda:entering_valures('pi'))
b_12.place(x=0,y=58)
b_13 = Button(Frame_cientifica, text = ",", width=6, height=1, bg=co10, fg=fundo, font=('lvy 10 bold'), relief=RAISED, overrelief=RIDGE, command=lambda:entering_valures(','))
b_13.place(x=59,y=58)
b_14 = Button(Frame_cientifica, text = "(", width=6, height=1, bg=co10, fg=fundo, font=('lvy 10 bold'), relief=RAISED, overrelief=RIDGE, command=lambda:entering_valures('( '))
b_14.place(x=118,y=58)
b_15 = Button(Frame_cientifica, text = ")", width=6, height=1, bg=co10, fg=fundo, font=('lvy 10 bold'), relief=RAISED, overrelief=RIDGE, command=lambda:entering_valures(') '))
b_15.place(x=177,y=58)
b_1 = Button(Frame_quadros, text = "c", width=14, height=1, bg=cor11, fg=fundo, font=('lvy 10 bold'), relief=RAISED, overrelief=RIDGE, command=lambda:sream_clear())
b_1.place(x=0,y=0)
b_2 = Button(Frame_quadros, text = "%", width=6, height=1, bg=cor11, fg=fundo, font=('lvy 10 bold'), relief=RAISED, overrelief=RIDGE, command=lambda:entering_valures('%'))
b_2.place(x=118,y=0)
b_3 = Button(Frame_quadros, text = "/", width=6, height=1, bg=cor11, fg=fundo, font=('lvy 10 bold'), relief=RAISED, overrelief=RIDGE, command=lambda:entering_valures('/'))
b_3.place(x=177,y=0)
b_4 = Button(Frame_quadros, text = "7", width=6, height=1, bg=cor11, fg=fundo, font=('lvy 10 bold'), relief=RAISED, overrelief=RIDGE, command=lambda:entering_valures(7))
b_4.place(x=0,y=29)
b_5 = Button(Frame_quadros, text = "8", width=6, height=1, bg=cor11, fg=fundo, font=('lvy 10 bold'), relief=RAISED, overrelief=RIDGE, command=lambda:entering_valures(8))
b_5.place(x=59,y=29)
b_6 = Button(Frame_quadros, text = "9", width=6, height=1, bg=cor11, fg=fundo, font=('lvy 10 bold'), relief=RAISED, overrelief=RIDGE, command=lambda:entering_valures(9))
b_6.place(x=118,y=29)
b_7 = Button(Frame_quadros, text = "*", width=6, height=1, bg=cor11, fg=fundo, font=('lvy 10 bold'), relief=RAISED, overrelief=RIDGE, command=lambda:entering_valures('*'))
b_7.place(x=177,y=29)
b_8 = Button(Frame_quadros, text = "4", width=6, height=1, bg=cor11, fg=fundo, font=('lvy 10 bold'), relief=RAISED, overrelief=RIDGE, command=lambda:entering_valures(4))
b_8.place(x=0,y=58)
b_9 = Button(Frame_quadros, text = "5", width=6, height=1, bg=cor11, fg=fundo, font=('lvy 10 bold'), relief=RAISED, overrelief=RIDGE, command=lambda:entering_valures(5))
b_9.place(x=59,y=58)
b_10 = Button(Frame_quadros, text = "6", width=6, height=1, bg=cor11, fg=fundo, font=('lvy 10 bold'), relief=RAISED, overrelief=RIDGE, command=lambda:entering_valures(6))
b_10.place(x=118,y=58)
b_11 = Button(Frame_quadros, text = "-", width=6, height=1, bg=cor11, fg=fundo, font=('lvy 10 bold'), relief=RAISED, overrelief=RIDGE, command=lambda:entering_valures('-'))
b_11.place(x=177,y=58)
b_12 = Button(Frame_quadros, text = "1", width=6, height=1, bg=cor11, fg=fundo, font=('lvy 10 bold'), relief=RAISED, overrelief=RIDGE, command=lambda:entering_valures(1))
b_12.place(x=0,y=87)
b_13 = Button(Frame_quadros, text = "2", width=6, height=1, bg=cor11, fg=fundo, font=('lvy 10 bold'), relief=RAISED, overrelief=RIDGE, command=lambda:entering_valures(2))
b_13.place(x=59,y=87)
b_14= Button(Frame_quadros, text = "3", width=6, height=1, bg=cor11, fg=fundo, font=('lvy 10 bold'), relief=RAISED, overrelief=RIDGE, command=lambda:entering_valures(3))
b_14.place(x=118,y=87)
b_15= Button(Frame_quadros, text = "+", width=6, height=1, bg=cor11, fg=fundo, font=('lvy 10 bold'), relief=RAISED, overrelief=RIDGE, command=lambda:entering_valures("+"))
b_15.place(x=177,y=87)
b_16= Button(Frame_quadros, text = "0", width=14, height=1, bg=cor11, fg=fundo, font=('lvy 10 bold'), relief=RAISED, overrelief=RIDGE, command=lambda:entering_valures(0))
b_16.place(x=0,y=116)
b_17= Button(Frame_quadros, text = ".", width=6, height=1, bg=cor11, fg=fundo, font=('lvy 10 bold'), relief=RAISED, overrelief=RIDGE, command=lambda:entering_valures("."))
b_17.place(x=118,y=116)
b_18= Button(Frame_quadros, text = "=", width=6, height=1, bg=cor11, fg=fundo, font=('lvy 10 bold'), relief=RAISED, overrelief=RIDGE, command=lambda:calculate())
b_18.place(x=177,y=116)

label_imagem = Label(creditos, bg="#ffe4f0")
label_imagem.pack()



botao_imagem = Button(creditos, text="Abrir Imagem", command=abrir_imagem, bg="#ec407a", fg="white", font=("Arial", 10, "bold"))
botao_imagem.place(x=75, y=75)

janela.mainloop()