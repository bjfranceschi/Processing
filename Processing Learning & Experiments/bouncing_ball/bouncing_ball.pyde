
position = 0
speed = 0
gravity = .98


def setup():
    size(600, 750, P3D)
    noStroke()
    fill(200)


def draw():

    background(0)
    lights()


    global position
    global speed
    global gravity

    speed = speed + gravity
    position = position + (speed + gravity)
    

    if position > height-50:
        speed = speed * -0.7
        position = height-50

    if mouseX < (width / 2) + 20 and mouseX > (width / 2) - 20 and mouseY < (position + 20) and mouseY > (position - 20):
        speed = abs(speed) * -1.1

    with pushMatrix():
        noStroke()
        fill(200)
        translate(width / 2, position, 0)
        sphere(40)

    print(speed)
