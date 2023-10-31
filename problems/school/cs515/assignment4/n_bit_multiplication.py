from unittest import TestCase

MAX_DIGITS = 27

def multiply_normal(a, b):
    a_len, b_len = len(a), len(b)
    z = [0 for _ in range(a_len + b_len)]
    for j in range(b_len):
        for i in range(a_len):
            z[j + i] += a[i] * b[j]
    return z

def carry(a):
    carry_over = 0

    for i in range(len(a)):
        a[i] += carry_over
        carry_over = a[i] // 10
        a[i] -= carry_over * 10

    return a

class NBitMultiplication(TestCase):

    tests = [
        (
            [1,2,3],
            [1],
            [1,2,3]
        ),
        (
            [1],
            [1,2,3],
            [1,2,3]
        ),
        (
            [6],
            [4],
            [2,4]
        ),
        (
            [1, 1],
            [1, 1],
            [1, 2, 1]
        ),
        (
            [9,9,9,9,9],
            [1],
            [9,9,9,9,9]
        ),
        (
            [9,9,9,9,9,9,9,9,9],
            [1],
            [9,9,9,9,9,9,9,9,9]
        ),
        (
            [1,2,3,4,5,6,7,8,9],
            [9,8,7,6,5,4,3,2,1],
            [1,2,1,9,3,2,6,3,1,1,1,2,6,3,5,2,6,9]
        )
    ]

    @staticmethod
    def func(a, b):
        """
        Recall: given 2 n-bit numbers x and y (where n is large), we can compute z = xy in O(n1.59)
        using Guass’s idea. Can we do even better than this. For example, 𝑂(𝑛1 + 𝜖) for any 𝜖 > 0.
        Elaborate your solution along with the complexity calculations of your algorithm.

        Toom-Cook algorithm: 𝑂(𝑛^log3(5)) where 1 + 𝜖 = log3(5)
        """

        a_m1, a_m2, a_0, a_1, a_inf = [], [], [], [], []
        b_m1, b_m2, b_0, b_1, b_inf = [], [], [], [], []
        c_m1, c_m2, c_0, c_1, c_inf = [], [], [], [], []
        c0, c1, c2, c3, c4          = [], [], [], [], []

        t_len = len(a)
        if t_len <= 9:
            return multiply_normal(a, b)

        a0 = a[:(t_len // 3)]
        a1 = a[(t_len // 3):(t_len * 2 // 3)]
        a2 = a[(t_len * 2 // 3):]
        b0 = b[:(t_len // 3)]
        b1 = b[(t_len // 3):(t_len * 2 // 3)]
        b2 = b[(t_len * 2 // 3):]

        for i in range(t_len // 3):
            a_m2.append((a2[i] << 2) - (a1[i] << 1) + a0[i])
            b_m2.append((b2[i] << 2) - (b1[i] << 1) + b0[i])

        for i in range(t_len // 3):
            a_m1.append(a2[i] - a1[i] + a0[i])
            b_m1.append(b2[i] - b1[i] + b0[i])

        a_0, b_0 = a0, b0
        for i in range(t_len // 3):
            a_1.append(a2[i] + a1[i] + a0[i])
            b_1.append(b2[i] + b1[i] + b0[i])

        a_inf, b_inf= a2, b2
        c_m2  = NBitMultiplication.func(a_m2, b_m2)
        c_m1  = NBitMultiplication.func(a_m1, b_m1)
        c_0   = NBitMultiplication.func(a_0, b_0)
        c_1   = NBitMultiplication.func(a_1, b_1)
        c_inf = NBitMultiplication.func(a_inf, b_inf)
        c4 = c_inf

        for i in range((t_len // 3) * 2):
            c  = -c_m2[i]
            c += (c_m1[i] << 1) + c_m1[i]
            c -= (c_0[i] << 1) + c_0[i]
            c += c_1[i]
            c += (c_inf[i] << 3) + (c_inf[i] << 2)
            c  = c // 6
            c3.append(c)

        for i in range((t_len // 3) * 2):
            c  = (c_m1[i] << 1) + c_m1[i]
            c -= (c_0[i] << 2) + (c_0[i] << 1)
            c += (c_1[i] << 1) + c_1[i]
            c -= (c_inf[i] << 2) + (c_inf[i] << 1)
            c  = c // 6
            c2.append(c)

        for i in range((t_len // 3) * 2):
            c  = c_m2[i]
            c -= (c_m1[i] << 2) + (c_m1[i] << 1)
            c += (c_0[i] << 1) + c_0[i]
            c += (c_1[i] << 1)
            c -= (c_inf[i] << 3) + (c_inf[i] << 2)
            c  = c // 6
            c1.append(c)

        c0 = c_0
        z = c0 + c2 + c4

        for i in range((t_len // 3) * 2):
            z[i + t_len // 3] += c1[i]

        for i in range((t_len // 3) * 2):
            z[i + t_len] += c3[i]

        number_str = (''.join(map(str, carry(z)))).strip('0')

        if len(number_str) % 2 == 0:
            number_str = number_str[::-1]

        output = [int(num) for num in number_str]

        return output

    def test(self):
        for test in self.tests:
            self.assertEqual(len(test), 3)

            for _ in range(MAX_DIGITS - len(test[0])):
                test[0].append(0)
            for _ in range(MAX_DIGITS - len(test[1])):
                test[1].append(0)

            a, b = test[0], test[1]
            output = NBitMultiplication.func(a, b)
            self.assertEqual(output, test[2])
