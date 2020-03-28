
'''
#minim reference: http://code.compartmental.net/minim/
'''

# import minim library
add_library('minim')


def setup():
    print(log(10))
    size(1280, 630)
    
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

def draw():
    background(0)
    stroke(250)
    
    # for full spectrum, make this equal to fft.specsize()
    spectrum = fft.specSize() - 300
    
    # LEFT channel
    fft.forward(player.left)

    for freq_band in range(0, spectrum, 1):
        
        x = map(freq_band, 0, spectrum, 0, width/2)
        line(x, height, x, height - fft.getBand(freq_band)*10)


    # RIGHT channel
    fft.forward(player.right)

    for freq_band in range(0, spectrum, 1):
        x = map(freq_band, 0, spectrum, width/2, width)
        line(x, height, x, height - fft.getBand(freq_band)*10)




def keyPressed():
    if key == ' ':
        if player.isPlaying():
            player.pause()
        
        else:
            player.play()

        
