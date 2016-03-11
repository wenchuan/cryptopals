#!/usr/bin/python
#
# http://cryptopals.com/sets/1/challenges/3/

from cryptopals import base64, xor

ciphertext = base64.hex_decode('1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736')

def decrypt(key):
    return xor.xor(ciphertext, [key] * len(ciphertext))

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
    scores = [(score(decrypt(k)), k) for k in xrange(256)]
    scores.sort(reverse=True)
    print 'key | score | cleartext'
    print '----+-------+----------'
    for (s, key) in scores[:30]:
        print format(key, '03d'), "|", format(s, '05d'), "|", ''.join(map(chr,decrypt(key)))

if __name__ == '__main__':
    print ''.join(map(chr, ciphertext))
    solve()
