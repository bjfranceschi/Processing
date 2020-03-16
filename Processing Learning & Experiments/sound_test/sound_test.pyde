
# this imports a processing library
add_library('sound')


def setup():
    size(600, 750)
    noFill()
    stroke(200)
    
    global sf
    sf = SoundFile(this, 'super_sprode.mp3')
    
    
def draw():
    background(0)
    
    # set a variable for playback speed equal to your mouseX values on the screen,
    # which are mapped to a range of (.25 to 2)
    playback_speed = map(mouseX, 0, width, 0.5, 1.5)
    sf.rate(playback_speed)


def mouseClicked():
    sf.stop()
    sf.play()
