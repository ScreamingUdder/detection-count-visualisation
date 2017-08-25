# An example heatmap generator, consuming Sans2D PulseImages outputted by the Kafka EventMessage Visualisation Streamer
import numpy as np
from kafka import KafkaConsumer
from PulseImage import PulseImage
import matplotlib.pyplot as plt
import matplotlib.animation as animation

MAX_COLUMN = 512
MAX_ROW = 120
FIRST_DETECTOR_MAX = 61440
DETECTOR_ID_OFFSET = 9

OUT_TOPIC_NAME = "FrameImageTest"
BROKERS = ["tenten:9092", "sakura:9092"]

consumer = KafkaConsumer(OUT_TOPIC_NAME, bootstrap_servers=BROKERS, auto_offset_reset='earliest', enable_auto_commit=False)


def update_detector(detectors, detector_id, value_to_add):
    x_to_be_added = 0

    detector_id -= DETECTOR_ID_OFFSET

    if detector_id >= FIRST_DETECTOR_MAX:
        detector_id -= FIRST_DETECTOR_MAX
        x_to_be_added += MAX_COLUMN

    y_cord = np.floor_divide(detector_id, MAX_COLUMN)
    x = (detector_id % MAX_COLUMN) + x_to_be_added

    detectors[(y_cord, x)] += value_to_add


def update_image(*args):
    messages = list(consumer.poll(1000, 1).values())
    if messages:
        message = messages[0][0]
    else:
        return im,
    pulse_image_bytes = message.value

    pulse_image = PulseImage.GetRootAsPulseImage(pulse_image_bytes, 0)

    for detector_id, detector_count in get_detector_info(pulse_image):
        update_detector(detectors, detector_id, detector_count)

    im.set_data(detectors)

    return im,


def get_detector_info(pulse_image):
    for i in range(0, pulse_image.DetectorIdLength()):
        detector_id = pulse_image.DetectorId(i)
        detector_count = pulse_image.DetectionCount(i)
        yield detector_id, detector_count


detectors = np.zeros((MAX_ROW, MAX_COLUMN * 2))
fig = plt.figure()
im = plt.imshow(detectors, animated=True, vmax=100, aspect="auto")
ani = animation.FuncAnimation(fig, update_image, interval=50, blit=True)
plt.show()