# Detection Count Visualisation
An example application for consuming the output of [detection-count-stream-processor](https://github.com/ScreamingUdder/detection-count-stream-processor) for SANS2D data.

Contains main script, PulseImage Flatbuffers python file and some simple unit tests.

## Usage Instructions

### Historical Data
By setting `auto_offset_reset='earliest'` as part of the Kafka Consumer set up, the application can proces historical data sent to the specified topic, with no processing required.

### Live Data
In order to access a live data stream, keep or return `auto_offset_reset='latest'`. Download and run the  [detection-count-stream-processor](https://github.com/ScreamingUdder/detection-count-stream-processor), connecting it to an active source of [EventMessages](https://github.com/ess-dmsc/streaming-data-types/blob/master/schemas/ev42_events.fbs). Setting the python script to consume from the output topic of the processor will allow you to view an animated image of the detector.

### Example Output
If the application has been set up correctly, the image will eventually look something like this:
![Example Frequency Graph](https://github.com/ScreamingUdder/detection-count-visualisation/blob/master/exampleOutput.PNG)
