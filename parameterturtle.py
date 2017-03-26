import turtle
new_square = turtle.Turtle()

def square(t):
    for i in range(4):
        t.fd(100)
        t.lt(90)
    print(t)
    
square(new_square)
turtle.mainloop()
