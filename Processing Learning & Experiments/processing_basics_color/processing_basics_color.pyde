
r = 0
g = 0
b = 0


def setup():
    size(400, 500)
    background(250)
    
    
def draw():
    background(255)
    fill(r, g, b)
    stroke(b, r, g)
    ellipse(mouseX, mouseY, 100, 100)

        
def mouseClicked(): 
    global r, g, b
    r = random(250)
    g = random(250)
    b = random(250)
