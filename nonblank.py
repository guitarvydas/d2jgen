#!/usr/bin/env python3
"""Read lines from stdin and output only the non-empty, non-blank lines."""

import sys


def main():
    for line in sys.stdin:
        if line.strip():
            sys.stdout.write(line)


if __name__ == "__main__":
    main()
