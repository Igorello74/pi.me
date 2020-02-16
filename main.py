"""
This script is intended to compress files using
the Pi number-based algorithm.

This algoryithm consists of finding byte sequnces
of the default_cluster length (in bytes) in the Pi number.
It's known that the Pi is irrational,
therefore any sequnces can be found in it.
Then, after finding them, it records something like that to
the output:
    [the digit place][the length of the cluster]
"""

import click


def cli():
    pass


class PiCompessor:
    """Compress files and byte-sequnces using the Pi-compression algorithm.
    This algoryithm consists of finding byte sequnces
    of the default_cluster length (in bytes) in the Pi number.
    It's known that the Pi is irrational,
    therefore any sequnces can be found in it.
    Then, after finding them, it records something like that to
    the output:
        [the digit place][the length of the cluster]
    """
    
    def __init__(default_cluster_size, 


def compess_src_into_dst(src, dst, default_size, last_digit):
    """Compress the given file at path using the Pi-compression algorythm.
    
    
    This algorythm consists of finding byte sequnces
    of the default_cluster length (in bytes) in the Pi number.
    It's known that the Pi is irrational,
    therefore any sequnces can be found in it.
    Then, after finding them it 