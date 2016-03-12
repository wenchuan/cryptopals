#!/usr/bin/python

sexect_to_base64 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
base64_to_sexect = dict([(sexect_to_base64[i], i) for i in xrange(len(sexect_to_base64))])

dec_to_hex = '0123456789abcdef'
hex_to_dec = dict([(dec_to_hex[i], i) for i in xrange(len(dec_to_hex))])

def base64_encode(s):
    """return the base64 encoding of a byte string"""
    b = hex_decode(s)
    return ''.join([encode_block(b[i:i+3]) for i in range(len(b))[::3]])

def hex_decode(s):
    """decode a lowercase hex string to byte string"""
    return [hex_to_dec[a] * 16 + hex_to_dec[b] for a,b in zip(s[::2],s[1::2])]

def hex_encode(s):
    """encode a byte string to a lowercase hex string"""
    return ''.join([dec_to_hex[b/16] + dec_to_hex[b%16] for b in s])

def encode_block(s):
    def encode_helper(x,y,z):
        val = (x << 16) + (y << 8) + z

        d = val % 64
        val /= 64
        c = val % 64
        val /= 64
        b = val % 64
        val /= 64
        a = val % 64

        return ''.join([sexect_to_base64[s] for s in a,b,c,d])

    if len(s) == 1:
        return encode_helper(s[0], 0, 0)[:2] + '=='
    elif len(s) == 2:
        return encode_helper(s[0], s[1], 0)[:3] + '='
    else:
        return encode_helper(s[0], s[1], s[2])
