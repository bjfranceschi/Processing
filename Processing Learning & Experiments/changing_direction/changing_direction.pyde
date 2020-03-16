


def setup():
    size(600, 750, P3D)

    noStroke()
    
speed = 50

# this should really be a boolean since we just need it to be negative or positive,
# but it has to be an int since we're multiplying it with speed to change position
direction = 1
position = 0
    
    
def draw():
    
    background(0)
    lights()
    
    global position
    global direction
    global speed

    position = position + (speed * direction)
    print(position)
    
    with pushMatrix():
        translate(250, position, 0)
        sphere(50)
        
        if position >= height:
            direction = direction * -1
        
        if position < 0:
            direction = direction * -1
