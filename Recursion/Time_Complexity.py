"""
Perfect — this is a **key skill** for mastering recursion and algorithm analysis.
Let’s build your understanding **from beginner → intermediate → expert**, step by step.
By the end, you’ll be able to calculate **any recursion’s time complexity** confidently.

---

## 🧩 1. Beginner Level — What Is Time Complexity?

**Definition:**
Time complexity measures **how the number of operations grows** as the input size `n` increases.

In recursion, this growth depends on:

* **How many recursive calls** happen, and
* **How much work** each call does besides recursion.

---

## 🪜 2. Basic Rule for Recursion Time Complexity

Almost all recursive problems can be described by a **recurrence relation**:

```
T(n) = a*T(n/b) + f(n)
```

Where:

* `a` → number of recursive calls
* `n/b` → size of each subproblem
* `f(n)` → non-recursive work per call (like swaps, loops, comparisons, etc.)

Your goal: find the **Big-O** of `T(n)`.

---

## 🧮 3. Step-by-Step Examples

### 🧠 Example 1: Simple recursion

```python
def f(n):
    if n <= 1:
        return
    f(n-1)
```

* Only **one recursive call** each time (`a=1`)
* Subproblem size reduces by 1 (`b ≈ 1`)
* Constant work per call (`f(n)=O(1)`)

So:

```
T(n) = T(n-1) + O(1)
```

Expanding:

```
T(n) = T(n-2) + O(1) + O(1)
T(n) = ... = O(n)
```

✅ **Time complexity = O(n)**

---

### 🧠 Example 2: Two recursive calls (Binary Tree recursion)

```python
def f(root):
    if not root:
        return
    f(root.left)
    f(root.right)
```

Here:

* `a = 2` (two recursive calls)
* Subproblem sizes together cover all `n` nodes once
* Constant work per node

So:

```
T(n) = 2*T(n/2) + O(1)
```

Using the **Master Theorem** (we’ll cover below),
✅ **T(n) = O(n)** — because total nodes = n, each visited once.

---

### 🧠 Example 3: Binary Search

```python
def binary_search(arr, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, low, mid-1)
    else:
        return binary_search(arr, mid+1, high)
```

Here:

* `a = 1` (one recursive call)
* Each time problem size halves (`n/2`)
* Constant work per call (`O(1)`)

So:

```
T(n) = T(n/2) + O(1)
```

Expanding gives logarithmic growth:
✅ **T(n) = O(log n)**

---

## ⚙️ 4. Master Theorem (Your Main Weapon)

Used to solve recurrences of the form:

```
T(n) = a*T(n/b) + f(n)
```

### Compare `f(n)` with `n^(log_b a)`:

| Case | Condition            | Time Complexity                 |
| ---- | -------------------- | ------------------------------- |
| 1️⃣  | `f(n)` grows slower  | `T(n) = O(n^(log_b a))`         |
| 2️⃣  | `f(n)` grows equally | `T(n) = O(n^(log_b a) * log n)` |
| 3️⃣  | `f(n)` grows faster  | `T(n) = O(f(n))`                |

---

### 💡 Example — Merge Sort

```
T(n) = 2*T(n/2) + O(n)
```

* `a = 2`, `b = 2`, so `n^(log_b a) = n^(log_2 2) = n^1`
* `f(n) = O(n)` → same as `n^(log_b a)`

✅ Case 2 → `O(n log n)`

---

## 🧩 5. Counting Actual Work (Tree Method)

For recursion that divides work (like merge sort, tree traversals):

Imagine a **recursion tree**, where:

* Each node = one function call
* Each level = work done per recursion depth

Example:

```
T(n) = 2*T(n/2) + O(n)
```

| Level | # of calls | Work per call | Total work per level |
| ----- | ---------- | ------------- | -------------------- |
| 0     | 1          | O(n)          | O(n)                 |
| 1     | 2          | O(n/2)        | O(n)                 |
| 2     | 4          | O(n/4)        | O(n)                 |
| ...   | ...        | ...           | ...                  |

Total work across log n levels = `O(n log n)`.

---

## 🚀 6. Advanced Patterns

### 🧠 Case 1: Tree Traversal (DFS, BFS)

* Each node visited once → **O(n)**
* Stack/queue adds at most one per node → **O(n)** space

### 🧠 Case 2: Divide & Conquer (Merge Sort, Quick Sort)

* Break into smaller subproblems → use Master Theorem
* Merge Sort → `O(n log n)`
* Quick Sort → `O(n log n)` avg, `O(n²)` worst

### 🧠 Case 3: Exponential Recursion (Fibonacci)

```python
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
```

Each call spawns 2 new calls → forms a binary recursion tree.

So:

```
T(n) = T(n-1) + T(n-2) + O(1)
```

Roughly doubles every level → **O(2^n)**

---

## 🔍 7. Tips to Analyze Any Recursive Function

1. **Count recursive calls.**
   → That’s your “a”.

2. **See how input size changes.**
   → That’s your “b”.

3. **Note constant work per call.**
   → That’s your `f(n)`.

4. **Form recurrence:** `T(n) = a*T(n/b) + f(n)`
   → Solve via **Master Theorem** or **Recursion Tree**.

---

## 🧠 8. Quick Reference Chart

| Type of Recursion                  | Example                | Time Complexity                    |
| ---------------------------------- | ---------------------- | ---------------------------------- |
| Linear                             | Factorial, Linked list | O(n)                               |
| Divide by 2                        | Binary Search          | O(log n)                           |
| Two-way (full tree)                | Invert Tree, DFS       | O(n)                               |
| Divide & Conquer (merge + combine) | Merge Sort             | O(n log n)                         |
| Exponential                        | Fibonacci              | O(2^n)                             |
| K-way recursion                    | N-ary Tree traversal   | O(n) (if all nodes processed once) |

---

## 🏁 9. Apply to Your Example (Invert Tree)

```python
T(n) = 2*T(n/2) + O(1)
```

(2 recursive calls, constant work)

→ Master Theorem ⇒ **O(n)**

---

## ✅ Final Mental Formula (for any recursion)

> **Total Time = (Number of Recursive Calls × Cost per Call) + Cost of Work in Each Call**

and

> **Each unique node or subproblem counted only once = O(n)**
> **Same subproblem repeated many times (like Fibonacci) = Exponential**

---

If you want, I can give you a **practice sheet** with 5 recursion examples (easy → hard) where you calculate time complexity step by step — would you like that?
"""