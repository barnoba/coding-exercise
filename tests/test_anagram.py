import sys
from unittest import mock

import pytest
import anagram_finder


def test_wrong_filename():
    with pytest.raises(FileNotFoundError):
        sys.argv = ["some_name", "some_file"]
        anagram_finder.main()


def test_no_arg():
    with pytest.raises(ValueError):
        sys.argv = ["some_name"]
        anagram_finder.main()


@mock.patch('anagram_finder.d', {1: [({'a': 1}, 'a')]})
def test_find_one_anagram():
    res = anagram_finder.find_anagrams("a")
    assert res.startswith("1 Anagrams found for a in")


@mock.patch('anagram_finder.d', {1: [({'a': 1}, 'a')]})
def test_find_no_anagram():
    res = anagram_finder.find_anagrams("b")
    assert res.startswith("No anagrams found for b in")


def test_load_dic():
    res = anagram_finder.load_dic("dictionary.txt")
    assert len(anagram_finder.d) == 24
    assert res.startswith("Welcome to the Anagram Finder\n-----------------------------\nInitialized in")