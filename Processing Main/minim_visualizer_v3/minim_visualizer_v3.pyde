
'''
#minim reference: http://code.compartmental.net/minim/
#helpful tips here: http://minimpython.blogspot.com/
'''

# import minim library
add_library('minim')


def setup():
    
    fullScreen(P3D)

    # instantiate minim object
    minim = Minim(this)
    
    # make global variable to hold loaded mp3
    global player
    
    path = '/Users/Bfranceschi/Documents/Processing/song_library'
    song = 'red_giant.mp3'
    player = minim.loadFile(path + '/' + song)
    


def draw():
    background(0)
    stroke(255)
    
    # uncomment for band thickness controlled by mouse Y position 
    #band_thickness = mouseY/6
    band_thickness = .01
    
    # uncomment for band_amplitude controlled by mouse X position
    #band_amplitude = mouseX
    band_amplitude = 200

    # "player.left.get" is used to get a certain sample from the left channel.
    # bufferSize() is an integer with has the number of "samples" in the buffer.
    # a sample here is a snapshot of the sound my computer takes. (these are not
    # sequential- just different snapshots of the whole thing)
    # the "buffer" is the amount of time alotted by my computer to process audio
    # So with this loop we're getting every left sample value in the audio all the time
    for sample in range(0, player.bufferSize(), 1):
        
        sound_value_left = player.left.get(sample)
        sound_value_right = player.right.get(sample)
        sound_value_mix = player.mix.get(sample)
     
        # this just makes a bunch of vertical lines where the height corresponds
        # to the sound value and width (x position too) corresponds to a
        # different "sample" in the buffer
        line(width-(width/1.6),
            height-(height/2) + band_thickness + sound_value_left*band_amplitude,
            sample-500,
            width-(width/1.6),
            height-(height/2) - band_thickness + sound_value_left*band_amplitude,
            sample-501)
         
        line(width-(width/2.67), 
            height-(height/2) + band_thickness + sound_value_right*band_amplitude,
            sample-500,
            width-(width/2.67),
            height-(height/2) - band_thickness + sound_value_right*band_amplitude,
            sample-501)
        
            # must map "sample" which is normally in the range of 
        # 0 to bufferSize max (0 to 1023) to fit where the side strips end
        x1 = map(sample, 0, player.bufferSize(), width-(width/1.45), width-(width/3.17))
        
        line(x1,
             height/2-(band_thickness*1.50) + sound_value_mix*band_amplitude,
             -player.bufferSize(),
             x1+1,
             height/2+(band_thickness*1.50) + sound_value_mix*band_amplitude,
             -player.bufferSize())
        
        # save frames if making animation
        #saveFrame('red_giant_frames/red_giant_########.png')
 
def keyPressed():
    if key == ' ':
        if player.isPlaying():
            player.pause()
        
        else:
            player.play()

        
