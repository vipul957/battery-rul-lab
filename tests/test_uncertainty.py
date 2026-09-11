from battery_rul_lab.uncertainty import bootstrap_mean
def test_bootstrap():
    mean, interval=bootstrap_mean([1,2,3])
    assert interval[0] <= mean <= interval[1]
