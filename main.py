#!/usr/bin/env python3
"""One Star, Written in Sap -- a make.fun one-liner entry.

Writes a single one-line 1-star review, in the voice of a houseplant
reviewing its human owner, to /output/entry.txt. Deterministic, stdlib only.
"""
import os

LINE = "One star: he named me after his ex, so I only get watered when he misses her \u2014 I've dropped six leaves spelling it out, and he still thinks I'm just thirsty."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
