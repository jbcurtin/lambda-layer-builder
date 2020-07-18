#!/usr/bin/env python

import argparse
import git
import logging
import os
import subprocess
import sys
import tempfile
import time
import typing

DELAY = .1
ENCODING = 'utf-8'
logger = logging.getLogger(__name__)

def run_command(cmd: typing.Union[str, typing.List[str]]) -> None:
    if isinstance(cmd, str):
        cmd = [cmd]

    proc = subprocess.Popen(cmd, shell=True)
    while proc.poll() is None:
        time.sleep(DELAY)

    if proc.poll() > 0:
        raise Exception

def capture_options() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--git-url', required=True, type=str)
    parser.add_argument('-d', '--build-dir', default=tempfile.NamedTemporaryFile().name, type=str)
    parser.add_argument('-c', '--commit', required=True, type=str)
    parser.add_argument('-m', '--build-command', required=True, type=str)
    return parser.parse_args()

def main(options: argparse.Namespace) -> None:
    logger.info(f'Checking out Git Repository[{options.git_url}] into DIR[{options.build_dir}]')

    repo = git.Repo.clone_from(options.git_url, options.build_dir, branch='master')
    repo.git.checkout(options.commit)
    old_dir = os.getcwd()
    os.chdir(options.build_dir)
    run_command(options.build_command)
    os.chdir(old_dir)
    sys.exit(0)

if __name__ == '__main__':
    options = capture_options()
    main(options)

