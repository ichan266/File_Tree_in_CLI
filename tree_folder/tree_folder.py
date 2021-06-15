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
        """ Here, we take in root_dir as the root directory as our argument and create an instance attribute, _generator, by using an OOP technique called composition that defines a "has a relationship. This means that every DirectoryTree object has a _TreeGenerator object attached."""
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

    def _tree_head(self):
        """ This method adds _root_dir to the _tree list (from the init method above). It then adds PIPE (see line 6) to the same list, signaling that it's on the top level. `os.sep` probably means starting a new line in CMD"""
        self._tree.append(f"{self._root_dir}{os.sep}")
        self._tree.append(PIPE)

    def build_tree(self):
        """ In this method, we call the _tree_head method we wrote above to create the tree head, (we haven't written the _tree_body method yet), generate the rest of the file tree diagram by using recursion. """
        self._tree_head()
        self._tree_body(self._root_dir)
        return self._tree
