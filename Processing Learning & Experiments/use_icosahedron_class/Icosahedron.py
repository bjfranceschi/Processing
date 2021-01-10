
class Icosahedron():
    """Class to generate an icosahedron.
    Attributes:
        ico_size : int
            size of icosahedron
        rgb_fill : tuple or int
            (r, g, b) color values, or color() object, of icosahedron fill
        rgb_stroke : tuple or int
            (r, g, b) color values, or color() object, of icosahedron stroke
            
    Methods:
        spawn():
            Generates icosahedron.
    """
    def __init__(self, ico_size, rgb_fill=None, rgb_stroke=None):
        self.ico_size = ico_size
        self.rgb_fill = rgb_fill
        self.rgb_stroke = rgb_stroke
        
    def spawn(self):
        
        ico_size = self.ico_size
        rgb_fill = self.rgb_fill
        rgb_stroke = self.rgb_stroke
        
        if rgb_fill:
            if isinstance(rgb_fill, int):
                fill(rgb_fill)
            else:
                fill(rgb_fill[0], rgb_fill[1], rgb_fill[2])
        else:
            noFill()
        
        if rgb_stroke:
            if isinstance(rgb_stroke, int):
                stroke(rgb_stroke)
            else:
                stroke(rgb_stroke[0], rgb_stroke[1], rgb_stroke[2])
            
        for i in range(0, 5):
            # triangle for top pentagon
            with beginShape():
                vertex(0, 0, 1.599*ico_size)
                vertex(-1.599*ico_size, -2.201*ico_size, 0)
                vertex(1.599*ico_size, -2.201*ico_size, 0)
                vertex(0, 0, 1.599*ico_size)
        
            # triangle for middle, point-down triangles
            with beginShape():
                vertex(0, -2.701*ico_size, -2.701*ico_size)
                vertex(-1.599*ico_size, -2.201*ico_size, 0)
                vertex(1.599*ico_size, -2.201*ico_size, 0)
                vertex(0, -2.701*ico_size, -2.701*ico_size)
                
            # rotate to create adjacent triangles
            rotateZ(radians(72))
        
        # flip canvas on its head
        rotateY(radians(180))
    
        # offset so sets of triangles interlock
        rotateZ(radians(36))
        
        # shift down 2.701*input, which is the z-amount taken from above middle triangles
        translate(0, 0, 2.701*ico_size)
        
        for i in range(0, 5):
            
            with beginShape():
                vertex(0, 0, 1.599*ico_size)
                vertex(-1.599*ico_size, -2.201*ico_size, 0)
                vertex(1.599*ico_size, -2.201*ico_size, 0)
                vertex(0, 0, 1.599*ico_size)
        
    
            with beginShape():
                vertex(0, -2.701*ico_size, -2.701*ico_size)
                vertex(-1.599*ico_size, -2.201*ico_size, 0)
                vertex(1.599*ico_size, -2.201*ico_size, 0)
                vertex(0, -2.701*ico_size, -2.701*ico_size)
                
            # rotate to create adjacent triangles
            rotateZ(radians(72))
