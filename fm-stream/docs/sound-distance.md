# Sound Distance

## Concept

The idea is to triangulate sounds to know where they are located relatively towards the microphones.

As a first I need to be able to figure out what sounds are visible via the GNU Radio. I will need to filter out only clear signals.

To keep it simple I will start with producing a constant signal at 500 hz. This will be transmitted from my laptop.
A microphone will also be connected to my laptop. This will be capturing sound via GNU Radio. I will need to filter out this 500hz signal as a digital signal. After processing I should receive a starting time, when I first picked up the signal.

Let's GO!
