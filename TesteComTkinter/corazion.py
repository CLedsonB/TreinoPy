import turtle 
import time

pen = turtle.Turtle() 
def curve(): 
    for i in range(50): 
        pen.right(4) 
        pen.forward(4) 
def heart(): 
  
    
    pen.fillcolor('#4e6579')     
    pen.begin_fill()  
    pen.left(140) 
    pen.forward(113)     
    curve() 
    pen.left(120) 
    curve() 
    pen.forward(112) 
    pen.end_fill() 
def txt(): 
    pen.up() 
    pen.setpos(-64, 95) 
    pen.down() 
    pen.color('#111111') 
    
    pen.write(' None', font=( 
      "Verdana", 10, "bold")) 
  
  
heart() 
txt()
pen.ht()
time.sleep(7)