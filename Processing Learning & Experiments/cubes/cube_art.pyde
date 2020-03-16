


def setup():
    size(600, 750, P3D)
    
    
def draw():
    background(100)

    noStroke()
    
    lights()

    global Y
    Y = Y + .04

    for i in range(0, -5000, -300):
        for x in range(-10, 10, 1):
            with pushMatrix():
                translate(width/8, x*100, i)
                rotateY(Y)
                box(50, 50, 50)

    for i in range(0, -5000, -300):
        for x in range(-10, 10, 1):
            with pushMatrix():
                translate(width-(width/8), x*100, i)
                rotateY(-Y)
                box(50, 50, 50)
