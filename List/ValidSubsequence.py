# Approach 1: Two-pointer technique(Time Complexity: O(n), Space Complexity: O(1))
# -------------------------------
# We use two pointers: one for the main array and one for the sequence.
# We iterate through the array and move the sequence pointer only when there's a match.
# If the sequence pointer reaches the end, it means all elements were found in order.

def isValidSubsequence_TwoPointers(array, sequence):
    arrIdx = 0  # Pointer for array
    seqIdx = 0  # Pointer for sequence

    # Iterate while both pointers are in bounds
    while arrIdx < len(array) and seqIdx < len(sequence):
        # If elements match, move the sequence pointer forward
        if array[arrIdx] == sequence[seqIdx]:
            seqIdx += 1
        # Always move the array pointer forward
        arrIdx += 1

    # If seqIdx has reached the end of the sequence, it's a valid subsequence
    return seqIdx == len(sequence)


# Approach 2: Single loop (more Pythonic)(Time Complexity: O(n), Space Complexity: O(1))
# -------------------------------
# We loop through the array and compare each value to the current sequence element.
# If matched, move the sequence pointer.
# If all sequence elements are matched by the end of the loop, it's a valid subsequence.

def isValidSubsequence_ForLoop(array, sequence):
    seqIdx = 0  # Pointer for sequence

    for value in array:
        # Early exit: if all elements in the sequence are matched
        if seqIdx == len(sequence):
            break

        # Match found, move to next sequence element
        if sequence[seqIdx] == value:
            seqIdx += 1

    # If all sequence elements were matched in order
    return seqIdx == len(sequence)


# Example usage:
if __name__ == "__main__":
    array = [5, 1, 22, 25, 6, -1, 8, 10]
    sequence = [1, 6, -1, 10]

    print("Two-Pointer Approach:", isValidSubsequence_TwoPointers(array, sequence))
    print("For-Loop Approach:", isValidSubsequence_ForLoop(array, sequence))
