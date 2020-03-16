
from spinning_cube import spinningCube

# matrix testing...

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
    fill(200)

    global Y
    Y = Y - .04
    print(Y)

    lights()

    # move the grid to the corner of the square, then rotate. Otherwise, it'll
    # rotate at (0,0) of the canvas (top left corner)
    '''
    with pushMatrix():
        translate(200, 300, 200)
        box1 = spinningCube(50, 'X', 100, Y)
        box1.spawn()


    with pushMatrix():    
        translate(300, 300, 200)
        box1 = spinningCube(50, 'Y', 255, Y)
        box1.spawn()
    '''

    for i in range(0, 1000, 100):
        for x in range(0, 1000, 100):
            with pushMatrix():
                if i < (mouseY+50) and i > (mouseY-50) and x < (mouseX+50) and x > (mouseX-50):
                    if mousePressed == True:
                        translate(x, i, -120)
                    else:
                        translate(x, i, 0)
                else:
                    translate(x, i, 0)
                
                rotateX(Y)
                rotateY(Y)
                box(50, 50, 50)
            
                
