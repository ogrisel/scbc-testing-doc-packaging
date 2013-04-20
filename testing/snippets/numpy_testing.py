import numpy as np
from numpy.testing import assert_array_equal
from numpy.testing import assert_array_almost_equal


def test_array_comparisions():
    ones = np.ones(3)
    assert_array_equal(ones, [1, 1, 1])
    assert_array_equal(ones, [1.0, 1.0, 1.0])


def test_array_comparisions_up_to_precision():
    thirds = np.ones(3) / 3.
    assert_array_almost_equal(thirds, [0.33, 0.33, 0.33], 2)
