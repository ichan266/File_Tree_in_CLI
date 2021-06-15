""" This module provides Tree main module."""

import os
import pathlib

PIPE = "│"
ELBOW = "└──"
TEE = "├──"
PIPE_PREFIX = "│   "
SPACE_PREFIX = "    "


class DirectoryTree:
    def __init__(self, root_dir):
        self._generator = _TreeGenerator(root_dir)

    def generate(self):
        tree = self.generator.build_tree()
        for entry in tree:
            print(entry)


class _TreeGenerator:
    def __init__(self, root_dir):
        """ When initialize an object, it takes in root_dir as an argument. It also creates an empty list, tree, to store the file names. Please note we use pathlib to turn root_dir into a pathlib.Path object and store it in the non-public _root_dir."""
        self._root_dir = pathlib.Path(root_dir)
        self._tree = []

    def build_tree(self):
        self._tree_head()
        self._tree_body(self._root_dir)
        return self._tree

    def _tree_head(self):
        self._tree.append(f"{self._root_dir}{os.sep}")
        self._tree.append(PIPE)
