n = 6  # Number of elements in the array
arr = [1, 1, 2, 3, 3, 3]
hmp = dict()  # Create an empty dictionary to store frequencies of elements.
    
for i in range(n):  # Loop through each element of the array.
    if arr[i] in hmp.keys():  # Check if the element is already a key in the dictionary.
        hmp[arr[i]] += 1  # If yes, increment its frequency count by 1.
    else:
        hmp[arr[i]] = 1  # If no, add the element to the dictionary with a frequency of 1.
    
for x in hmp:  # Loop through the dictionary to print the frequency of each element.
    print(x, " ", hmp[x])  # Print the element (key) and its frequency (value).
    

arr = [1, 1, 2, 3, 3, 3]
freq_dict = {}

for num in arr:
    freq_dict[num] = freq_dict.get(num, 0) + 1

print(freq_dict)

"""
#### Iteration-wise Breakdown:
| Iteration | `num` | `freq_dict.get(num, 0)` | `freq_dict[num] =` |
|-----------|------|-----------------------|-------------------|
| 1st       | 1    | 0                     | 1                 |
| 2nd       | 1    | 1                     | 2                 |
| 3rd       | 2    | 0                     | 1                 |
| 4th       | 3    | 0                     | 1                 |
| 5th       | 3    | 1                     | 2                 |
| 6th       | 3    | 2                     | 3                 |
Output:
{1: 2, 2: 1, 3: 3}
"""
