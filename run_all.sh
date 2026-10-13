#!/usr/bin/env bash
# Hourly: refresh sibling repos, run E2E tests, regenerate README, commit+push. Uses flock lock.
set -uo pipefail
cd "$(dirname "$0")"
exec 9>/tmp/fertiggerichte-hub.lock
flock -n 9 || { echo "already running"; exit 0; }
for d in /workspace/food-connectors /workspace/fertiggerichte-daten; do git -C "$d" pull -q --ff-only 2>/dev/null || true; done
rm -rf results screenshots; mkdir -p results screenshots
timeout 2400 python3 -m pytest -q tests -p no:cacheprovider --junitxml=results/junit.xml || true
python3 make_report.py
git add -A && git commit -qm "report: $(date -u +%Y-%m-%dT%H:%MZ)" && git push -q origin HEAD:main || true
