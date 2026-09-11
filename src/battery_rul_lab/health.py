"""Interpretable battery health indicators."""
from __future__ import annotations
import numpy as np

def capacity_retention(measured_capacity: float, rated_capacity: float) -> float:
    if rated_capacity <= 0: raise ValueError("rated_capacity must be positive")
    return float(measured_capacity / rated_capacity)

def linear_rul(cycles: np.ndarray, retention: np.ndarray, threshold: float = .8) -> float:
    """Estimate cycles until threshold using a least-squares degradation trend."""
    if len(cycles) != len(retention) or len(cycles) < 2: raise ValueError("need two aligned observations")
    slope, intercept = np.polyfit(cycles, retention, 1)
    if slope >= 0: return float("inf")
    return max(0.0, float((threshold - intercept) / slope - cycles[-1]))
