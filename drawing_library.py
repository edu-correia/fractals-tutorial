# Author: Eduardo Correia [https://github.com/edu-correia]

import turtle

# Screen Configuration
WIDTH, HEIGHT = 1600, 900
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.screensize(3 * WIDTH, 3 * HEIGHT)
screen.bgcolor('black')
screen.delay(0)

# "Pencil" configuration
pencil = turtle.Turtle()
pencil.pensize(4)
pencil.speed(1)
pencil.setpos(-WIDTH // 6, HEIGHT // 6)
pencil.color('green')

# Fractal specific configuration
step = 100
angle = 90

# Methods that you may find helpful:

# Draw line following pencil angle
pencil.forward(step)

# Rotates pencil angle to the left
pencil.left(angle)

# Rotates pencil angle to the right
pencil.right(angle)


# Necessary! Or the screen will close instantly.
screen.exitonclick()
