# DSA practice

Short Python exercises with worked examples, edge-case tests, and complexity notes. The solutions use only the Python standard library.

## Array search

| Function | Example | Approach | Time | Extra space |
| --- | --- | --- | --- | --- |
| `first_occurrence` | `([1, 4, 4, 9], 4) → 1` | Binary search on a sorted array | O(log n) | O(1) |
| `two_sum` | `([-3, 7, 1], 4) → (0, 1)` | Hash table of earlier indices | O(n) average | O(n) |

In `first_occurrence`, a matching midpoint moves the right boundary leftward. This keeps earlier duplicates in play. In `two_sum`, the lookup happens before insertion so the same index cannot be used twice. Both functions return `None` when there is no match.

## Run the examples

```python
from array_search import first_occurrence, two_sum

print(first_occurrence([1, 4, 4, 9], 4))  # 1
print(two_sum([-3, 7, 1], 4))            # (0, 1)
```

## Run the tests

```sh
python3 -m unittest discover -v
```
