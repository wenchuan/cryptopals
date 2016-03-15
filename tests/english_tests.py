#!/usr/bin/python

from cryptopals import english

def test_score():
    s = 'This challenge isnt conceptually hard, but it involves actual error-prone coding. The other challenges in this set are there to bring you up to speed. This one is there to qualify you. If you can do this one, youre probably just fine up to Set 6.'
    print english.score(map(ord, s))
    s = ' For each KEYSIZE, take the first KEYSIZE worth of bytes, and the second KEYSIZE worth of bytes, and find the edit distance between them. Normalize this result by dividing by KEYSIZE.  The KEYSIZE with the smallest normalized edit distance is probably the key. You could proceed perhaps with the smallest 2-3 KEYSIZE values. Or take 4 KEYSIZE blocks instead of 2 and average the distances.  Now that you probably know the KEYSIZE: break the ciphertext into blocks of KEYSIZE length.  Now transpose the blocks: make a block that is the first byte of every block, and a block that is the second byte of every block, and so on. '
    print english.score(map(ord, s))
