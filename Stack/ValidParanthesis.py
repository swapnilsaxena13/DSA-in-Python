
"""
 Every time we encounter an opening bracket ((, [, {), we push it onto the stack. When a closing bracket (), ], }) appears, we first check if the stack is empty — if it is, that means there’s no matching opening bracket, so the string is invalid. If the stack isn’t empty, we compare the closing bracket with the one on top of the stack using a dictionary that maps opening to closing brackets. If they don’t match, we return false. After the entire string is processed, if the stack is empty, it means all brackets were properly closed and nested — hence, the string is valid.
"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        # Sets of opening and closing brackets
        open = {'(', '[', '{'}
        close = {')', ']', '}'}
        
        # Dictionary to map opening to corresponding closing bracket
        dic = {'(': ')', '[': ']', '{': '}'}

        # Stack to track unmatched opening brackets
        stack = []

        for i in s:
            if i in open:
                # Push opening brackets onto the stack
                stack.append(i)
            elif i in close:
                # Check 1: if stack is empty → no match for closing bracket
                # Check 2: if top of stack doesn't match current closing bracket
                if not stack or dic[stack[-1]] != i:
                    return False
                else:
                    # If it matches, pop the opening bracket
                    stack.pop()

        # If stack is empty at the end, all brackets matched correctly
        return len(stack) == 0

# -------------------------
# 🧪 Test the Code Below
# -------------------------

sol = Solution()
test_cases = [
    ("()", True),
    ("()[]{}", True),
    ("(]", False),
    ("([)]", False),
    ("{[]}", True),
    ("(((", False),
    ("]", False),
    ("", True)
]

for s, expected in test_cases:
    result = sol.isValid(s)
    print(f"isValid('{s}') ➞ {result} (Expected: {expected})")
