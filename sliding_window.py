"""Sliding windows over strings and integer arrays."""

from typing import Sequence


def longest_unique_length(text: str) -> int:
    """Return the length of the longest substring without repeated characters."""
    last_seen = {}
    left = best = 0
    for right, char in enumerate(text):
        if char in last_seen:
            left = max(left, last_seen[char] + 1)
        last_seen[char] = right
        best = max(best, right - left + 1)
    return best


def max_window_sum(values: Sequence[int], width: int) -> int:
    """Find the largest sum of exactly width consecutive values."""
    if not 1 <= width <= len(values):
        raise ValueError("width must be between 1 and the length of values")
    current = sum(values[i] for i in range(width))
    best = current
    for right in range(width, len(values)):
        current += values[right] - values[right - width]
        best = max(best, current)
    return best
