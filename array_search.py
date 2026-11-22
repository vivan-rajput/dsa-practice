"""Search patterns for integer arrays."""

from typing import Optional, Sequence, Tuple


def first_occurrence(values: Sequence[int], target: int) -> Optional[int]:
    """Find the first index of target in ascending order, or return None."""
    left, right = 0, len(values)
    while left < right:
        middle = (left + right) // 2
        if values[middle] < target:
            left = middle + 1
        else:
            right = middle
    if left < len(values) and values[left] == target:
        return left
    return None


def two_sum(values: Sequence[int], target: int) -> Optional[Tuple[int, int]]:
    """Return distinct indices adding to target, or None if no pair exists."""
    first_index = {}
    for index, value in enumerate(values):
        complement = target - value
        if complement in first_index:
            return first_index[complement], index
        first_index.setdefault(value, index)
    return None
