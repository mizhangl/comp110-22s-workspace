"""Happy Valentine's Day from Aperture Science! Creating a Companion Cube.
And always remember: the cake is a lie!"""

__author__ = "730490943"

from turtle import Turtle, colormode, done, tracer
colormode(255)


def main() -> None:
    """The entrypoint of my scene.
    Note: Functions called in 'main()' must be passed a Turtle expression because each function expects it. 
    The actual name of the object does not matter, as each function will rename it accordingly. Thus, 'my_turtle', created in 'main()',
    will be passed through to, say, 'heart()', whereupon it will rename the turtle, for its purposes, as 'turtle'.""" 
    my_turtle: Turtle = Turtle()
    tracer(0, 0)
    background(my_turtle, 350)
    center_circle(my_turtle, 0, -20)
    heart(my_turtle, 0, 0)
    pink_rectangle(my_turtle, 85, 70)
    gray_rectangle(my_turtle, 186, 105)
    quadrants(my_turtle, 80, 180)


def background(turtle: Turtle, width: int) -> None:
    """Draws the dark gray background that all other images are superimposed upon. Takes a given width of the square and draws
    the square accordingly."""
    i: int = 0
    turtle.penup()
    turtle.begin_fill()
    turtle.goto(-170, 240)
    turtle.color(170, 169, 169)
    turtle.pendown()
    while i < 4:
        turtle.forward(width)
        turtle.right(90)
        i += 1
    turtle.end_fill()


def center_circle(turtle: Turtle, x: float, y: float) -> None:
    """Draws the gray central circle behind the heart at coordinates 'x' 'y'."""
    turtle.penup()
    turtle.goto(x, y)
    turtle.color(241, 240, 240)
    turtle.setheading(0.0)
    turtle.begin_fill()
    turtle.pendown()
    turtle.circle(85)
    turtle.end_fill()


def heart(turtle: Turtle, x: float, y: float) -> None:   
    """Draws a heart! At given coordinates 'x' and 'y'."""
    turtle.penup()
    turtle.goto(x, y)
    turtle.begin_fill()
    turtle.pendown()
    turtle.color(255, 199, 199)
    turtle.left(130)
    turtle.forward(80)

    curve(turtle)  # Call of function curve to draw the curves of the heart.
    turtle.left(145)
    curve(turtle)
    turtle.goto(x, y)
    turtle.end_fill()
    

def curve(turtle: Turtle) -> None:
    """Draws the curve of a heart. Will be called in function 'heart'."""
    turtle.color(255, 199, 199)
    i: int = 0
    while i < 203:
        turtle.forward(0.5)
        turtle.right(1)
        i += 1


def pink_rectangle(turtle: Turtle, x: float, y: float) -> None:  
    """Draws the little pink rectangles that connect the center circle to the outer gray rectangles. 
    Located using coordinates 'x' and 'y'."""
    turtle.setheading(0.0)
    turtle.color(255, 166, 166)
    horizontal_pink_rectangle(turtle, 20, 50, 85, 70)  # Calls function horizontal_pink_rectangle to draw east most Rectangle.
    horizontal_pink_rectangle(turtle, 20, 50, -135, 70)  # Draws West most rectangle.
    vertical_pink_rectangle(turtle, 50, 20, 10, 150)  # Draws North most rectangle.
    vertical_pink_rectangle(turtle, 50, 20, 10, -70)  # Draws South most rectangle.


def horizontal_pink_rectangle(turtle: Turtle, length: int, width: int, x: float, y: float) -> None:
    """Function called into 'pink_rectangle' function for efficiency. Takes parameters length and width to create
    a horizontal rectangle. Also takes coordinates 'x' and 'y' for placement."""
    i: int = 0 
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    while i < 2:
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(length)
        turtle.right(90)
        i += 1
    turtle.end_fill()


def vertical_pink_rectangle(turtle: Turtle, length: int, width: int, x: float, y: float) -> None:
    """Function called into 'pink_rectangle' function for efficiency. Takes parameters 'length' and 'width' to create
    a vertical rectangle. Also takes parameters 'x' and 'y' for placement."""
    i: int = 0
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    while i < 2:
        turtle.left(90)
        turtle.forward(length)
        turtle.left(90)
        turtle.forward(width)
        i += 1
    turtle.end_fill()


def gray_rectangle(turtle: Turtle, x: float, y: float) -> None:
    """Function that creates the smaller gray rectangles that lie at each of the cardinal directions in the image.
    Takes the coordinates 'x' and 'y' as placement."""
    turtle.color(241, 240, 241)
    rectangle(turtle, 90, 50, 186, 106, 0.0)  # East most rectangle. 
    rectangle(turtle, 90, 50, -135, 105, 0.0)  # West most rectangle.
    rectangle(turtle, 90, 50, -45, 250, 90.0)  # North most rectangle.
    rectangle(turtle, 90, 50, -45, -70, 90)  # South most rectangle.


def rectangle(turtle: Turtle, length: int, width: int, x: float, y: float, angle: float) -> None:
    """Function that is called into 'gray_rectangles' for ease an efficiency. Takes parameters 'length' and 'width', and creates
    a rectangle corresponding to those dimensions. Also takes parameters 'x', 'y' for coordinates, and 'angle', which orients
    the rectangle."""
    i: int = 0 
    turtle.penup()
    turtle.goto(x, y)
    turtle.setheading(angle)
    turtle.pendown()
    turtle.begin_fill()
    while i < 2:
        turtle.right(90)
        turtle.forward(length)
        turtle.right(90)
        turtle.forward(width)
        i += 1
    turtle.end_fill()


def quadrants(turtle: Turtle, x: float, y: float) -> None:
    """Function that creates the four quadrants in each corner of the image. Takes one quadrant created from 'one_quadrant',
    rotates it to its correct orientation using 'angle', and then places it to where it belongs using coordinates 'x' and 'y'."""
    turtle.color(241, 240, 241)
    one_quadrant(turtle, 1.5, 80, 180, 10)  # Top right quadrant.
    one_quadrant(turtle, 1.5, 115, -15, 280)  # Bottom right quadrant.
    one_quadrant(turtle, 1.5, -117, 135, 100)  # Top left quadrant.
    one_quadrant(turtle, 1.5, -70, -60, -170)  # Bottom left quadrant.
    

def one_quadrant(turtle: Turtle, scale, x: float, y: float, angle: float) -> None:
    """Function that creates a quadrant and is called into 'quadrants'. Takes the parameter 'scale',
    which conveys by what magnitude the shape is sized up to. Takes one quadrant and rotates it to its correct
    orientation using 'angle', and then places it where it belongs using coordinates 'x' and 'y'."""
    turtle.penup()
    turtle.goto(x, y)
    turtle.setheading(angle)
    turtle.pendown()
    turtle.begin_fill()
    i: int = 0
    while i < 100:  # Creates the curve within the quadrant. 
        turtle.forward(0.5 * scale)
        turtle.right(1)
        i += 1
    turtle.left(90)  # The following set of code creates the outer straight lines that connect to the curve.
    turtle.forward(50 * scale)
    turtle.left(90)
    turtle.forward(84 * scale)
    turtle.left(90)
    turtle.forward(84 * scale)
    turtle.left(90)
    turtle.forward(50 * scale)
    turtle.end_fill()


if __name__ == "__main__":
    main()
done() 