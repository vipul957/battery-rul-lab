from __future__ import annotations
import numpy as np
def bootstrap_mean(values, samples=500, seed=7):
    """Return mean and a 95 percent bootstrap interval."""
    x=np.asarray(values,dtype=float)
    if x.size < 2: raise ValueError("at least two values are required")
    rng=np.random.default_rng(seed); means=rng.choice(x,(samples,x.size),replace=True).mean(axis=1)
    return float(x.mean()), (float(np.quantile(means,.025)), float(np.quantile(means,.975)))
