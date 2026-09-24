#!/usr/bin/env bash
# Reproduce the 5A format analysis.
#
# Expects the Play to Clinch research exports unpacked so that the season
# directories sit next to this script's `data/` path:
#
#   data/2092/{boys,girls}/...
#   data/2093/{boys,girls}/...
#   data/2094/{boys,girls}/...
#
# Pure stdlib Python 3 — no third-party packages required.
set -euo pipefail
cd "$(dirname "$0")/scripts"

python3 a1_capacity.py    # builds out_rows.json + out_dualfill.csv (roster + fill checks)
python3 a3_depth.py       # roster distribution and lineup-position ability curves
python3 a5_rescore.py     # counterfactual re-scoring of played duals under each format
python3 a6_postseason.py  # sweep/one-point rates and State-field dispersion
python3 a7_6s5d.py        # the 6S/5D petition: on-court demand, JV knock-on, roster settings
