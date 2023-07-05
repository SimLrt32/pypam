.. currentmodule:: pypam

Introduction to pypam
=====================

Concepts
--------
The idea of pypam is to process all the acoustic data resulting from an underwater acoustic deployment.
For a deployment, we understand a single instrument from the moment it gets into the water until the moment it
is taken out.
This data is usually stored in different files (and folders), and sometimes has to be zipped because of lack of
storage space. Don't panic, you can still work with zipped folders directly from pypam without having to unzip the
whole project. Usually these files have a continuity in time, and very often it is interesting to extract time
series.

pypam allows to choose  "time window" per AcousticSurvey, which will be the time resolution of the computed output.
Then each feature will be computed on that time window (independently of the file duration and sampling frequency).
The output is an xarray dataset. The dimensions of these arrays are always:

* *id*: id of the bin (increasing integer)
extra coordinates (metadata)

* *datetime*: bin start timestamp of the "time window"
* *start_sample*: start sample of the bin respect to the file
* *end_sample*: end sample of the bin respect to the file
* *id_*: id with respect to the file (changes when multiple files per deployment)


Temporal (features) analysis
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
In bioacoustics, sometimes several frequency bands are interesting to study at the same time and extract features.
pypam allows so by passing a list of bands to analyze. Then, a features per "time window" and per frequency band is
computed.

For features analysis, the second dimension is:

- *bands*: all the bands analyzed (just as an int)
extra coordinates (metadata)

- *band_lowfreq*: low limit of the frequency band
- *band_highfreq*: high limit of the frequency band

Available features
~~~~~~~~~~~~~~~~~~
The available features now are:

+------------------------+----------------+---------------+
| Feature name           | Type           | string        |
+========================+================+===============+
| Acoustic Complexity    | acoustic index | aci           |
| Index (ACI)            |                |               |
+------------------------+----------------+---------------+
| Bioacoustic Index (BI) | acoustic index | bi            |
+------------------------+----------------+---------------+
| Spectral Entropy of    | acoustic index | sh            |
| Shannon (SH)           |                |               |
+------------------------+----------------+---------------+
| Temporal Entropy of    | acoustic index | th            |
| Shannon (SH)           |                |               |
+------------------------+----------------+---------------+
| Normalized Difference  | acoustic index | th            |
| Sound Index (NDSI)     |                |               |
+------------------------+----------------+---------------+
| Acoustic Evenness      | acoustic index | aei           |
| Index (AEI)            |                |               |
+------------------------+----------------+---------------+
| Acoustic Diversity     | acoustic index | adi           |
| Index (ADI)            |                |               |
+------------------------+----------------+---------------+
| Zero Crossing Rate     | acoustic index | zcr           |
| (ZCR)                  |                |               |
+------------------------+----------------+---------------+
| Acoustic Diversity     | acoustic index | adi           |
| Index (ADI)            |                |               |
+------------------------+----------------+---------------+
| Root Mean Squared      | temporal       | rms           |
| Value (rms)            | feature        |               |
+------------------------+----------------+---------------+
| Sound Exposure Level   | temporal       | sel           |
| (SEL)                  | feature        |               |
+------------------------+----------------+---------------+
| Dynamic Range          | temporal       | dynamic_range |
|                        | feature        |               |
+------------------------+----------------+---------------+
| Peak                   | temporal       | peak          |
|                        | feature        |               |
+------------------------+----------------+---------------+
| Root Mean Squared      | temporal       | rms_envelope  |
| Value Envelope         | feature        |               |
+------------------------+----------------+---------------+
| Spectrum Slope         | temporal       | spectrum_slope|
|                        | feature        |               |
+------------------------+----------------+---------------+



Frequency domain analysis
^^^^^^^^^^^^^^^^^^^^^^^^^
pypam allows to compute frequency-domain analysis (spectrum, spectrogram, third octave band levels...) per "time window"

For frequency domain analysis, the second dimension is:
  - frequency: central frequency of the frequency band

In case of spectrograms, a third dimension is added:
 - time: time in seconds of the spectrogram at that specific time window


Frequency domain features
~~~~~~~~~~~~~~~~~~~~~~~~~
  - spectrogram
  - Spectrum
    - power_spectrum
    - psd (power spectral density)
  - Spectral Probability Density (SPD)
  - octave bands


