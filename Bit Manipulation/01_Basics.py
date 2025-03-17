### **Binary to Decimal & Decimal to Binary Conversion (Lecture Notes)**  
"""
#### **1. Most Significant Bit (MSB)**  
- **MSB = 0** → Positive number  
- **MSB = 1** → Negative number (stored in **2’s complement** form)  

#### **2. Decimal to Binary Conversion**  
- If **positive**: Convert to binary normally and fit into required bits.  
- If **negative**:  
  1. Convert magnitude to binary.  
  2. Take **2’s complement** (invert bits + add 1).  
  3. Fit into required bits.  

#### **3. Binary to Decimal Conversion**  
- If **MSB = 0**, directly convert to decimal.  
- If **MSB = 1**, apply **2’s complement** to get the negative decimal value.  



### **Bitwise Operators - Power Concept**  

In bitwise operations, **0 and 1 hold different power roles** depending on the operator used. Here's how:  

---

### **1. Bitwise AND (`&`) - 0 is Powerful, 1 is Powerless**  
- `0` **dominates** because `A & 0 = 0` (forcefully turns OFF a bit).  
- `1` **is powerless** because `A & 1 = A` (keeps the bit unchanged).  
- **Example:**  
  ```
  1101
  &1011
  -----
  1001  (Result)
  ```
- **Concept:** AND only returns `1` if both inputs are `1`, otherwise, the `0` overpowers and forces the result to `0`.

---

### **2. Bitwise OR (`|`) - 0 is Powerless, 1 is Powerful**  
- `0` **is powerless** because `A | 0 = A` (does not change the bit).  
- `1` **is powerful** because `A | 1 = 1` (forcefully turns ON a bit).  
- **Example:**  
  ```
  1101
  |1011
  -----
  1111  (Result)
  ```
- **Concept:** OR ensures that as long as **one of the bits is 1**, the result will always be `1`.

---

### **3. Bitwise XOR (`^`) - 1 Toggles, 0 is Powerless**  
- `0` **is powerless** because `A ^ 0 = A` (bit remains unchanged).  
- `1` **toggles the bit** because `A ^ 1 = Inverted(A)`.  
- **Example:**  
  ```
  1101
  ^1011
  -----
  0110  (Result)
  ```
- **Concept:** XOR is useful for **toggling bits**, as `1` in XOR acts like a switch.

---

### **4. Bitwise NOT (`~`) - Inverts All Bits**  
- Every `0` becomes `1`, and every `1` becomes `0`.  
- **Example (8-bit representation):**  
  ```
  A  = 00001100  (12 in decimal)
  ~A = 11110011  (-13 in decimal, using 2’s complement)
  ```

---

### **5. Left & Right Shift Operators**
- **Left Shift (`<<`)**: Moves bits **left**, filling with `0s`, effectively multiplying by `2^n`.  
- **Right Shift (`>>`)**: Moves bits **right**, dividing by `2^n`, filling with `0s` or `1s` (sign extension).  
- **Unsigned Right Shift (`>>>`)** (Java, JS): Moves right but always fills with `0s`.  

---

### **Key Takeaways:**  
- **AND (`&`) → 0 dominates (forces OFF), 1 is weak**  
- **OR (`|`) → 1 dominates (forces ON), 0 is weak**  
- **XOR (`^`) → 1 toggles, 0 does nothing**  


Bitwise Operators & Masking - Detailed Notes
What is a Bit Mask?
A bit mask is a binary number used to modify or extract specific bits in another number using bitwise operators.

🔹 A mask is a predefined binary value that interacts with another number via:

AND (&) → Used to clear or check bits.
OR (|) → Used to set bits.
XOR (^) → Used to toggle bits.
1. Turning a Bit ON (Using OR | & Masking)
To set a specific bit to 1, use a mask where:

The target bit is 1
All other bits are 0

Formula: A | Mask

Example:
Turn ON the 4th bit of A = 10100101


A    = 10100101  
Mask = 00001000  (1 at the 4th position)
----------------  
Result = 10101101  
👉 Effect: The 4th bit is now 1.

2. Turning a Bit OFF (Using AND & & NOT ~ & Masking)
To set a specific bit to 0, use a mask where:

The target bit is 0
All other bits are 1

Formula: A & ~Mask

Example:
Turn OFF the 5th bit of A = 10110101


A    = 10110101  
Mask = 00010000  (1 at the 5th position)  
~Mask = 11101111  (Invert mask)  
----------------  
Result = 10100101  
👉 Effect: The 5th bit is now 0.

3. Toggling a Bit (Using XOR ^ & Masking)
To flip a specific bit (1 → 0 or 0 → 1), use a mask where:

The target bit is 1
All other bits are 0

Formula: A ^ Mask

Example:
Toggle the 4th bit of A = 10100101


A    = 10100101  
Mask = 00001000  (1 at the 4th position)
----------------  
Result = 10101101  
👉 Effect: If the bit was 0, it becomes 1, and vice versa.

4. Checking if a Bit is ON or OFF (Using AND & & Masking)
To check if a specific bit is set (1) or not (0), use a mask where:

Formula: A & Mask

Example:
Check if the 3rd bit of A = 10110101 is ON or OFF

A    = 10110101  
Mask = 00000100  (Checking 3rd bit)  
----------------  
Result = 00000100  (Bit is ON)
👉 Effect: The 3rd bit is ON because the result is not 0.



Key Takeaways About Bit Masking
✔ Use OR (|) + Mask to turn ON a bit.
✔ Use AND (&) + NOT (~) + Mask to turn OFF a bit.
✔ Use XOR (^) + Mask to toggle a bit.
✔ Use AND (&) + Mask to check if a bit is set.
✔ Use shifting (<<, >>) for efficient bitwise operations.

Practical Applications of Bit Masking
🔹 Bitwise flags: Store multiple true/false values in a single integer.
🔹 Memory optimization: Store small values efficiently.
🔹 Fast computations: Used in graphics, encryption, network protocols, and game development.
🔹 Checking power of 2: (n & (n-1)) == 0 checks if n is a power of 2.
🔹 Finding the rightmost set bit: n & -n gives the lowest set bit of n.


"""