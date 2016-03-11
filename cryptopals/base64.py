#!/usr/bin/python

sexect_to_base64 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
base64_to_sexect = dict([(sexect_to_base64[i], i) for i in xrange(len(sexect_to_base64))])

dec_to_chr = '0123456789abcdef'
chr_to_dec = dict([(dec_to_chr[i], i) for i in xrange(len(dec_to_chr))])

def base64_encode(s):
    b = hexstring_to_bytes(s)
    return ''.join([encode_block(b[i:i+3]) for i in range(len(b))[::3]])

def hexstring_to_bytes(s):
    return [chr_to_dec[a] * 16 + chr_to_dec[b] for a,b in zip(s[::2],s[1::2])]

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
