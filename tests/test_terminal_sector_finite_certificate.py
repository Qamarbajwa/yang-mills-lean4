"""Exact finite normalization defects; no physical-measure or continuum claim."""
from fractions import Fraction as F


def test_rare_sector_probability_does_not_bound_marked_integral():
    values = []
    for epsilon in [F(1, 2), F(1, 4), F(1, 8)]:
        probability = epsilon**2
        marked_value = epsilon**-3
        integral = probability * marked_value
        assert integral == 1 / epsilon
        values.append((probability, integral))
    assert values[0][0] > values[1][0] > values[2][0]
    assert values[0][1] < values[1][1] < values[2][1]


def test_terminal_weight_and_source_factor_must_be_restored():
    # nu=(1/2,1/2), h=(1,3), and marked M=(0,2).
    vacuum = F(1, 2) * 1 + F(1, 2) * 3
    ordinary = F(1, 2) * 0 + F(1, 2) * 2
    terminal = (F(1, 2) * 1 * 0 + F(1, 2) * 3 * 2) / vacuum
    assert ordinary == 1
    assert terminal == F(3, 2)
    # (1+2z1)(1+3z2) has mixed coefficient6 although both vacua are1.
    scalar_factor = {frozenset(): F(1), frozenset({1}): F(2)}
    terminal_jet = {frozenset(): F(1), frozenset({2}): F(3)}
    mixed = sum(a * b for left, a in scalar_factor.items()
                for right, b in terminal_jet.items()
                if not left & right and left | right == frozenset({1, 2}))
    assert mixed == 6
    assert terminal_jet.get(frozenset({1, 2}), F(0)) == 0
