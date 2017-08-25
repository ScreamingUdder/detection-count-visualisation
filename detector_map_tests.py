import pytest
import consumer as ex
import numpy as np


def test_update_index_zero():
    detectors = np.zeros((ex.MAX_COLUMN * 2, ex.MAX_ROW)).astype(int)

    ex.update_detector(detectors, ex.DETECTOR_ID_OFFSET, 1)

    assert detectors[(0, 0)] == 1


def test_update_row_two():
    detectors = np.zeros((ex.MAX_COLUMN * 2, ex.MAX_ROW)).astype(int)

    ex.update_detector(detectors, ex.MAX_COLUMN + ex.DETECTOR_ID_OFFSET, 1)

    assert detectors[(0, 1)] == 1


def test_update_index_zero_panel_two():
    detectors = np.zeros((ex.MAX_COLUMN * 2, ex.MAX_ROW)).astype(int)

    ex.update_detector(detectors, ex.FIRST_DETECTOR_MAX + ex.DETECTOR_ID_OFFSET, 1)

    assert detectors[(ex.MAX_COLUMN, 0)] == 1


def test_update_row_two_panel_two():
    detectors = np.zeros((ex.MAX_COLUMN * 2, ex.MAX_ROW)).astype(int)

    ex.update_detector(detectors, ex.FIRST_DETECTOR_MAX + ex.MAX_COLUMN + ex.DETECTOR_ID_OFFSET, 1)

    assert detectors[(ex.MAX_COLUMN, 1)] == 1
