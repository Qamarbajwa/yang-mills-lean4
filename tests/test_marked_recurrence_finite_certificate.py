"""Independent finite rational certificate; no cutoff-uniform conclusion."""
from fractions import Fraction as F


def test_third_connected_coefficient_requires_conditional_covariance_sector():
    weights = [F(1, 8), F(1, 8), F(3, 8), F(3, 8)]
    x1 = [F(0), F(0), F(2), F(2)]
    x2 = [F(-1), F(1), F(-2), F(2)]
    x3 = x2[:]

    def mean(values):
        return sum(w * x for w, x in zip(weights, values))

    m1, m2, m3 = map(mean, (x1, x2, x3))
    m12 = mean([a * b for a, b in zip(x1, x2)])
    m13 = mean([a * b for a, b in zip(x1, x3)])
    m23 = mean([a * b for a, b in zip(x2, x3)])
    m123 = mean([a * b * c for a, b, c in zip(x1, x2, x3)])
    connected = m123 - m1 * m23 - m2 * m13 - m3 * m12 + 2 * m1 * m2 * m3
    coarse_mean = F(3, 2)
    coarse_covariance = F(6) - coarse_mean * F(13, 4)
    assert m2 == m3 == m12 == m13 == 0
    assert connected == coarse_covariance == F(9, 8)
