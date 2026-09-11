# Battery RUL Lab

[![Quality](https://github.com/vipul957/battery-rul-lab/actions/workflows/quality.yml/badge.svg)](https://github.com/vipul957/battery-rul-lab/actions/workflows/quality.yml) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> **Battery RUL Lab** is a battery health estimation and remaining-useful-life research toolkit.

## Start here

**In one sentence:** Estimate battery health and remaining useful life with interpretable uncertainty.

| If you want to... | Open this first |
|---|---|
| Understand the method | [`src/battery_rul_lab/health.py`](src/battery_rul_lab/health.py) |
| See the second reusable utility | [`src/battery_rul_lab/uncertainty.py`](src/battery_rul_lab/uncertainty.py) |
| Run a tiny example | [`examples/quick_demo.py`](examples/quick_demo.py) |
| Understand the next milestone | [`docs/ROADMAP.md`](docs/ROADMAP.md) |
| Check correctness | [`tests/`](tests/) and the CI badge above |

### System flow

```mermaid
flowchart LR
    A[Domain input] --> B[Validated contract]
    B --> C[health indicators]
    C --> D[Measured output]
    D --> E[Limitations and next experiment]
```

### What is implemented now

The repository currently contains a dependency-light, deterministic baseline with tests. It is intentionally small enough to inspect line by line. The next research layer should preserve the same input contract and evaluation protocol rather than replacing the baseline with an opaque demo.


## Problem statement

Estimate degradation state and remaining cycles while communicating uncertainty.

The central mathematical object is **capacity retention q[t]/q[rated] and threshold-crossing RUL**. The current implementation keeps this object small and testable so that later deep-learning improvements can be compared with an auditable baseline.

## Data contract

Expected input: **cycle-indexed capacity, voltage, current, temperature, impedance, and protocol metadata**. Every adapter must document units, provenance, timezone, missing values, licensing, and information available at prediction time. Synthetic examples test the software contract; they are not domain evidence.

## Baseline and assumptions

The first method is **interpretable health indicators followed by state-space or sequence models**. It assumes correctly timestamped observations and a stable evaluation definition. A future model must preserve the split logic and report improvement over this baseline rather than only reporting an absolute score.

## Evaluation protocol

Report **cycle MAE, retention error, concordance, calibration, early-warning lead time**. Include performance by regime, calibration or uncertainty quality where applicable, compute cost, and known failure cases. Never tune repeatedly on the final test set.

## Next research milestone

**Add licensed battery adapters, sequence features, bootstrap intervals, and a model card.**

## Research status

This repository is a documented baseline and extensible source scaffold. Results are experimental until validated on a licensed, representative dataset. No proprietary data, employment claim, endorsement, or company affiliation is implied.

## Architecture

The project separates domain formulation, data contracts, deterministic baselines, model implementations, evaluation, and deployment concerns. `src/` contains importable utilities, `tests/` contains fast contract tests, `examples/` contains runnable synthetic demonstrations, and `docs/ROADMAP.md` describes the next research stages.

## Reproducibility contract

Any future experiment must record dataset provenance and license, units and timezone, sampling interval, missing-value policy, split logic, random seeds, software versions, compute environment, and known limitations. Preprocessing must be fitted only on training data. Temporal problems require chronological or group-aware splits.

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
pytest -q
python examples/quick_demo.py
```

## Engineering standards

The repository includes GitHub Actions CI, MIT licensing, contribution and security guidance, issue and pull-request templates, and monthly Dependabot updates. A model card should be added before presenting domain results as decision-ready.

## Limitations

The baseline is not production-ready. Real deployment requires external validation, monitoring, access controls, incident response, and review by subject-matter experts.

## References

[1]: https://scikit-learn.org/stable/modules/model_evaluation.html "Scikit-learn model evaluation"
[2]: https://pytorch.org/docs/stable/index.html "PyTorch documentation"
