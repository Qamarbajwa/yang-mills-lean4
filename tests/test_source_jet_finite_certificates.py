"""Exact finite countermodels; no test certifies a continuum estimate."""
from fractions import Fraction as F


def test_vacuum_normalized_conditional_transport_certificate():
    # Haar weights 1/3; unnormalized Gibbs weights 1,2,3.
    density = [F(1), F(2), F(3)]
    values = [F(-1), F(2), F(4)]
    groups = [[0, 1], [2]]
    vacuum = sum(density) / 3
    global_moment = sum(d * x for d, x in zip(density, values)) / sum(density)
    transported = F(0)
    for group in groups:
        mass = sum(density[i] for i in group) / 3
        insertion = sum(density[i] * values[i] for i in group) / sum(density[i] for i in group)
        transported += mass * insertion / vacuum
    assert transported == global_moment == F(5, 2)
    # Dividing the entire source jet by itself would erase this nonzero coefficient.
    assert transported != 0


def test_signed_mass_one_is_not_probability_certificate():
    weights, values = [F(2), F(-1)], [F(1), F(-1)]
    assert sum(weights) == 1
    assert sum(abs(w) for w in weights) == 3
    assert sum(w * x for w, x in zip(weights, values)) == 3
    assert max(abs(x) for x in values) == 1


def test_second_source_connected_defect_certificate():
    weights, values = [F(1, 2), F(1, 2)], [F(-1), F(1)]
    first = sum(w * x for w, x in zip(weights, values))
    joint = sum(w * x * x for w, x in zip(weights, values))
    defect = joint - first * first
    assert first == 0 and joint == 1 and defect == 1
    assert first * first + defect == joint
