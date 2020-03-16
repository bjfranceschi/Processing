
#box() obj is extruded rect()

def setup():
    size(600, 750, P3D)
    #background(0)


def draw():
    background(100)
    noStroke()
    
    lights()
    
    global Y
    Y = Y - .05


    translate(width/2, height/2)
    print(Y*(-100))
    rotateY(Y)
    rotateX(50)
    
    translate(0, 0, 0)
    box(200, 200, 200)
    
    translate(0, 1000, -5000)
    box(200, 200, 200)
