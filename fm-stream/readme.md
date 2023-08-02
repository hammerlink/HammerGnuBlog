# Next goal

- detect the distance to the radio transmitter
- transmit with dab+ protocol

# Walkthrough
## Soapy HackRF block sampling issue

Appearantly this block does no longer allow a dynamic sample rate. It has a fixed sample rate every 1e6.
I needed to work with rational resampler block. To transform the sample rate correctly.

## Low volume

I managed to get it to work on my radio. But it was very hard to detect as it was very silent.
My next goal is to control the volume.

### Multiply const 2023-07-25

I tried to change the volume on the FM radio by using a multiply const block
But anywhere I placed the block it didn't have the required effect

I found the following blog: 
https://lists.gnu.org/archive/html/discuss-gnuradio/2016-03/msg00769.html

They are also talking about the rational resampler, could this be an influence?

### Local audio sink to test the volume

I want better control of the multiply const block. I will attach it to my computer sound to test if the block works.
The multiply const block does nothing to the volume.
Possibly related to the volume of the computer? Not really, you can scale youtube & other programs their sound internally

According to the documentation on the wiki this should be the correct approach
https://wiki.gnuradio.org/index.php/Simulation_example:_AM_transmitter_and_receiver

### WAV File

The issue might be that the WAV files cannot use a multiply const since the values are fixed?
To investigate

After consulting ChatGPT it suggested that I should check the FM transmittion strength.

Or the format of the WAV signal could be bad. It might be intresting to record my own WAV file to check this out.

I discovered the mistake. I was using the wrong variable ID in the multiply const block. Therefor the volume never changed.
You need to use the ID of the QT GUI Range slider instead of the variable name. Silly mistake.

In mean time I also discovered that you can record data into a regular file. Capturing all the samples in raw state.
The WAV file format is more compressed, containing the same data.

### Test
Low volume test executed successfully
