
'''
#minim reference: http://code.compartmental.net/minim/
'''

# import minim library
add_library('minim')

from cube import Cubes

spin_speed = int()
move_speed = int()



def setup():
    fullScreen(P3D)
    print(log(10))
    #size(1280, 630, P3D)

    path = '/Users/Bfranceschi/Documents/Processing/song_library'
    song = 'super_sprode.mp3'
    #song = 'frequency_test.mp3'

    # instantiate minim object
    minim = Minim(this)

    # make global variable to hold loaded mp3
    global player
    player = minim.loadFile(path + '/' + song)

    # instantiate FFT object - Fast Fourier Transform is an algorithm that changes
    # the domain of a signal from time to frequency - this is useful for
    # deconstructing a signal made up of multiple pure frequencies
    global fft
    fft = FFT(player.bufferSize(), player.sampleRate())

    # specSize() is the number of frequency bands in the spectrum produced
    # by this Fast Fourier Transform of the audio buffer
    print("Number of frequency bands: ", fft.specSize())
    
    # instantiate cubes
    global cubes
    cubes = Cubes(50, width, height)
    



def draw():
    background(0)
    stroke(250)
    noFill()
    

    # for full spectrum, make this equal to fft.specsize()
    spectrum = fft.specSize()

    # do the forward transform
    fft.forward(player.mix)

    global spin_speed
    spin_speed += .01
    
    global move_speed
    move_speed += 5
    
    global cubes
    cubes.spawn(spin_speed, move_speed, fft)


def keyPressed():
    if key == ' ':
        if player.isPlaying():
            player.pause()

        else:
            player.play()
