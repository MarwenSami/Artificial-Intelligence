#!/usr/bin/python3
from tkinter import *
import os
import graph
import pprint
from subprocess import call

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
fenetre.geometry("500x600")
filename = input('Enter le chemin du fichier de labyrinthe\n')
with open(filename) as f:
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
def callback_a():
    graph.a_star(mCanvas, mGraph, start, exit)
b1 = Button(fenetre, text="A*", command=callback_a)
def callback_bfs():
    graph.best_first_search(mCanvas, mGraph, start, exit)
b2 = Button(fenetre, text="Best First Search", command=callback_bfs)
def callback_uc():
    graph.uniform_cost(mCanvas, mGraph, start, exit)
b3 = Button(fenetre, text="Uniform Cost", command=callback_uc)
def init():
    with open(filename) as f:
        array = []
        i = 0
        l = 0
        c = 0
        for line in f:
                if(i<4):
                        i+=1
                else:
                        for x in line.split():
                                if not x:
                                        break
                                if x=="-1": #Exit
                                        mCanvas.create_rectangle(c*BLOCK_DIM, l*BLOCK_DIM, (c+1)*BLOCK_DIM, (l+1)*BLOCK_DIM, fill="blue")
                                if x=='1': #Wall
                                        mCanvas.create_rectangle(c*BLOCK_DIM, l*BLOCK_DIM, (c+1)*BLOCK_DIM, (l+1)*BLOCK_DIM, fill="grey")
                                if x=='0': #Path
                                        mCanvas.create_rectangle(c*BLOCK_DIM, l*BLOCK_DIM, (c+1)*BLOCK_DIM, (l+1)*BLOCK_DIM, fill="green")
                                c+=1
                        l+=1
                        c = 0

    mCanvas.create_oval((start[1]*BLOCK_DIM), (start[0]*BLOCK_DIM), (start[1]*BLOCK_DIM)+(BLOCK_DIM), (start[0]*BLOCK_DIM)+(BLOCK_DIM), fill="red")
b4 = Button(fenetre, text="Reset", command=init)
b1.pack()
b2.pack()
b3.pack()
b4.pack()
fenetre.mainloop()
