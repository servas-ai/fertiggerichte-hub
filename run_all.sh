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
# Sanity gate: never publish an empty report (e.g. pytest killed by timeout under box overload).
if ! python3 -c "import json,sys;d=json.load(open('report.json'));c=d.get('connectors');sys.exit(0 if (len(c) if isinstance(c,(list,dict)) else (c or 0))>0 else 1)"; then
  echo "empty report (no connector results) - not committing; restoring last good report"
  git checkout -- . 2>/dev/null; git clean -fdq results screenshots 2>/dev/null
  exit 3
fi
git add -A && git commit -qm "report: $(date -u +%Y-%m-%dT%H:%MZ)" && { git pull -q --rebase origin main || git rebase --abort; git push -q origin HEAD:main; } || true
