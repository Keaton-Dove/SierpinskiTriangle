# Sierpinski Triangle renderer
# Keaton Dove 4/13/22

from graphics import *
from random import *

AMOUNT_POINTS = 10000
USE_DEFAULT_TRIANGLE = False
DEFAULT_TRIANGLE = (500, 100, 200, 600, 800, 600)

def main():
    graphWin = GraphWin("Sierpinski", 1000, 700)
    trianglePoints = []

    # Initializing the base triangle using the DEFAULT_TRIANGLE coordinates provided or random coords
    if USE_DEFAULT_TRIANGLE:
        for i in range(0, len(DEFAULT_TRIANGLE), 2):
            p = Point(DEFAULT_TRIANGLE[i], DEFAULT_TRIANGLE[i + 1])
            trianglePoints.append(p)
            p.draw(graphWin)
    else:
        for i in range(3):
            p = Point(randint(0, 1000), randint(0, 700))
            trianglePoints.append(p)
            p.draw(graphWin)

    # Get starting point from user mouse click
    currentPoint = graphWin.getMouse()
    currentPoint.draw(graphWin)

    # Initialize pointCounter label
    pointCounter = Text(Point(50, 50), '0')
    pointCounter.draw(graphWin)

    # Drawing all of the points
    for i in range(AMOUNT_POINTS + 1):
        # Choosing a random point from the triangle to traverse halfway towards
        randPoint = trianglePoints[randint(0, 2)]
        currentPoint = Point((currentPoint.x + randPoint.x) / 2, (currentPoint.y + randPoint.y) / 2)
        currentPoint.draw(graphWin)

        # Updating label that counts points
        pointCounter.setText(i)

    # Wait for user to close window with Q key
    while True:
        key = graphWin.getKey()
        if key == 'q':
            graphWin.close()
            return 0

if __name__ == '__main__':
    main()

