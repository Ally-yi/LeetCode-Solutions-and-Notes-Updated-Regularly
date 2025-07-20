# Regular Expression Matching (LeetCode #10)

**Problem Link:** [https://leetcode.com/problems/regular-expression-matching/](https://leetcode.com/problems/regular-expression-matching/)

---



## Basic Regex Usage Summary (with Python Examples)

### 1. Basic Character Matching

* Matches the exact characters as is.
* Example:

  ```python
  import re
  print(re.match(r'abc', 'abc'))    # Matches, output: <re.Match object; span=(0, 3), match='abc'>
  print(re.match(r'abc', 'ab'))     # No match, output: None
  ```

### 2. `.` — Matches Any Single Character

* Matches exactly one arbitrary character except newline.
* Example:

  ```python
  print(re.match(r'a.c', 'abc'))    # Matches 'abc'
  print(re.match(r'a.c', 'axc'))    # Matches 'axc'
  print(re.match(r'a.c', 'ac'))     # No match (missing one char)
  print(re.match(r'a.c', 'abbc'))   # No match (too many chars)
  ```

### 3. `*` — Matches Zero or More of the Preceding Character

* Matches zero or more repetitions of the character before `*`.
* Examples:

  ```python
  print(re.match(r'a*', ''))        # Matches empty string
  print(re.match(r'a*', 'aaa'))     # Matches 'aaa'
  print(re.match(r'ab*c', 'ac'))    # Matches 'ac' (b occurs zero times)
  print(re.match(r'ab*c', 'abc'))   # Matches 'abc'
  print(re.match(r'ab*c', 'abbbc')) # Matches 'abbbc'
  ```

### 4. `^` and `$` — Start and End Anchors

* `^` matches the start of the string.
* `$` matches the end of the string.
* Used to ensure the entire string matches the pattern.
* Examples:

  ```python
  print(re.match(r'^abc$', 'abc'))      # Matches exactly 'abc'
  print(re.match(r'^abc$', 'abcd'))     # No match (extra characters)
  print(re.match(r'^a.*b$', 'axyzb'))   # Matches 'axyzb'
  print(re.match(r'^a.*b$', 'cab'))     # No match (does not start with 'a')
  ```

---

## More Regex Features (with Examples)

### 5. `+` — One or More of the Preceding Character

* Like `*` but requires at least one occurrence.
* Example:

  ```python
  print(re.match(r'a+', ''))       # No match (need at least one 'a')
  print(re.match(r'a+', 'aaa'))    # Matches 'aaa'
  print(re.match(r'a+', 'b'))      # No match
  ```

### 6. `?` — Zero or One of the Preceding Character (Optional)

* Makes the previous character optional.
* Example:

  ```python
  print(re.match(r'ab?c', 'ac'))   # Matches 'ac' (b is optional)
  print(re.match(r'ab?c', 'abc'))  # Matches 'abc'
  print(re.match(r'ab?c', 'abbc')) # No match (extra b)
  ```

### 7. `{n,m}` — Specify Repetition Range

* Matches between n and m occurrences of the preceding character.
* Example:

  ```python
  print(re.match(r'a{2,4}', 'a'))       # No match (less than 2)
  print(re.match(r'a{2,4}', 'aaa'))     # Matches 'aaa' (3 times)
  print(re.match(r'a{2,4}', 'aaaaa'))   # Matches 'aaaa' (max 4 times)
  ```

### 8. `[]` — Character Classes

* Matches any one character inside the brackets.
* Example:

  ```python
  print(re.match(r'[abc]', 'a'))   # Matches 'a'
  print(re.match(r'[abc]', 'd'))   # No match
  print(re.match(r'[a-z]', 'm'))   # Matches 'm' (lowercase letter)
  ```

### 9. Predefined Character Classes

* `\d` — digit `[0-9]`
* `\w` — word character `[a-zA-Z0-9_]`
* `\s` — whitespace (space, tab, newline, etc.)
* Example:

  ```python
  print(re.match(r'\d+', '123abc'))   # Matches '123'
  print(re.match(r'\w+', '_abc123'))  # Matches '_abc123'
  print(re.match(r'\s+', '   \t\n'))  # Matches whitespace
  ```

### 10. Grouping and Capturing `()`

* Groups parts of regex and captures matched substrings.
* Example:

  ```python
  m = re.match(r'(\w+)@(\w+)\.(\w+)', 'test@example.com')
  if m:
      print(m.group(0))  # Whole match: 'test@example.com'
      print(m.group(1))  # First group: 'test'
      print(m.group(2))  # Second group: 'example'
      print(m.group(3))  # Third group: 'com'
  ```

### 11. Non-capturing Group `(?:...)`

* Groups without capturing, useful for grouping without storing matches.
* Example:

  ```python
  print(re.match(r'(?:ab)+', 'abab'))   # Matches 'abab'
  ```

### 12. Alternation `|`

* Matches either the expression before or after `|`.
* Example:

  ```python
  print(re.match(r'cat|dog', 'dog'))   # Matches 'dog'
  print(re.match(r'cat|dog', 'cat'))   # Matches 'cat'
  print(re.match(r'cat|dog', 'cow'))   # No match
  ```

### 13. Word Boundary `\b`

* Matches position between word and non-word characters.
* Example:

  ```python
  import re
  print(re.search(r'\bcat\b', 'a cat in the hat'))  # Matches 'cat'
  print(re.search(r'\bcat\b', 'catalog'))           # No match
  ```

---

## Combined Pattern Example (LeetCode #10 pattern)

```python
import re

pattern = r'^mis*is*p*.$'
test_str = "mississippi"
print(re.match(pattern, test_str) is not None)  # Output: True
```

* Explanation:

  * `s*` matches zero or more 's'
  * `p*` matches zero or more 'p'
  * `.` matches any single character

---

## References

* [Python `re` Module Documentation](https://docs.python.org/3/library/re.html)
