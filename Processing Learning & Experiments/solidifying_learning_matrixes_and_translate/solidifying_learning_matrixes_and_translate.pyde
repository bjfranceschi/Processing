
# see: https://www.processing.org/tutorials/transform2d/

# when you use translate, you move the grid that something is on. You never
# actually move an object - only the grid it is on. with the "with pushMatrix()"
# statement, it's like taking a screenshot of the grid as it is currently. Then
# we can use translate() to move it, etc, which it does only as long as it's within
# that "with" block. Then it goes back to the original state, not rotating nor
# being translated nor anything, at which point we can freeze it again with
# another "with pushMatrix()" statement etc.

def setup():
    size(600, 750, P3D)
    frameRate(100)
    
speed = int()
    
def draw():
    background(255)


    global speed
    speed = speed + .01

    with pushMatrix():
        translate(50, 50)
        rotate(speed)
        rect(0, 0, 50, 50)
        

    with pushMatrix():
        translate(200, 200)
        rect(0, 0, 50, 50)
    
    print(frameCount)
    
    
    
    
    
