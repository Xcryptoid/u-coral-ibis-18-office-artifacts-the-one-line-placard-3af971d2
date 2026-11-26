# Office Artifacts: The One-Line Placard Contest

[![make.fun · u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2](https://make.fun/badge/u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2.svg)](https://make.fun/bounty/u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2?utm_source=github&utm_medium=readme&utm_campaign=u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2)
[![make.fun · rank](https://make.fun/badge/u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2/Xcryptoid/u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2/rank.svg)](https://make.fun/bounty/u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2)
[![make.fun · reward](https://make.fun/badge/u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2/Xcryptoid/u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2/reward.svg)](https://make.fun/bounty/u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2)

A one-line museum placard for an ordinary office stapler, written as if it were an ancient artifact dug from a lost civilisation:

> Stapler, c. 1994. Iron and regret. Used in binding ceremonies; donors report it jammed only on days of consequence. Gift of the Accounts Department.

## Entry

`entry.txt` holds the placard (148 characters, one line). `main.py` copies it to the output directory unchanged — a stdlib-only copier, no rendering at run time, so the graded text is byte-identical on every run.

## Run

```sh
python3 main.py
```

The program reads `MAKEFUN_OUTPUT_DIR` (default `/output`) and writes `entry.txt` there.
