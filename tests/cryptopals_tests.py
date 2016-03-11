#!/usr/bin/python

from nose.tools import *
from cryptopals import base64, xor
from random import shuffle

def setup():
    print "SETUP!"

def teardown():
    print "TEAR DOWN!"

def test_hexstring_to_bytes_empty():
    assert [] == base64.hex_decode('')

def test_hexstring_to_bytes_simple():
    assert [0] == base64.hex_decode('00')
    assert [1] == base64.hex_decode('01')
    assert [255] == base64.hex_decode('ff')

def test_hexstring_to_bytes_full_range():
    source = range(256)
    hexstring = ''.join([format(x, '02x') for x in source])
    transformed = base64.hex_decode(hexstring)
    print source
    print hexstring
    print transformed
    assert source == transformed

def test_hexstring_to_bytes_full_range_shuffled():
    source = range(256)
    shuffle(source)
    hexstring = ''.join([format(x, '02x') for x in source])
    transformed = base64.hex_decode(hexstring)
    print source
    print hexstring
    print transformed
    assert source == transformed

def test_encode_block():
    assert 'AAAA' == base64.encode_block([0,0,0])
    assert '////' == base64.encode_block([255,255,255])
    assert 'Beef' == base64.encode_block([5,231,159])
    assert 'YW55' == base64.encode_block([97,110,121])
    assert 'cw==' == base64.encode_block([115])
    assert 'c3U=' == base64.encode_block([115, 117])

def test_base64_encode():
    assert 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t' == base64.base64_encode('49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d')

def test_fixed_xor():
    assert base64.hex_decode('746865206b696420646f6e277420706c6179') == xor.xor(base64.hex_decode('1c0111001f010100061a024b53535009181c'), base64.hex_decode('686974207468652062756c6c277320657965'))
