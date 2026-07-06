from turtle import Turtle , Screen
from designs import Midline, MakeCircle
from console import Console
import time

screen = Screen()
screen.setup(width = 1100,height = 700)
screen.bgcolor("yellow green")
screen.tracer(0)

midline = Midline()
centrecircle = MakeCircle()


right_console = Console()
right_console.make_console(525)

left_console = Console()
right_console.make_console(-525)

screen.listen()
screen.onkeypress(right_console.up,"Up")
screen.onkeypress(right_console.down,"Down")
# screen.onkeypress(left_console.up,"w")
# screen.onkeypress(left_console.down,"s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.01)

screen.exitonclick()