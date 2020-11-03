import functools
import sys
from time import time
from collections import defaultdict, Counter

d = defaultdict(list)


def timer(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        start_time = time()
        value = f(*args, **kwargs)
        end_time = time()
        dif = end_time - start_time
        print(value.format(dif*1000))
        return value
    return wrapper


@timer
def load_dic(file_name):
    with open(file_name, 'r') as f:
        words = [word.strip() for word in f.readlines()]
        for word in words:
            d[len(word.strip())].append((Counter(word), word))
    return "Welcome to the Anagram Finder\n-----------------------------\nInitialized in {} ms\n"


@timer
def find_anagrams(word):
    anagrams = []
    for c, w in d[len(word)]:
        if c == Counter(word):
            anagrams.append(w)
    if len(anagrams) == 0:
        return f"No anagrams found for {word} in {{}} ms"
    return f"{len(anagrams)} Anagrams found for {word} in {{}} ms\n" + ",".join(anagrams)


def main():
    if len(sys.argv) != 2:
        raise ValueError("Should be exact one argument")
    load_dic(sys.argv[1])

    inp = ''
    while inp != 'exit':
        inp = input("AnagramFinder>").strip()
        if inp != 'exit':
            find_anagrams(inp)


if __name__ == '__main__':
    main()

