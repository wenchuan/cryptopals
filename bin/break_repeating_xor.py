#!/usr/bin/python
#
# http://cryptopals.com/sets/1/challenges/6/

import requests
from cryptopals import base64, bits, english

url = 'http://cryptopals.com/static/challenge-data/6.txt'
raw_text = requests.get(url).text.replace('\n','')
ciphertext = base64.base64_decode(raw_text)

def calculate_normalized_hamming_distance(keysize):
    num_blocks = 4
    accu = 0
    for i in xrange(num_blocks):
        accu += bits.hamming_distance(ciphertext[i*keysize:(i+1)*keysize], ciphertext[(i+1)*keysize:(i+2)*keysize])
    return accu / float(num_blocks * keysize)

def guess_keysize():
    normalized_hamming_distance_by_keysize = [(calculate_normalized_hamming_distance(keysize), keysize) for keysize in xrange(2, 50)]
    normalized_hamming_distance_by_keysize.sort()
    return [c for _, c in normalized_hamming_distance_by_keysize[:5]]

def break_one_byte_xor_cipher(s):
    """return a list of five most probable key"""
    scores = [(english.score(bits.xor(s, [x] * len(s))), x) for x in xrange(256)]
    scores.sort(reverse=True)
    return scores[0][1]

def break_cipher(keysize):
    """given keysize, break each block for each byte of the key"""
    key = [break_one_byte_xor_cipher(ciphertext[i::keysize]) for i in xrange(keysize)]
    cleartext = bits.xor_encrypt(ciphertext, key)
    return english.score(cleartext), key

if __name__ == '__main__':
    scores = [break_cipher(keysize) for keysize in guess_keysize()]
    scores.sort(reverse=True)

    key = scores[0][1]
    cleartext = bits.xor_encrypt(ciphertext, key)

    print ''.join(map(chr, key))
    print ''.join(map(chr, cleartext))
