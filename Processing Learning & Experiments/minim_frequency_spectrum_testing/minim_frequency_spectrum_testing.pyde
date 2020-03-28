
'''
#minim reference: http://code.compartmental.net/minim/
'''

# import minim library
add_library('minim')


def setup():
    size(1280, 330)
    
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
    
    # do the Fast Fourier forward transform on the "mix" channel (a mix of left and
    # right channels) of the audio buffer object
    fft.forward(player.mix)

    # here we create a line for each frequency band in the spectrum, where the
    # height of that line corresponds to the amplitude (getBand()) of that
    # frequency band. The lower frequency bands (1, 2, 3, 4, etc) correspond to
    # lower frequencies, and the higher frequency bands (200, 300, 400, etc)
    # correspond to higher ones. Seems like most of the common frequencies are 
    # within the range of band 0 to band 100, and 100 to 513 all seem very high
    
    # for full spectrum, make this equal to fft.specsize()
    spectrum = fft.specSize()-400
    
    for freq_band in range(spectrum):
        
        x = map(freq_band, 0, spectrum, 0, width)
        
        line(x, height, x, height - fft.getBand(freq_band)*8)


def keyPressed():
    if key == ' ':
        if player.isPlaying():
            player.pause()
        
        else:
            player.play()

        
