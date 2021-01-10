
from Icosahedron import Icosahedron

def setup():
    size(640, 800, P3D)

def draw():
    background_colors = color(10, 0, 60)
    background(background_colors)
    #lights()
    
    global Y
    Y = Y - .005
    
    with pushMatrix():
        translate(width/2, height/2.5, -500)
        
        # set perspective
        rotateX(radians(103))
        rotateZ(radians(-205))
        
        # continuously spin
        rotateZ(Y*2)
        
        # instantiate and spawn Icosahedron
        x = Icosahedron(ico_size=30,
                        rgb_fill=(background_colors),
                        rgb_stroke=180
                        )
        
        x.spawn()

    
    
    
    
