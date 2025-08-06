# Top K Frequent Elements (LeetCode \#347)

**Problem Link:** [https://leetcode.com/problems/top-k-frequent-elements/](https://leetcode.com/problems/top-k-frequent-elements/)

-----

## Solution Idea: Hash Map and Sorting


1.  **Frequency Counting:** We need to find out how many times each unique number appears in the input array `nums`. A **hash map (dictionary)** is the perfect data structure for this task. We can iterate through `nums` and store each number as a key and its count as the value. For example, `[1, 1, 1, 2, 2, 3]` would become `{1: 3, 2: 2, 3: 1}`.

2.  **Sorting:** After counting, we have a list of (number, frequency) pairs. The next step is to sort these pairs. The sorting key must be the **frequency**, and we need to sort in **descending order** to get the most frequent elements first. The result of this step would be `[(1, 3), (2, 2), (3, 1)]`.

3.  **Extracting the Top K:** The final step is to take the first `k` elements from the sorted list and extract just the numbers (the keys of our hash map). If `k=2`, we would take `(1, 3)` and `(2, 2)` and return `[1, 2]`.



## Code 

```python
from collections import Counter
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        
        counts = Counter(nums)

        sorted_counts = sorted(counts.items(), key=lambda item: item[1], reverse=True)

        result = [item[0] for item in sorted_counts[:k]]

        return result
```

## Method-by-Method Analysis

#### `collections.Counter`

  * **Purpose:** This is a highly efficient subclass of a dictionary designed specifically for counting hashable objects.
  * **How it works:** When initialized with an iterable (like our `nums` list), it automatically counts the occurrences of each element and stores them in a dictionary-like object.
  * **Code line:** `counts = Counter(nums)`
  * **Example:** For `nums = [1, 1, 1, 2, 2, 3]`, `counts` becomes `Counter({1: 3, 2: 2, 3: 1})`. This is the most efficient way to perform the frequency counting step.

#### `dict.items()`

  * **Purpose:** This method returns a view object that displays a list of a dictionary's key-value tuple pairs `(key, value)`.
  * **Code line:** `counts.items()`
  * **Example:** For our `counts` dictionary, `counts.items()` returns a view that looks like `dict_items([(1, 3), (2, 2), (3, 1)])`. We need this list of tuples to perform the sorting.

#### `sorted()`

  * **Purpose:** This is a built-in Python function that returns a new sorted list from the items in an iterable.
  * **Parameters:**
      * `iterable`: The list of tuples from `counts.items()`.
      * `key`: This is a crucial argument. It's a function that gets called on each element before making comparisons. We want to sort by frequency, which is the **second element** in each tuple. The **`lambda`** function `lambda item: item[1]` specifies this.
      * `reverse`: This boolean argument controls the sorting order. We set it to `True` for a **descending sort**, ensuring the highest frequencies are at the beginning of the list.
  * **Code line:** `sorted_counts = sorted(counts.items(), key=lambda item: item[1], reverse=True)`
  * **Result:** `sorted_counts` becomes `[(1, 3), (2, 2), (3, 1)]`.

#### List Slicing (`[:k]`) and List Comprehension

  * **Purpose:** These are Pythonic ways to efficiently extract and transform data from a list.
  * **`sorted_counts[:k]`:** This is **list slicing**. It creates a new list containing the first `k` elements of `sorted_counts`. For `k=2`, it returns `[(1, 3), (2, 2)]`.
  * **`[item[0] for item in ...]`:** This is a **list comprehension**. It's a compact way to create a new list by iterating through an existing one. We iterate through `sorted_counts[:k]` and, for each tuple `item`, we extract the first element (`item[0]`), which is the number.
  * **Code line:** `result = [item[0] for item in sorted_counts[:k]]`
  * **Result:** `result` becomes `[1, 2]`.

#### `clambdar`

  * `lambda item: item[1]` is an anonymous, single-expression function.
  * `item` is the argument (in our case, a tuple like `(1, 3)`).
  * `item[1]` is the return value (in our case, the frequency `3`).
