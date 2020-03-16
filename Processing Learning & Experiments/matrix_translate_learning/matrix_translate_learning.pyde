
from spinningCube import SpinningCube

#matrix testing...

# pushMatrix() is a function that saves the current position of the coordinate system
# popMatrix() returns the coordinate system to previous state
# when making an independently moving shape, you could surround that code with pushMatrix() at
# the top, and popMatrix() at the bottom, or you could write it within a with pushMatrix(): clause.
# They do the same thing.
# translate() moves the coordinate system
#(so you want to move the coordinate system rather than moving shapes, for ex)

def setup():
    size(600, 750, P3D)

    
    
    
def draw():
    background(200)
    noFill()
    
    global Y
    Y = Y - .05
    print(Y)
    
    # move the grid to the corner of the square, then rotate. Otherwise, it'll
    # rotate at (0,0) of the canvas (top left corner)
    with pushMatrix():
        translate(200, 300, 200)
        box1 = SpinningCube(50, 'X', 100, Y)
        box1.spawn()


    with pushMatrix():    
        translate(300, 300, 200)
        box1 = SpinningCube(50, 'Y', 255, Y)
        box1.spawn()

    
    with pushMatrix():
        translate(400, 300, 200)
        noFill()
        rotateZ(Y)
        box(50, 50, 50)



    
    
