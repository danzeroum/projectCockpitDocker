"""Ponto de entrada: ``python -m cockpit_harness <comando>``."""

import sys

from cockpit_harness.cli import main

if __name__ == "__main__":
    sys.exit(main())
