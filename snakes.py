import turtle
import time
import random

delay = 0.1
segments = []
# screen setup
wn = turtle.Screen()
wn.title("snake game by Arun")
wn.bgcolor("black")
wn.tracer(0)
wn.setup(600, 600)
# snake head
head = turtle.Turtle()
head.color("red")
head.penup()
head.shape("square")
head.goto(0, 0)
head.direction = "stop"
head.speed(0)



# moves :)
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    # segment


# functions
def go_up():
   if  head.direction != 'down':
        head.direction = 'up'


def go_down():
    if head.direction != 'up':
        head.direction = 'down'


def go_left():
    if head.direction != 'right':
        head.direction = 'left'


def go_right():
    if head.direction != 'left':
        head.direction = 'right'


# keyboard_input
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")
# food
food = turtle.Turtle()
food.color("blue")
food.penup()
food.shape("circle")
food.goto(0, 100)
#score
pen = turtle.Turtle()
pen.color("white")
pen.shape("square")
pen.goto(0,229)
pen.penup()
pen.hideturtle()
pen.write("Score: 0 Highscore: 0",align="center",font=("arial",10,"bold"))
score = 0
high_score = 0


food.speed(0)

while True:
    wn.update()
    if head.xcor()> 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290 :
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"
        score = 0
        for segment in segments:
            segment.goto(1000,1000)
        segments.clear()
        print("game over ")
    pen.clear()
    pen.write(f"Score: {score} Highscore: {high_score}", align="center", font=("arial", 10, "bold"))


    if head.distance(food) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)
        new_segment = turtle.Turtle()
        new_segment.color("blue")
        new_segment.penup()
        new_segment.shape("square")
        score = score + 1
        high_score = 0
        if score >= high_score:
            high_score = score

        segments.append(new_segment)
    # move segment to the first in reverse order
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)
    # moving segments 0 towards head
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)
    move()
    for segment in segments:
        if segment.distance(head) < 20 :
            head.goto(0,0)
            time.sleep(1)
            head.direction = "stop"
            score = 0

            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()




    time.sleep(delay)

wn.mainloop()