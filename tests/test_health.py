import numpy as np
from battery_rul_lab.health import capacity_retention, linear_rul

def test_retention(): assert capacity_retention(80, 100) == .8

def test_rul_is_positive(): assert linear_rul(np.arange(5), 1 - .02*np.arange(5)) > 0
