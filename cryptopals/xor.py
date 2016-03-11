#!/usr/bin/python

def xor(a,b):
    return [x^y for x,y in zip(a,b)]

def xor_encrypt(cleartext, key):
    '''key is an array'''
    return [x^y for x,y in zip(cleartext, key * (len(cleartext) / len(key) + 1))]
