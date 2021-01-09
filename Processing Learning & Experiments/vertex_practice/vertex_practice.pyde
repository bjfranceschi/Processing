"""Goal here is to learn vertex() function by creating an icosahedron made up of
equilateral triangles.

Beginning with the top "pentagon", a regular pentagon is made up of 5 triangles
with angles of 54, 54, and 72 degrees, which translates to the following coordinates
(with origin at top (72-degree) vertex): A: (0, 0), B: (-1.599, -2.201), C: (1.599, -2.201),
or any magnitude of these coefficients. Then need to extrude the middle meeting point
of the triangles, which is where all the 72-degree angles meet (72*5=360), and by
extruding this point up the Z-axis, the angles become slightly more acute - hopefully
down to 54-degrees so that they're equilateral. Ended up eyeballing this part.

The following code creates a single tringle for the top pentagon, "attached" to
a single middle triangle, then rotates the canvas 36 degrees, and repeats this 5 times.

It then flips the canvas 180 degrees on its head, rotates it by 36 degrees again so
that the following triangles interlock with the previous ones, and does the
above triangle creation again.
"""


def setup():
    size(650, 700, P3D)
    

def draw():
    background(100)
    
    # starting from grid where 0,0 is center of window
    translate(width/2, height/2.5, -1200)

    # set perspective
    rotateX(radians(103))
    rotateZ(radians(-205))
    
    # continuously rotate
    global Y
    Y = Y - .005
    rotateZ(Y)
    
    # fill first set of triangles as yellow
    fill(200, 200, 0) # yellow
    
    for i in range(0, 5):
        # triangle for top pentagon
        stroke(250, 10, 10) # red stroke, to identify top
        with beginShape():
            vertex(0, 0, 159.9)
            vertex(-159.9, -220.1, 0)
            vertex(159.9, -220.1, 0)
            vertex(0, 0, 159.9)
    
        # triangle for middle, point-down triangles
        stroke(0, 0, 0)
        with beginShape():
            vertex(0, -270.1, -270.1)
            vertex(-159.9, -220.1, 0)
            vertex(159.9, -220.1, 0)
            vertex(0, -270.1, -270.1)
            
        # rotate to create adjacent triangles
        rotateZ(radians(72))
    
    
    # flip canvas on its head
    rotateY(radians(180))

    # offset so sets of triangles interlock
    rotateZ(radians(36))
    
    # now shift down 270.1, which is the z-amount taken from above middle triangles
    translate(0, 0, 270.1)

    # fill second set of triangles as blue to help visualize what we're doing
    fill(0, 200, 200)
    
    for i in range(0, 5):
        
        stroke(250, 10, 10) # red stroke, to identify "top", now bottom b/c rotated 180 degs
        with beginShape():
            vertex(0, 0, 159.9)
            vertex(-159.9, -220.1, 0)
            vertex(159.9, -220.1, 0)
            vertex(0, 0, 159.9)
    
        stroke(0, 0, 0)
        with beginShape():
            vertex(0, -270.1, -270.1)
            vertex(-159.9, -220.1, 0)
            vertex(159.9, -220.1, 0)
            vertex(0, -270.1, -270.1)
            
        # rotate to create adjacent triangles
        rotateZ(radians(72))
        
        
        
    
    
    
    
