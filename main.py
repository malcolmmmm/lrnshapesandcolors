from turtle import * 
import random
speed(0)
S = Screen()
S.bgcolor("#7E91A6")
def triangle():
  for i in range(3):
    forward(100)
    left(120)
def square():
  for i in range(4):
    forward(100)
    left(90)
def circle1():
  circle(50)
def pentagon():
  for i in range(5):
    forward(100)
    left(72)
def hexagon():
  for i in range(6):
    forward(100)
    left(60)
def rectangle():
  for i in range(2):
    forward(100)
    left(90)
    forward(50)
    left(90)
def semicircle():
  circle(50, 180)
def octagon():
  for i in range(8):
    forward(50)
    left(45)
def cross():
    for i in range(4):
      forward(50)
      left(90)
      forward(100)
      right(90)
      forward(100)
      left(90)
def diamond():
  left(90)
  right(36)
  forward(100)
  left(72)
  forward(100)
  left(144)
  right(36)
  forward(100)
  left(72)
  forward(100)

def star():
  for i in range(5):
    forward(100)
    left(72)
    forward(100)
    right(144)
  
def endgame(num):
  penup()
  if num == 1:
    setposition(-100,0)
  if num == 2:
    setposition(-250,0)
  if num == 3:
    setposition(-350,0)
  pendown()
  for i in range(num):
    color('yellow')
    begin_fill()
    star()
    end_fill()
    penup()
    forward(250)
    pendown()



while True:
  cm = input("""Welcome!!!!
   This games purpose is to help you learn shapes and colors.
   Everything must be typed in lowercase.
   Do you wish to continue(y/n)?""") 
  if cm == "y":
    wejdwodjwod = 5
  else:
    break
  
  score = 0
  for i in range(10):
    while True:
      l = ["yellow", "blue", "red", "green", "purple", "pink", "black", "white", "orange"]
      shape = random.randint(1, 11)  
      a = random.choice(l)
      color(a)
      begin_fill()
      if shape == 1:
        triangle()
      elif shape == 2:
        square()
      elif shape == 3:
        circle1()
      elif shape == 4:
        pentagon()
      elif shape == 5:
        hexagon()
      elif shape == 6:
        rectangle()
      elif shape == 7:
        semicircle()
      elif shape == 8:
        octagon()
      elif shape == 9:
        cross()
      elif shape == 10:
        diamond()
      elif shape == 11:
        star()
      else:
        continue
      end_fill()
      cmd = input("what shape is it? ")
      cmd2 = input("What is the color of the shape? ")
      if cmd2 == a:
        if cmd == "triangle" and shape == 1:
          score = score + 1
          print("You got that right!")
        elif cmd == "square" and shape == 2:
          score = score + 1
          print("You got that right!")
        elif cmd == "circle" and shape == 3:
          score = score + 1
          print("You got that right!")
        elif cmd == "pentagon" and shape == 4:
          score = score + 1
          print("You got that right!")
        elif cmd == "hexagon" and shape == 5:
          score = score + 1
          print("You got that right!")
        elif cmd == "rectangle" and shape == 6:
          score = score + 1
          print("You got that right!")
        elif cmd == "semicircle" and shape == 7:
          score = score + 1
          print("You got that right!")
        elif cmd == "octagon" and shape == 8:
          score = score + 1
          print("You got that right!")
        elif cmd == "cross" and shape == 9:
          score = score + 1
          print("You got that right!")
        elif cmd == "diamond" and shape == 10:
          score = score + 1
          print("You got that right!")
        elif cmd == "star" and shape == 11:
          score = score + 1
          print("You got that right!")
      else:
        if shape == 1:
          print("I'm sorry the correct answer was: " + a + " triangle")
        elif shape == 2:
          print("I'm sorry the correct answer was: " + a + " square") 
        elif shape == 3:
          print("I'm sorry the correct answer was: " + a + " circle")
        elif shape == 4:
          print("I'm sorry the correct answer was: " + a + " pentagon")
        elif shape == 5:
          print("I'm sorry the correct answer was: " + a + " hexagon")
        elif shape == 6:
          print("I'm sorry the correct answer was: " + a + " rectangle")
        elif shape == 7:
          print("I'm sorry the correct answer was: " + a + " semicircle")
        elif shape == 8:
          print("I'm sorry the correct answer was: " + a + " octagon")
        elif shape == 9:
          print("I'm sorry the correct answer was: " + a + " cross")
        elif shape == 10:
          print("I'm sorry the correct answer was: " + a + " diamond")
        elif shape == 11:
          print("I'm sorry the correct answer was: " + a + " star")
      clear()
      reset()
      break
    if (i + 1) % 3 == 0:
      i = i + 1
      print("You got " + str(score) + " correct out of the last " + str(i) + " questions. ")
      i = i - 1
      
  print 'you got', score, 'out of 10, Correct!!! good job!'
  if score <= 3:
    num = 1  
  elif 4 <= score  and score <= 7:
    num = 2
  else:
    num = 3
  endgame(num)
  break 

    

  

  



