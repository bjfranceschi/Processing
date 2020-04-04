
from random import choice

class Cubes:
    def __init__(self, num_cubes, w, h):
        self.num_cubes = num_cubes
        self.rotate_1 = [choice([rotateX, rotateY, rotateZ]) for x in range(num_cubes)]
        self.rotate_2 = [choice([rotateX, rotateY, rotateZ]) for x in range(num_cubes)]
        self.x_pos = [random(-w*3, w*4) for x in range(num_cubes)]
        self.y_pos = [random(-h*3, h*4) for y in range(num_cubes)]


    def _setup_cube(self, spin_speed, move_speed, fft):

        for x_pos, y_pos, rotate_1, rotate_2 in zip(self.x_pos, self.y_pos, self.rotate_1, self.rotate_2):
            
            with pushMatrix():
                translate(x_pos, y_pos, -5000+move_speed)
                
                rotate_1(spin_speed)
                rotate_2(spin_speed)
                
                box_size = 100 + \
                ((fft.getBand(1) + fft.getBand(2) + fft.getBand(3)) / 3) * 6
                box(box_size, box_size, box_size)
    

    def spawn(self, spin_speed, move_speed, fft):
        
        num = self.num_cubes
        
        for i in range(num):
            self._setup_cube(spin_speed, move_speed, fft)
