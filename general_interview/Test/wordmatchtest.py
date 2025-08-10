import pytest
from general_interview import wordmatch

@pytest.fixture
def solution():
    return wordmatch()

def test_wordPattern_true(solution):
    pattern = "abba"
    s = "dog cat cat dog"
    assert solution.wordPattern(pattern, s) == True

def test_wordPattern_false(solution):
    pattern = "abba"
    s = "dog cat cat fish"
    assert solution.wordPattern(pattern, s) == False

def test_wordPattern_different_lengths(solution):
    pattern = "abba"
    s = "dog cat cat"
    assert solution.wordPattern(pattern, s) == False

def test_wordPattern_empty_string(solution):
    pattern = ""
    s = ""
    assert solution.wordPattern(pattern, s) == True

def test_wordPattern_single_character(solution):
    pattern = "a"
    s = "apple"
    assert solution.wordPattern(pattern, s) == True
