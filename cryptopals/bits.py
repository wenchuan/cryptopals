#!/usr/bin/python

def xor(a,b):
    return [x^y for x,y in zip(a,b)]

def xor_encrypt(cleartext, key):
    '''key is an array'''
    return [x^y for x,y in zip(cleartext, key * (len(cleartext) / len(key) + 1))]

def hamming_distance(x, y):
    """calculate the hamming distance of two given byte strings"""
    assert len(x) == len(y)
    return sum([count_set_bits(b) for b in xor(x,y)])

def count_set_bits(b):
    """count the bits of a byte"""
    assert 0 <= b <= 255
    r = 0
    while b != 0:
        r += 1
        b = (b & (b - 1))
    return r
