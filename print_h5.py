#!/usr/bin/env python
"""Print the contents of an HDF5 file"""
import numpy as np
np.warnings.filterwarnings('ignore')

import h5py
import argparse


def print_node(node, indent=4):
    """

    Args:
        node: the node to print
        indent: how many spaces per indent level

    Returns:
        None

    Examples
        >>> print_node("a/b/c", indent=4)
                c
        >>> print_node("a")
        a
        >>> print_node("a/b", indent=3)
           b
    """
    *first, last = str(node).split("/")
    print(" " * indent * len(first) + last)


def print_h5(h5filename, indent=4):
    """For a given HDF5 file, print its content"""
    with h5py.File(h5filename) as h5file:
        h5file.visit(lambda node: print_node(node, indent=2))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("h5file", help="HDF5 file to display")
    parser.add_argument("-i","--indent",
                        help="Indentation (default=4)",type=int,default=4)
    args = parser.parse_args()
    print_h5(args.h5file)


if __name__=="__main__":
    main()