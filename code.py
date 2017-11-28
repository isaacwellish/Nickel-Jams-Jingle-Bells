# Playground 808
# Drum machine
from digitalio import DigitalInOut, Direction
import audioio
import touchio
import board
import time
import neopixel

RED = 0x100000 # (0x10, 0, 0) also works
GREEN = (0, 0x10, 0)
 
bpm = 120 #beats per minute for sustained hold, change this to suit your tempo
 

#new neopixel code
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=.8)
pixels.fill((0,0,0))

pixels[0] = RED
pixels[1] = GREEN
pixels[2] = RED
pixels[3] = GREEN
pixels[4] = RED
pixels[5] = GREEN
pixels[6] = RED
pixels[7] = GREEN
pixels[8] = RED
pixels[9] = GREEN

pixels.show()




# enable the speaker
spkrenable = DigitalInOut(board.SPEAKER_ENABLE)
spkrenable.direction = Direction.OUTPUT
spkrenable.value = True
 
# make the input cap sense pads
capPins = (board.A1, board.A2, board.A3, board.A4, board.A5)
 
touchPad = []
for i in range(5):
    touchPad.append(touchio.TouchIn(capPins[i]))
 
# The seven files assigned to the touchpads
audiofiles = ["CJingle.wav", "DJingle.wav", "EJingle.wav",
               "FJingle.wav", "GJingle.wav"]
 
def play_file(filename):
    print("playing file "+filename)
    f = open(filename, "rb")
    a = audioio.AudioOut(board.A0, f)
    a.play()
   # time.sleep(bpm/960) #sixteenthNote delay


 
while True:


    for i in range(5):
        if touchPad[i].value:
            play_file(audiofiles[i])




