#!/usr/bin/python3
from tkinter import *
import graph
import pprint

BLOCK_DIM = 25
position_persoX = 0
position_persoY = 0
tailleX = 0
tailleY = 0
mCanvas = None
mGraph = None
matrix = [[]]
start = None
exit = None

fenetre = Tk()
fenetre.geometry("500x500")

with open('labyrinthe.txt') as f:
	array = []
	i = 0
	l = 0
	c = 0
	for line in f:
		if(i<4):
			if i ==0:
				position_persoX = int(line)
			if i == 1:
				position_persoY = int(line)
			if i == 2:
				tailleX = int(line)
			if i == 3:
				tailleY = int(line)
			i+=1
		else:
			if mCanvas == None: #Creating Canvas
				mCanvas = Canvas(fenetre,width=BLOCK_DIM*tailleX,height=BLOCK_DIM*tailleY,bg='black')
				matrix = [[0 for x in range(tailleX)] for y in range(tailleY)]
			for x in line.split():
				if not x:
					break
				if x=="-1": #Exit
					mCanvas.create_rectangle(c*BLOCK_DIM, l*BLOCK_DIM, (c+1)*BLOCK_DIM, (l+1)*BLOCK_DIM, fill="blue")
					exit = (l,c)
				if x=='1': #Wall
					mCanvas.create_rectangle(c*BLOCK_DIM, l*BLOCK_DIM, (c+1)*BLOCK_DIM, (l+1)*BLOCK_DIM, fill="grey")
					matrix[l][c] = 1
				if x=='0': #Path
					mCanvas.create_rectangle(c*BLOCK_DIM, l*BLOCK_DIM, (c+1)*BLOCK_DIM, (l+1)*BLOCK_DIM, fill="green")
				c+=1
			l+=1
			c = 0

#Add person
start = (position_persoX, position_persoY)
mCanvas.create_oval((start[1]*BLOCK_DIM), (start[0]*BLOCK_DIM), (start[1]*BLOCK_DIM)+(BLOCK_DIM), (start[0]*BLOCK_DIM)+(BLOCK_DIM), fill="red")
pprint.pprint(start)
pprint.pprint(matrix)
mGraph = graph.create_graph(matrix)
#pprint.pprint(mGraph)
mCanvas.pack()
#graph.a_star(mCanvas, mGraph, start, exit)
#graph.best_first_search(mCanvas, mGraph, start, exit)
graph.uniform_cost(mCanvas, mGraph, start, exit)
fenetre.mainloop()
