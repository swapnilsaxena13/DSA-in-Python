"""
Problem: Find the Town Judge

A town judge has two properties:
1. The judge trusts nobody.
2. Everybody else trusts the judge.

If there are n people labeled 1 to n and a list trust where
[a, b] means person 'a' trusts person 'b', we must find the judge.

Approach (Using Incoming and Outgoing Counts)

Key Idea:
---------
We treat the trust relationships like a directed graph.

a -> b means:
a trusts b

So:
- 'a' has an outgoing edge
- 'b' has an incoming edge

The judge must satisfy:
1. outgoing[judge] = 0      (judge trusts nobody)
2. incoming[judge] = n - 1  (everyone else trusts the judge)

Steps:
------

1. Create two dictionaries:
   incoming[i] → number of people who trust person i
   outgoing[i] → number of people person i trusts

2. Traverse the trust list:
   If a trusts b:
       outgoing[a] += 1
       incoming[b] += 1

3. Check each person from 1 → n:
   If:
       outgoing[i] == 0
       AND
       incoming[i] == n - 1
   Then i is the judge.

4. If no such person exists, return -1.

Time Complexity:
----------------
O(n + t)
n = number of people
t = number of trust relationships

Space Complexity:
-----------------
O(n)

Python Implementation:
----------------------
"""

from collections import defaultdict

class Solution:
    def findJudge(self, n, trust):
        incoming = defaultdict(int)
        outgoing = defaultdict(int)

        # Count incoming and outgoing trusts
        for a, b in trust:
            outgoing[a] += 1
            incoming[b] += 1

        # Find the judge
        for i in range(1, n + 1):
            if outgoing[i] == 0 and incoming[i] == n - 1:
                return i

        return -1