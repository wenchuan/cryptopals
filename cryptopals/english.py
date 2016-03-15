#!/usr/bin/python

# https://en.wikipedia.org/wiki/Letter_frequency
LETTER_FREQUENCY = {
    'a':  0.08167,
    'b':  0.01492,
    'c':  0.02782,
    'd':  0.04253,
    'e':  0.12702,
    'f':  0.02228,
    'g':  0.02015,
    'h':  0.06094,
    'i':  0.06966,
    'j':  0.00153,
    'k':  0.00772,
    'l':  0.04025,
    'm':  0.02406,
    'n':  0.06749,
    'o':  0.07507,
    'p':  0.01929,
    'q':  0.00095,
    'r':  0.05987,
    's':  0.06327,
    't':  0.09056,
    'u':  0.02758,
    'v':  0.00978,
    'w':  0.02360,
    'x':  0.00150,
    'y':  0.01974,
    'z':  0.00074
}

SPACE_FREQUENCY = 0.145
OTHER_FREQUENCY = 0.085

def score(s):
    """
    assign a score to byte string s, signifies the likelihood of it being english
    the higehr the score, the more it reads like english
    """
    letters = [chr(c).lower() for c in s if chr(c).isalpha()]
    spaces = [chr(c) for c in s if chr(c).isspace()]

    space_error = abs(len(spaces) / float(len(s)) - SPACE_FREQUENCY)
    other_error = abs((len(s) - len(letters) - len(spaces)) / float(len(s)) - OTHER_FREQUENCY)

    count = dict([(c,0) for c in LETTER_FREQUENCY])
    for c in letters:
        count[c] += 1

    letter_error = sum([abs(LETTER_FREQUENCY[c] - count[c] / float(len(s))) for c in count])

    # lowest score is 0
    return max(0.0, 1.0 - letter_error - space_error - other_error)
