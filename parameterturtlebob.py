import turtle
bob = turtle.Turtle()

def square(bob):
    for i in range(4):
        bob.fd(100)
        bob.lt(90)
    print(bob)
    
square(bob)
turtle.mainloop()
