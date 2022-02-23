"""Testing practice using utils.py!"""

__author__ = "730490943"

from utils import only_evens, sub, concat


def test_list_empty() -> None:
    """Test edge case when the given list is empty."""
    x: list[int] = []
    assert only_evens(x) == []


def test_only_evens_all_evens() -> None:
    """Test usage case when the given list is composed only of even numbers."""
    x: list[int] = [2, 4, 6, 8, 10]
    assert only_evens(x) == [2, 4, 6, 8, 10]


def test_only_evens_mixed() -> None:
    """Test usage case when the given list is composed of a mix of even and odd numbers."""
    x: list[int] = [1, 2, 3, 4, 5, 6]
    assert only_evens(x) == [2, 4, 6]


def test_sub_empty() -> None:
    """Test edge case when the given list is empty while start_index and end_index are held constant at 1."""
    x: list[int] = list()
    assert sub(x, 1, 1) == []


def test_sub_start_negative() -> None:
    """Test usage case when the given start_index is less than zero.
    
    For the purposes of this test, end_index will be set to 4.
    """
    x: list[int] = [1, 2, 3, 4, 5, 6]
    assert sub(x, -1, 4) == [1, 2, 3, 4]


def test_sub_regular() -> None:
    """Test usage case of sub when the given start and end indices are in conventional parameters."""
    x: list[int] = [1, 2, 3, 4, 5]
    assert sub(x, 1, 3) == [2, 3]


def test_concat_empty() -> None:
    """Test edge case when the both lists given to concat is empty."""
    x: list[int] = []
    y: list[int] = []
    assert concat(x, y) == []


def test_concat_same_length() -> None:
    """Test usage case when the two lists given to concat are different lengths."""
    x: list[int] = [1, 2, 3]
    y: list[int] = [4]
    assert concat(x, y) == [1, 2, 3, 4]


def test_concat_different_length() -> None:
    """Test usage case when the two lists given to concat are the same length."""
    x: list[int] = [1, 2, 3]
    y: list[int] = [4, 5, 6]
    assert concat(x, y) == [1, 2, 3, 4, 5, 6]
