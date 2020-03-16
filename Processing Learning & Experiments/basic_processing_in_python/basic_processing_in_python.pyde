
# as I understand it, the setup() function will run once to inialize things, and 
# the draw function will run continuously from top to bottom until the program is killed

def setup():
    size(650, 560) 
    stroke(255)
    frameRate(200)

# instantiate variable outside draw, then declare it as global when referencing
speed = int()

def draw():
    background(0)
    
    # range args are start, stop, step
    for x in range(0, 1000, 50):
        ellipse(x, 250, 10, 10)

    # reference as global
    global speed
    
    speed = speed + 1
    
    if speed > width:
        speed = 0
        print("condition met")
        
    ellipse(speed, 200, 50, 50)

 
