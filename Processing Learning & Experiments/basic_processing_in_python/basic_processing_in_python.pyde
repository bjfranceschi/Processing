
# as I understand it, the setup() function will run once to inialize things, and 
# the draw function will run continuously from top to bottom until the program is killed


 
import sys

def setup():
    size(650, 560) 
    stroke(255)
    frameRate(200)
  

def draw():
    background(0)
    
    # range args are start, stop, step
    for x in range(0, 1000, 50):
        ellipse(x, 250, 10, 10)

    # must instantiate global variables with "global" in draw function
    global Y
    
    Y = Y + 1
    
    if Y > width:
        Y = 0
        print("condition met")
        #sys.exit()
        
    ellipse(Y, 200, 50, 50)

 
