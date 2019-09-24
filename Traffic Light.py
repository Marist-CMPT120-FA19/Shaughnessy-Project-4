from graphics import *

def main ():
    win= GraphWin('Stoplight')

    rectangle= Rectangle(Point(30,30), Point(90, 150))
    rectangle.setOutline("black")
    rectangle.setFill("gray")
    rectangle.draw(win)

    redlight= Circle(Point(60,55), 15)
    redlight.setOutline("black")
    redlight.setFill("red")
    redlight.draw(win)

    yellowlight= Circle(Point(60,90), 15)
    yellowlight.setOutline("black")
    yellowlight.setFill("yellow")
    yellowlight.draw(win)

    greenlight= Circle(Point(60,125), 15)
    greenlight.setOutline("black")
    greenlight.setFill("green")
    greenlight.draw(win)
                
main()
