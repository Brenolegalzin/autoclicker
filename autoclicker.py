import tkinter
import time
import pyautogui
from threading import Thread
screen = tkinter.Tk()
screen.title("autoclicker TK")
screen.geometry("800x500")
Text1 = tkinter.Label(screen, text="digite o tempo entre os clicks(apenas numeros)")
Text1.pack()
Input = tkinter.Entry(screen)
Input.pack()
Text2 = tkinter.Label(screen, text="digite esquerda ou direita sem maiuscula ou qualquer mudanca, isso determina qual lado do mouse")
Text2.pack()
Input2 = tkinter.Entry(screen)
Input2.pack()
pyautogui.FAILSAFE = False
count = 10
clicksAtivado = False
def cliques():
	global count,clicksAtivado
	while clicksAtivado:
		if count>0:
			time.sleep(1)
			count -= 1
			screen.update()
			Text3.config(text=count)
		else:
			time.sleep(float(Input.get()))
			clique = Input2.get()
			if clique=="esquerda":
				pyautogui.click(button="left")
			elif clique=="direita":
				pyautogui.click(button="right")
			else:
				pyautogui.click(button="left")
def iniciar():
	button2.pack()
	global count,clicksAtivado
	button.config(command=0)
	button2.config(command=parar)
	count = 10
	clicksAtivado = True
	thread = Thread(target=cliques)
	thread.start()
button = tkinter.Button(screen, text="iniciar", command=iniciar)
button.pack()
def parar():
	button2.pack_forget()
	global clicksAtivado, count
	clicksAtivado = False
	button.config(command=iniciar)
	button2.config(command=0)
	count = 10
	Text3.config(text=count)
button2 = tkinter.Button(screen, text="parar", command=parar)
Text2 = tkinter.Label(screen, text="A rodada de cliques começara em :")
Text2.pack()
Text3 = tkinter.Label(screen, text=10)
Text3.pack()
screen.mainloop()
