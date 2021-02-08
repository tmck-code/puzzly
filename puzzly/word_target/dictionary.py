from itertools import permutations
from pkg_resources import resource_string
import sys

def load(word_len=9):
    istream = resource_string('puzzly', 'data/words_alpha.txt').decode().split('\n')
    return set(filter(lambda x: len(x) == word_len, map(str.strip, istream)))

def solve(word, dictionary):
    for p in set(map(''.join, permutations(word, len(word)))):
        if p in dictionary:
            yield p

def main():
    d = load(len(sys.argv[1]))
    print(list(solve(sys.argv[1], d)))
