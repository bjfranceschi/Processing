
import random as rand

class Cubes:
    def __init__(self, num_cubes, w, h):
        self.num_cubes = num_cubes
        self.rotate_1 = [rand.choice([rotateX, rotateY, rotateZ]) for x in range(num_cubes)]
        self.rotate_2 = [rand.choice([rotateX, rotateY, rotateZ]) for x in range(num_cubes)]
        self.x_pos = [random(-w, w*2) for x in range(num_cubes)]
        self.y_pos = [random(-h, h*2) for y in range(num_cubes)]
        self.z_pos = [random(-10000, -100) for z in range(num_cubes)]


    def _setup_cube(self, spin_speed, move_speed, fft):
        cubenum = 0
        for x_pos, y_pos, z_pos, rotate_1, rotate_2 in zip(self.x_pos, self.y_pos, self.z_pos, self.rotate_1, self.rotate_2):
            with pushMatrix():
                
                translate(x_pos, y_pos, z_pos + move_speed)
                
                rotate_1(spin_speed)
                rotate_2(spin_speed)
                
                box_size = 100 + \
                ((fft.getBand(1) + fft.getBand(2) + fft.getBand(3)) / 3) * 6
                box(box_size, box_size, box_size)
                
        return z_pos

    def spawn(self, spin_speed, move_speed, fft):
        
        num = self.num_cubes
        
        for i in range(num):
            self._setup_cube(spin_speed, move_speed, fft)
