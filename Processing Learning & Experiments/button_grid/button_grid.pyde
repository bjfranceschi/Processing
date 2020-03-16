
def setup():
    size(600, 750, P3D)

global CLICK_DEPTH
CLICK_DEPTH = 0

def mouseClicked():
    CLICK_DEPTH = -50
    

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

    for i in range(0, 1000, 50):
        for x in range(0, 1000, 50):
            with pushMatrix():
                if i < (mouseY+25) and i > (mouseY-25) and x < (mouseX+25) and x > (mouseX-25):
                    if mousePressed == True:
                        translate(x, i, -25)
                    else:
                        translate(x, i, 0)
                else:
                    translate(x, i, 0)

                box(50, 50, 50)
            
                
