#!/usr/bin/env python

import argparse
import logging
import sys
import typing

logger = logging.getLogger(__name__)

def capture_options() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--build-dir', default=tempfile.NamedTemporaryFile().name, type=str)
    return parser.parse_args()

def main(options: argparse.Namespace) -> None:
    sys.exit(0)

if __name__ == '__main__':
    options = capture_options()
    main(options)

