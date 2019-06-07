import unittest

import numpy as np

from bdacore.outliers import mad, mad_outliers, fft_outliers


class UtilsOutliersTest(unittest.TestCase):
    def test_mad(self):
        # given
        a = [1, 2, 3, 3, 4, 4, 4, 5, 5.5, 6, 6, 6.5, 7, 7, 7.5, 8, 9, 12, 52, 90]

        # when
        mad_value = mad(a)

        # then
        self.assertEqual(2.0, mad_value)

    def test_mad_outliers(self):
        # given
        a = np.array([1, 0, 0, 1, 10, 2, 115, 110, 32, 16, 2, 0, 15, 1])

        # when
        outliers = mad_outliers(a)

        # then
        y_true = [False, False, False, False, True, False, True, True, True, True, False, False, True, False]

        self.assertListEqual(y_true, outliers.tolist())

    def test_fft_outliers(self):
        # given
        a = np.array([1, 0, 0, 1, 10, 2, 115, 110, 32, 16, 2, 0, 15, 1])

        # when
        outliers = fft_outliers(a, freq_cut_index=12, outlier_proportion=0.2)

        # then
        y_true = [False, False, False, False, False, False, True, True, False, False, False, False, False, False]

        self.assertListEqual(y_true, outliers.tolist())


if __name__ == '__main__':
    unittest.main()
