# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 10:40:28 2019

@author: shayan
"""
import turtle as trtl
import tkinter as tk
from tkinter import ttk
import numpy
import random
import time



class App():
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry('580x580')
        self.window.configure(bg = 'beige')
        self.window.title('SnakeGame')
        self.buttonStart = ttk.Button(self.window, text='start', command= self.Game)
        self.buttonStart.place(x= 25, y= 200 , width= 530 , height= 250)
        self.window.mainloop()
        
        
    def Game(self):
        self.window = tk.Tk()     
        self.window.geometry('580x580')
        self.window.configure(bg = 'beige')
        self.window.title('SnakeGame')
        self.buttonGameEasy = ttk.Button(self.window, text='Easy', command= self.GameEasy)
        self.buttonGameEasy.place(x= 30, y= 100 , width= 530 , height= 150)
        self.window.mainloop()
    
    def GameEasy(self):
        self.ix = -320
        self.fx = 320
        self.inc = 21
        self.iy = -320
        self.fy = 320
        self.x =numpy.arange(self.ix,self.fx,self.inc)
        self.y =numpy.arange(self.iy,self.fy,self.inc)
        self.xgrid,self.ygrid = numpy.meshgrid(self.x,self.y) 
        gridshape = self.xgrid.shape
        self.Ny = gridshape[0]
        self.Nx = gridshape[1]
        self.score = 0
        self.i = 1
        self.bobs = []
        self.delay = 0.1
        
        self.scr = trtl.Screen()
        self.scr.update()
        
        self.bob = trtl.Turtle() 
        self.bob.shape("square") 
        self.bob.color('ghost white')
        
        self.xpos = self.xgrid[int(round(self.Ny/2,0)),int(round(self.Nx/2,0))]
        self.ypos = self.ygrid[int(round(self.Ny/2,0)),int(round(self.Nx/2,0))]
        self.bob.penup()
        self.bob.goto(self.xpos,self.ypos)
        self.bob.speed(0)
        
        self.scr.setup(width = 660, height = 660)
        self.scr.bgcolor("navy")
        trtl.listen()
        
        
        

        self.choose()
        self.run=True
        while self.run:
            self.movement()
            self.die()
            self.eat()
            time.sleep(self.delay)
        self.Gameover()
        


    
    def movement(self):
        newpos = self.bob.pos()
        trtl.onkeypress(self.turnleft, key="Left") 
        trtl.onkeypress(self.turnright, key="Right")
        trtl.onkeypress(self.turnup, key="Up")
        trtl.onkeypress(self.turndown, key="Down")
        self.bob.forward(21)
        
        
        I = len(self.bobs)
        for i in range (0,I):
            oldpos = self.bobs[i].position()
            self.bobs[i].goto(newpos)
            newpos = oldpos

        
            
    def turnleft(self): 
        if self.bob.heading() != 0:
            currentSpeed = self.bob.speed()
            self.bob.speed(10)
            self.bob.seth(180) 
            self.bob.speed(currentSpeed)
            
    def turnright(self):
        if self.bob.heading() != 180:
            currentSpeed = self.bob.speed()
            self.bob.speed(10)
            self.bob.seth(0) 
            self.bob.speed(currentSpeed)
            
    def turnup(self):
        if self.bob.heading() != 270:
            currentSpeed = self.bob.speed()
            self.bob.speed(10)
            self.bob.seth(90)
            self.bob.speed(currentSpeed)
            
    def turndown(self):
        if self.bob.heading() != 90:
            currentSpeed = self.bob.speed()
            self.bob.speed(10)
            self.bob.seth(270)
            self.bob.speed(currentSpeed)
            
            
    def seeds(self):
        self.beeb = trtl.Turtle() 
        self.beeb.penup()
        self.beeb.shape("square") 
        self.beeb.color('red')
        Ix = random.randint(0,self.Nx-1)
        Iy = random.randint(0,self.Ny-1)
        self.beeb.goto(self.xgrid[Iy,Ix],self.ygrid[Iy,Ix])
        
        
    def seeds2(self):
        self.boby = trtl.Turtle()
        self.boby.penup()
        self.boby.shape("square")
        self.boby.color("yellow")
        Ix = random.randint(0,self.Nx-1)
        Iy = random.randint(0,self.Ny-1)
        self.boby.goto(self.xgrid[Iy,Ix],self.ygrid[Iy,Ix])
        
    
    def choose(self):
        SeedsList = ["seed1","seed2"]
        self.which_seeds = random.choice(SeedsList)
        if self.which_seeds=="seed1" :
            self.seeds()
        elif self.which_seeds=="seed2" :
            self.seeds2()
        
        
        
        
    def update(self):
        if self.which_seeds=="seed1" :
            Ix = random.randint(0,self.Nx-1)
            Iy = random.randint(0,self.Ny-1)      
            
            self.beeb.penup()
            self.beeb.goto(self.xgrid[Iy,Ix],self.ygrid[Iy,Ix])
            self.beeb.speed(0)
            self.beeb.showturtle()  
            
            self.score+=5
            
        elif self.which_seeds=="seed2" :
            Ix = random.randint(0,self.Nx-1)
            Iy = random.randint(0,self.Ny-1) 
            
            self.boby.penup()
            self.boby.goto(self.xgrid[Iy,Ix],self.ygrid[Iy,Ix])
            self.boby.speed(0)
            self.boby.showturtle()   
            
            self.score+=10
   
        
    def eat(self):
        if self.which_seeds=="seed1" and self.bob.distance(self.beeb) < 0.1:
            self.beeb.hideturtle()
            self.update()
            self.i+=1
            self.bobs.append(self.bob.clone())
            self.delay = self.delay - 0.002
            
            
        elif self.which_seeds=="seed2" and self.bob.distance(self.boby) < 0.1:
            self.boby.hideturtle()
            self.update()
            self.i+=2
            self.bobs.append(self.bob.clone())
            self.delay = self.delay - 0.002


    def Gameover(self):
        if self.which_seeds=="seed1" :
            self.beeb.hideturtle()
        elif self.which_seeds=="seed" :
            self.boby.hideturtle()
        self.bob.reset()
        self.bob.hideturtle()
        self.bob.pencolor("white")
        self.bob.write("GAME OVER AND YOUR SCORE IS "+ str(self.score) + " \n  CLICK ANY WHERE TO RESTART",align ="center", font=("Arial",12,"bold"))
        self.scr.exitonclick()


            
    def die(self):
        I = len(self.bobs)
        currentPosition = self.bob.pos()
        if currentPosition[0]>325 or currentPosition[0]<-325 or  currentPosition[1]>325 or currentPosition[1]<-325:
            self.run = False
        for i in range (I):
            if currentPosition == self.bobs[i].pos():
                self.run = False

        
me = App()



    
  
    