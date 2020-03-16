


class spinningCube:
    
    def __init__(self, cube_size, rotate_angle, fill_shade, rotation_speed_variable):
        self.cube_size = cube_size
        self.rotate_angle = rotate_angle
        self.fill_shade = fill_shade
        self.rotation_speed_variable = rotation_speed_variable
        
    def spawn(self):
        
        fill(self.fill_shade)
        
        if self.rotate_angle == 'X':
            rotateX(self.rotation_speed_variable)
            
        elif self.rotate_angle == 'Y':
            rotateY(self.rotation_speed_variable)
            
        elif self.rotate_angle == 'Z':
            rotateZ(self.rotation_speed_variable)
    
        box(self.cube_size)
