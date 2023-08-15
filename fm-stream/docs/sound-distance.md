# Sound Distance

## Concept

The idea is to triangulate sounds to know where they are located relatively towards the microphones.

As a first I need to be able to figure out what sounds are visible via the GNU Radio. I will need to filter out only clear signals.

To keep it simple I will start with producing a constant signal at 500 hz. This will be transmitted from my laptop.
A microphone will also be connected to my laptop. This will be capturing sound via GNU Radio. I will need to filter out this 500hz signal as a digital signal. After processing I should receive a starting time, when I first picked up the signal.

Let's GO!

## 2023 08 15 Producing the sound signal

To produce the sound signal I am working with a Signal Source in combination with an audio source (my default microphone).

### Analyzing the produced sound

2 tools are useful to analyze what I am doing:

#### QT GUI Frequency Sink

This sink visualizes all the active sound frequencies. It extracts all the active frequencies and shows them on a histogram.

Current Sample rate = 32k

Configuration:
- FFT Size = How many points are visualized on the histogram
The sound range that I want to analyze is between 0 - 1000 hz. This is a very small range.
The current sample rate is 32k so that means if I would use the default FFT size of 1024.
I would have 32000 / 1024 points visible => 31.25 distance between each point on the histogram.

=> I upgraded this to 16k so that I would see a point every 2 hz. This is sufficient to analyze the 0 - 1000 hz range.

- Average = (None, Low, Medium, High)
I want to analyze the current sound only, therefor I picked None. I don't need any averaging.
I suppose this is mainly useful if you are analyzing signals that are only very shortly visible. So that you can pick them up more easily.

### Filtering the produced sound

Using a Low pass & high pass filter I managed to take out the 500 hz signal specifically
