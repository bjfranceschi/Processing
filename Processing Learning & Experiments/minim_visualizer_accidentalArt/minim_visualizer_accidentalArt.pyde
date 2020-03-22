
'''
#helpful tips here: http://minimpython.blogspot.com/
'''

# import minim library
add_library('minim')

Y = int()

def setup():
    size(1000, 750, P3D)

    # instantiate minim object
    minim = Minim(this)
    
    # make global variable to hold loaded mp3
    global player
    
    path = '/Users/Bfranceschi/Documents/Processing/song_library'
    song = 'super_sprode.mp3'
    
    player = minim.loadFile(path + '/' + song)
    print(player.left.get(10))

Y = int()

def draw():
    background(30)
    stroke(180)

    
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
     
        global Y
        Y = Y + .00000001
     
        rotateZ(Y)
     
        # this just makes a bunch of tiny lines (dots pretty much, that's
        # why "sample+1") where the height corresponds to the sound value and
        # width (x position too) corresponds to a different sample in the buffer
        line(200,
            360 + sound_value_left*100,
            sample-500,
            200,
            390 + sound_value_left*100,
            sample-501)
         
        line(width-200, 
            360 + sound_value_right*100,
            sample-500,
            width-200,
            390 + sound_value_right*100,
            sample-501)
        
        # for the far back strip, need to map "sample" which is normally in the
        # range of 0 to bufferSize max (0 to 1023) to fit where the side strips end
        x1 = map(sample, 0, player.bufferSize(), 154, 445)
        
        line(x1,
             354 + sound_value_mix*100,
             -player.bufferSize(),
             x1,
             397 + sound_value_mix*100,
             -player.bufferSize())
            




def keyPressed():
    if player.isPlaying():
        player.pause()
        
    else:
        player.play()
