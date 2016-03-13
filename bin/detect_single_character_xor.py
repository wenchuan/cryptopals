#!/usr/bin/python
#
# http://cryptopals.com/sets/1/challenges/4/

import requests
from cryptopals import base64, bits

r = requests.get('http://cryptopals.com/static/challenge-data/4.txt')

ciphertexts = map(base64.hex_decode, r.text.split())

def decrypt(key, ciphertext):
    return bits.xor(ciphertext, [key] * len(ciphertext))

def score_byte(b):
    c = chr(b)
    if str.isspace(c):
        return 2
    if str.isdigit(c):
        return 1
    if str.isalpha(c):
        return 5
    return 0

def score(text):
    return sum(map(score_byte, text))

def solve():
    scores = [(score(decrypt(k,c)), k, c) for k in xrange(256) for c in ciphertexts]
    scores.sort(reverse=True)
    print 'key | score | cleartext'
    print '----+-------+----------'
    for (s, k, c) in scores[:30]:
        print format(k, '03d'), "|", format(s, '05d'), "|", ''.join(map(chr,decrypt(k,c)))

if __name__ == '__main__':
    solve()
