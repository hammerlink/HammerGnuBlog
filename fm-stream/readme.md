# Next goal

- detect the distance to the radio transmitter

# Walkthrough
## Soapy HackRF block sampling issue

Appearantly this block does no longer allow a dynamic sample rate. It has a fixed sample rate every 1e6.
I needed to work with rational resampler block. To transform the sample rate correctly.

## Low volume

I managed to get it to work on my radio. But it was very hard to detect as it was very silent.
My next goal is to control the volume.


