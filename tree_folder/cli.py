""" This module provides Tree CLI. """

import argparse
import pathlib
import sys

from . import __version__
from .tree_folder import DirectoryTree


def main():
    args = parse_cmd_line_arguments()
    root_dir = pathlib.Path(args.root_dir)
    if not root_dir.is_dir():
        print("The specified root directory does not exist")
        sys.exit()
    tree = DirectoryTree(root_dir)
    tree.generate()


def parse_cmd_line_arguments():
    parser = argparse.ArgumentParser(
        prog="tree",
        description="Tree Project, a directory tree generator",
        epilog="Thanks for giving it a try! =D"
    )
    parser.version = f"Tree Project v{__version__}"
    parser.add_argument("-v", "--version", action="version")
    parser.add_argument(
        "root_dir",
        metavar="ROOT_DIR",
        nargs="?",
        default=".",
        help="Generate a full directory tree starting at ROOT_DIR",
    )
    return parser.parse_args()
