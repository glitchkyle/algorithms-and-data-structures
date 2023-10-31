from math import exp, pi, cos, sin
from unittest import TestCase

def FFT(P):
    n = len(P)

    if n <= 1:
        return P
    theta = -2 * pi / n
    w = [complex(cos(theta * i), sin(theta * i)) for i in range(n)]

    y_e = FFT(P[::2])
    y_o = FFT(P[1::2])

    y = [0 + 0j for _ in range(n)]
    for j in range(n // 2):
        y[j] = y_e[j] + w[j] * y_o[j]
        y[j + n // 2] = y_e[j] - w[j] * y_o[j]

    return y

def ifft(poly):
    N = len(poly)
    if N <= 1:
        return poly
    even = ifft(poly[0::2])
    odd = ifft(poly[1::2])
    theta = 2 * pi / N
    w =[complex(cos(theta * i), sin(theta * i)) for i in range(N)]

    result = [0 + 0j for _ in range(N)]
    for k in range(N):
        result[k] = even[k % (N // 2)] + w[k] * odd[k % (N // 2)]

    return result / N

class FastFourierMultiplication(TestCase):

    tests = [
        (
            12345,
            6789,
            83810205
        ),
        (
            0,
            0,
            0
        ),
        (
            123,
            1,
            123
        ),
        (
            1,
            123,
            123
        ),
        (
            11,
            11,
            121
        ),
        (
            99999,
            1,
            99999
        ),
        (
            999999999,
            1,
            999999999
        ),
        (
            123456789,
            987654321,
            121932631112635269
        ),
        (
            1234567890,
            9876543210,
            12193263111263526900
        )
    ]

    @staticmethod
    def func(x, y):
        """
        Recall: given 2 n-bit numbers x and y (where n is large), we can compute z = xy in O(n1.59)
        using Guass’s idea. Also, recall another important divide and conquer algorithm called Fast
        Fourier Transform (FFT), we can multiply two n-bit numbers in O(n log n loglog n). Try to
        design the multiplication algorithm using FFT. Outline your algorithms and complexity
        calculations.

        O(n log n loglog n)
        """
        x_poly = [x]
        y_poly = [y]

        n = 1
        while n < max(len(x_poly), len(y_poly)):
            n *= 2

        x_poly.extend([0] * (n - len(x_poly)))
        y_poly.extend([0] * (n - len(y_poly)))

        x_fft = FFT(x_poly)
        y_fft = FFT(y_poly)

        result_fft = [a * b for a, b in zip(x_fft, y_fft)]

        result_poly = ifft(result_fft)
        result = int(round(result_poly[0].real))

        return result

    def test(self):
        for test in self.tests:
            self.assertEqual(len(test), 3)
            output = FastFourierMultiplication.func(test[0], test[1])
            self.assertEqual(output, test[2])