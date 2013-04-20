import unittest, tempfile, csv
import numpy as np
from nose.tools import assert_equals
from numpy.testing import assert_array_almost_equal


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.f = tempfile.TemporaryFile()
        self.f.write('0.1,0.2\n')
        self.f.write('-0.1,1.4\n')
        self.f.seek(0)

    def tearDown(self):
        self.f.close()

    def test_numpy_csv(self):
        a = np.loadtxt(self.f, delimiter=',')
        assert a.shape == (2, 2)

        expected = [[0.1, 0.2], [-0.1, 1.4]]
        assert_array_almost_equal(a, expected, 2)

    def test_csv(self):
        dicts = list(csv.DictReader(self.f, fieldnames=['a', 'b']))
        assert len(dicts) == 2

        expected = [{'a': '0.1', 'b': '0.2'}, {'a': '-0.1', 'b': '1.4'}]
        assert_equals(dicts, expected)
