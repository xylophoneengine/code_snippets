#!/usr/bin/env python3
"""
    Personal pylint example
"""
import argparse
from pathlib import Path

INPUT_FILE = ""

parser = argparse.ArgumentParser(description='cheat sheet')
parser.add_argument('-f',
                    '--flag',
                    action='store_true')
parser.add_argument('-i',
                    '--input-file',
                    type=str,
                    required=True,
                    action='store')

arguments = parser.parse_args()

if arguments.flag:
    print('yeih')

try:
    _f = Path(arguments.input_file)
except:
    exit(-1)
if not _f.exists():
    print("File does not exist")
if not _f.is_file():
    print("file does not exist")
INPUT_FILE = _f
