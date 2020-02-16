"""This file declares an abstract class for a constant-based
compression algorithm. This algorithm consists of finding sequences of data in
irrational constants. For instance:
    The input file in hex (meaningless):
        3f195a3103702e30
    The Pi number in hex:
        3.243f6a8885a308d313198a2e03707344a40
    Then, the input file is divided into clasters that were found:
        3f|19|5a|31|0370|2e|30
    The output file in hex (schematically)
        [3|2][19|2][10|2][16|2][25|4][23|2][12|2]

This file contains such classes:
  ConstantCompressor - an abstract class for this compression algorithm.
"""
