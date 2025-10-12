"""Description
You are given an integer array heights where heights[i] represents the height of the i^th bar.

You may choose any two bars to form a container. Return the maximum amount of water a container can store.

Example 1:

Input: height = [1,7,2,5,4,7,3,6]

Output: 36
Example 2:

Input: height = [2,2,2]

Output: 4
Constraints:

2 <= height.length <= 1000
0 <= height[i] <= 1000
"""



"""
Brute Force:
We have to calculate the area.So, For that we must find the two bar which will the most water in it.We can do this using two loops for each pair which one can store the most water in it.
"""

"""
🟩 Positional Argument: passed by order → range(1, 10)
🟦 Keyword Argument: passed by name → range(start=1, stop=10)
⚠️ Rule: Positional must come before keyword
✅ Python syntax: range(i+1, len(height)) (no = inside)
"""
class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea=0
        for i in range(0,len(height)):
            for j in range(i+1,len(height)):
                area=min(height[i],height[j])*(j-i)
                if area > maxArea:
                    maxArea=area

        return maxArea
        

"""
Optimal Solution (Two Pointer):
we will keep our first pointer at the beginning and our second pointer at the very end of the array because we want our width of the graph to be maximum so that the area will be maximum.So, Now we will look which pointer is smaller and move that pointer only and check now the area is maximum or not and update that accordingly.
"""

class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea=0
        l=0
        r=len(height)-1
        while l<r:
            area=min(height[l],height[r])*(r-l)
            if area>maxArea:
                maxArea=area
            
            if height[l]>height[r]:
                r=r-1
            else:
                l=l+1
        return maxArea

        """
### 🧩 Python `len()` and `range()`

* `len(list)` → total elements, last index = `len(list)-1`
* `range(start, stop)` → includes `start`, **excludes `stop`**
* ✅ Loop all indices safely:

```python
for i in range(len(list)):  # 0 to len(list)-1
    ...
```
* ❌ Using `len(list)-1` → skips last element
* 💡 Python avoids “index out of bounds” automatically because `range` never reaches `stop`.
        """