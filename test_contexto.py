"""Test script for Contexto."""

import sys
from contexto.cli.src.main import app

if __name__ == "__main__":
    # Run the CLI app with the provided arguments
    sys.argv = ["contexto"] + sys.argv[1:]
    app()
