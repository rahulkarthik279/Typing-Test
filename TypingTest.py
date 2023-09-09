import tkinter as t
import random as r
import time
top = t.Tk()
top.title("Typing Test")
top.geometry("1200x500")
top["bg"] = "black"
tup = ["Good morning to everybody present in this room","Friends are great and help us grow in life","An apple a day always keeps the doctor away"]
rand = int(r.random()*len(tup))
word = ""
realword = tup[rand]
numAccurate= 0
numTyped = 0
textin = t.StringVar()
label3 = t.Label(text = "")
now = time.strftime("0")
label3.pack()
def update_clock():
	global label3
	global now
	def incrementTime():
		global label3
		global now
		now = str(int(now)+1)
		label3.configure(text=now)
	incrementTime()
	top.after(1000, update_clock)
update_clock()
def clear_label(label):
	label["text"] = ""
num = 0
def pressletter(word2,event):
	global numAccurate
	global numTyped
	global num
	word = word2
	textin.set(word)
	reallabel = t.Label(text = textin)
	tup = ["blue","green","red"]
	tup2 = ["pink","orange","light blue"]
	if num % 2 == 0:
		label2 = t.Label(top,text = "Go back and type it correctly",fg = tup[int(r.random()*len(tup))],bg = "black",font = ("Arial",40,"bold"))
	else:
		label2 = t.Label(top,text = "Go back and type it correctly",fg = tup2[int(r.random()*len(tup2))],bg = "black",font = ("Arial",40,"bold"))
	if word != realword[0:len(word)]:
		entry = t.Entry(top,bg = "red",fg = "white",width = 100,textvar = textin)
		entry.place(x = 300,y=200)
		label2.place(x = 250,y = 300)
		num+=1
		numTyped+=1
	else:
		entry = t.Entry(top,bg = "green",fg = "white",width = 100,textvar = textin)
		entry.place(x = 300,y=200)
		label2 = t.Label(top,text = "Go back and type it correctly",bg = "black",fg = "black",font = ("Arial",40,"bold"))
		label2.place(x = 250, y = 300)
		numAccurate+=1
		numTyped+=1
def numWords():
	num = 0
	for char in realword:
		if char == " ":
			num+=1
	return num+1
def enterkey(event):
	global numAccurate
	global numTyped
	global label3
	label2 = t.Label(top,text = "Accuracy: " + str(round((float(numAccurate)/float(numTyped))*100)) + "%")
	label4 = t.Label(top,text = "WPM: " + str(round((numWords()/int(now))*60)))
	label5 = t.Label(top,text = "Number of seconds taken: " + str(int(now)))
	label3.configure(text = "",bg = "black")
	label2.pack()
	label4.pack()
	label5.pack()
top.bind("<Return>",lambda a: enterkey(a))	
top.bind("<Key>",lambda a: pressletter(entry.get(),a))
label = t.Label(top,text = "Typing Test",font = ("Arial",20,"bold"),fg = "blue",bg = "black")
sentence = t.Label(top,text = realword,font = ("Arial",15,"bold"),fg = "white",bg = "black").place(x=400,y=125)
entry = t.Entry(top,bg = "green",fg = "white",width = 100,textvar = textin)
entry.place(x = 300,y=200)
label.pack()
top.mainloop()