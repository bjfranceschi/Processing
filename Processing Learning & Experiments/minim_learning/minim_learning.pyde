
'''
#helpful tips here: http://minimpython.blogspot.com/
'''

# import minim library
add_library('minim')


def setup():
    size(600, 750, P3D)

    # instantiate minim object
    minim = Minim(this)
    
    # make global variable to hold loaded mp3
    global player
    player = minim.loadFile('super_sprode.mp3')
    print(player.left.get(10))


def draw():
    background(100)

    # "player.left.get" is used to get a certain sample from the left channel.
    # bufferSize() is an integer with has the number of "samples" in the buffer.
    # a sample here is a snapshot of the sound my computer takes. (these are not
    # sequential- just different snapshots of the whole thing)
    # the "buffer" is the amount of time alotted by my computer to process audio
    # So with this loop we're getting every left sample value in the audio all the time
    for sample in range(0, player.bufferSize()):
        sound_value_left = player.left.get(sample)
        sound_value_right = player.right.get(sample)

        with pushMatrix():
            translate(width/4, height/2, 0)
            box(100*(sound_value_left*2), 100*(sound_value_left*2), 0)

        with pushMatrix():
            translate(width/1.5, height/2, 0)
            box(100*(sound_value_right*2), 100*(sound_value_right*2), 0)

    

def keyPressed():
    if player.isPlaying():
        player.pause()
        
    else:
        player.play()
