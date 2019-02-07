from turtle import mainloop
from random import randint
import time

from turtle import *
import sys


class Turtle_Race(Turtle):
    def __init__(self):
        Turtle.__init__(self)

    def _track(self):
        r_count = -200
        up = False
        self.speed(0)

        for i in range(0, 14):
            self.pu()
            self.goto(r_count, 200)
            self.setheading(0)
            self.pd()
            self.write(i)
            self.right(90)

            for x in range(0, 20):
                self.penup()
                self.forward(10)
                self.pendown()
                self.forward(10)
            if i == 0:
                self.write('Start', align='right')
            elif i == 13:
                self.write('Finish', align='left')
            r_count += 30

        self.up()
        self.goto((200 - r_count) / 2, 200 + 20)
        self.color('darkred')
        self.write("Placed your bet?", True, align='center', font=('Comic Sans Ms', 16, 'bold'))
        self.down()

    def _instructions(self):
        self.up()
        self.goto((200 - 220) / 2, -250)
        self.color('black')
        self.write("Press the 'space' key to begin", True, align='center',
                   font=('Comic Sans Ms', 14, ('normal', 'italic')))
        self.down()

    def turtle_obj(self, x, y, color):
        self.pu()
        self.goto(x, y)
        self.shape('turtle')
        self.color(color)
        self.pd()
        self.width(3)

def play():
    print("Game started")

    for i in range(-200, -70):
        for t in my_turtles:
            t.forward(randint(1, 5))

    t_pos = (tuple(my_turtles[0].pos())[0], tuple(my_turtles[1].pos())[0], tuple(my_turtles[2].pos())[0],
             tuple(my_turtles[3].pos())[0])

    t_count = len(my_turtles)

    for x in range(0, t_count):
        my_turtles[x].pencolor(0, 0, 0)
        if t_pos[x] > t_pos[(x + 1 - t_count)] and t_pos[x] > t_pos[(x + 1 + 1 - t_count)] and t_pos[x] > t_pos[
            (x + 1 + 1 + 1 - t_count)]:
            print("winner is ", str(x))
            my_turtles[x].write("\tFirst", align="center", font=('Comic Sans Ms', 10, 'normal'))
        elif t_pos[(x + 1 - t_count)] > t_pos[(x + 1 + 1 - t_count)] and t_pos[(x + 1 - t_count)] > t_pos[
            (x + 1 + 1 + 1 - t_count)]:
            print("Second is ", str(x))
            my_turtles[x].write("\tSecond", align="center", font=('Comic Sans Ms', 10, 'normal'))
        elif t_pos[(x + 1 + 1 - t_count)] > t_pos[
            (x + 1 + 1 + 1 - t_count)]:
            print("Third is ", str(x))
            my_turtles[x].write("\tThird", align="center", font=('Comic Sans Ms', 10, 'normal'))
        else:
            print("Looser is ", str(x))
            my_turtles[x].write("\tLast", align="center", font=('Comic Sans Ms', 10, 'normal'))


    onkey(restart, 'space')
    listen()

def restart():
    for x in range(0, len(my_turtles)):
        my_turtles[x].clear()

    my_turtles[0].turtle_obj(-200, 120, "red")
    my_turtles[1].turtle_obj(-200, 40, "yellow")
    my_turtles[2].turtle_obj(-200, -40, "green")
    my_turtles[3].turtle_obj(-200, -120, "blue")
    play()


def main():
    global my_turtles

    screen = Screen()
    screen.title("Turtle race")
    screen.bgcolor('white')

    raceTrack = Turtle_Race()
    raceTrack._track()

    turtle_1 = Turtle_Race()
    turtle_1.turtle_obj(-200, 120, "red")

    turtle_2 = Turtle_Race()
    turtle_2.turtle_obj(-200, 40, "yellow")

    turtle_3 = Turtle_Race()
    turtle_3.turtle_obj(-200, -40, "green")

    turtle_4 = Turtle_Race()
    turtle_4.turtle_obj(-200, -120, "blue")

    raceTrack._instructions()

    my_turtles = [turtle_1, turtle_2, turtle_3, turtle_4]
    onkey(play, 'space')
    listen()

    return 'EVENT LOOP'


if __name__ == '__main__':
    sys.stdout.write(main())
    mainloop()
