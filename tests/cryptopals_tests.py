#!/usr/bin/python

from nose.tools import *
from cryptopals import base64, xor
from random import shuffle, randint, choice

def setup():
    print "SETUP!"

def teardown():
    print "TEAR DOWN!"

def test_hex_decode_empty():
    assert [] == base64.hex_decode('')

def test_hex_decode_simple():
    assert [0] == base64.hex_decode('00')
    assert [1] == base64.hex_decode('01')
    assert [255] == base64.hex_decode('ff')

def test_hex_decode_full_range():
    source = range(256)
    hexstring = ''.join([format(x, '02x') for x in source])
    transformed = base64.hex_decode(hexstring)
    print source
    print hexstring
    print transformed
    assert source == transformed

def test_hex_decode_full_range_shuffled():
    source = range(256)
    shuffle(source)
    hexstring = ''.join([format(x, '02x') for x in source])
    transformed = base64.hex_decode(hexstring)
    print source
    print hexstring
    print transformed
    assert source == transformed

def test_hex_encode_simple():
    assert '00' == base64.hex_encode([0])
    assert '01' == base64.hex_encode([1])
    assert '11' == base64.hex_encode([17])
    assert 'ff' == base64.hex_encode([255])

def test_hex_encode_decode():
    source = [randint(0,255) for i in xrange(1024)]
    assert source == base64.hex_decode(base64.hex_encode(source))

def test_hex_decode_encode():
    source = ''.join([choice('0123456789abcdef') for i in xrange(1024)])
    assert source == base64.hex_encode(base64.hex_decode(source))

def test_encode_block():
    assert 'AAAA' == base64.encode_block([0,0,0])
    assert '////' == base64.encode_block([255,255,255])
    assert 'Beef' == base64.encode_block([5,231,159])
    assert 'YW55' == base64.encode_block([97,110,121])
    assert 'cw==' == base64.encode_block([115])
    assert 'c3U=' == base64.encode_block([115, 117])

def test_decode_block():
    assert [0,0,0] == base64.decode_block('AAAA')
    assert [255,255,255] == base64.decode_block('////')
    assert [5,231,159] == base64.decode_block('Beef')
    assert [97,110,121] == base64.decode_block('YW55')
    assert [115] == base64.decode_block('cw==')
    assert [115,117] == base64.decode_block('c3U=')

def test_base64_decode():
    assert base64.base64_decode('SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t') == base64.hex_decode('49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d')


def test_base64_encode():
    assert 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t' == base64.base64_encode(base64.hex_decode('49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'))

def test_fixed_xor():
    assert base64.hex_decode('746865206b696420646f6e277420706c6179') == xor.xor(base64.hex_decode('1c0111001f010100061a024b53535009181c'), base64.hex_decode('686974207468652062756c6c277320657965'))

def test_repeating_key_xor():
    cleartext = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"

    a = xor.xor_encrypt(map(ord, cleartext), map(ord, "ICE"))
    b = base64.hex_decode('0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f')
    assert a == b
