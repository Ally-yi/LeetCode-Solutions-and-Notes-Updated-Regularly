# Group Anagrams (LeetCode #49)

**Problem Link:** [https://leetcode.com/problems/group-anagrams/](https://leetcode.com/problems/group-anagrams/)

## The Core Idea: Anagrams Share a DNA

Think of anagrams like "eat," "tea," and "ate." They're all different words, but at their heart, they're made of the exact same letters: 'a', 'e', and 't'. If you were to sort these letters, every single one of those words would become "aet."

This sorted version of the word is like its unique "fingerprint" or "DNA." It's an immutable key that tells us which words belong together. This is the whole secret to solving the problem.

Our strategy is to use a **hash map** (a dictionary in Python) to keep track of these groups.

## Solution Approach

1.  **Create a group container:** Start with an empty dictionary. The keys will be the sorted words (our fingerprints), and the values will be lists of the original words.
2.  **Process each word:** Go through every word in the input list.
3.  **Get the fingerprint:** For each word, sort its letters. For example, "tea" becomes "aet."
4.  **Group it:** Use this sorted string ("aet") as the key to find the right list in our dictionary. Then, simply add the original word ("tea") to that list.
5.  **Collect the results:** Once we've gone through every single word, all our anagrams will be neatly organized into lists. We just need to pull all those lists out of the dictionary and return them.

## Code

This Python code puts the plan into action. We use `defaultdict(list)` which is a handy shortcut—it automatically creates an empty list for us if a key doesn't exist yet.

```python
from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # This dictionary will store our grouped anagrams.
        # The key is the sorted word (e.g., "aet"), and the value is a list
        # of the original words that share that key.
        anagrams = defaultdict(list)

        # Loop through every word we're given.
        for word in strs:
            
            # Sort the characters of the word and join them back into a string.
            # This gives us our unique "fingerprint" for all anagrams.
            key = "".join(sorted(word))
            
            # Use the fingerprint to find the right group in our dictionary
            # and append the original word to it.
            anagrams[key].append(word)

        # The result is all the lists of words (the values) from our dictionary.
        return list(anagrams.values())
```
