
# this imports a processing library
add_library('sound')


def setup():
    size(600, 750)
    noFill()
    stroke(200)
    
    global sf
    
    path = '/Users/Bfranceschi/Documents/Processing/song_library'
    song = 'red_giant.mp3'

    sf = SoundFile(this, path + '/' + song)
    
    
def draw():
    background(0)
    
    # set a variable for playback speed equal to your mouseX values on the screen,
    # which are mapped to a range of (.25 to 2)
    playback_speed = map(mouseX, 0, width, 0.5, 1.5)
    sf.rate(playback_speed)


def mouseClicked():
    sf.stop()
    sf.play()
