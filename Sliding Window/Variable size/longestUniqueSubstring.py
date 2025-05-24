# longest_unique_substring.py

"""
Problem: Find the length of the longest substring without repeating characters.

Approach: Sliding Window using Set
---------------------------------------------------------
- Use two pointers `left` and `right` to form a sliding window.
- Expand `right` to include new characters if not seen before.
- If a character is repeated, shrink the window from the `left` side
  until the duplicate is removed.
- Use a set to track unique characters in the current window.
- Track the max length during this process.

Why this works:
- This ensures all substrings checked are unique.
- The window only contains non-repeating characters at any point.
"""
#Time Complexity: O(n)

def lengthOfLongestSubstring(s: str) -> int:
    # Edge case: Empty string
    if not s:
        return 0

    left = 0
    max_length = 0
    seen_chars = set()

    for right in range(len(s)):
        # If duplicate found, move left pointer and remove from set
        while s[right] in seen_chars:
            seen_chars.remove(s[left])
            left += 1
        # Add current char to the set
        seen_chars.add(s[right])
        # Update max length
        max_length = max(max_length, right - left + 1)

    return max_length


# Sample test cases to run the code
if __name__ == "__main__":
    test_input = "pwwkew"
    print(f"Input: {test_input}")
    result = lengthOfLongestSubstring(test_input)
    print(f"Output: {result}")  # Expected Output: 3


"""
----------------------------------------
Mistakes in your original solution:
----------------------------------------

1. Wrong use of set:
   - You used: max_s.add(s[left:right+1]) → This adds a whole substring.
   - Correct: max_s.add(s[right]) → Only add a single character.

2. Incorrect substring length:
   - You used: len(s[left:right]) → Excludes s[right].
   - Correct: right - left + 1 → Includes both ends of the window.

3. Not handling empty string:
   - Your code assumes s is non-empty and does max_s.add(s[0]), which crashes for "".
   - Correct: Check with `if not s: return 0`.

4. Not removing elements from set:
   - You moved the `left` pointer ahead but did not remove `s[left]` from the set.
   - This kept duplicates in the set and broke the logic.

By fixing these, the code now correctly computes the length of the longest substring without repeating characters.
"""
