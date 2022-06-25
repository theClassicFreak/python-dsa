# Given an array of sorted numbers, remove all duplicates from it. You should not use any extra space
# after removing the duplicates in -place return the new length of the array.

# Example 1:

# Input: [2, 3, 3, 3, 6, 9, 9]
# Output: 4
# Explanation: The first four elements after removing the duplicates will be[2, 3, 6, 9].
# Example 2:

# Input: [2, 2, 2, 11]
# Output: 2
# Explanation: The first two elements after removing the duplicates will be[2, 11].


def remove_duplicates(arr):
    left = 1  # non duplicate tracker
    right = 0  # iterator
    for right in range(len(arr)):
        if arr[left-1] != arr[right]:
            arr[left] = arr[right]
            left += 1
    return left


def main():
    print(remove_duplicates([2, 3, 3, 3, 6, 9, 9]))
    print(remove_duplicates([2, 2, 2, 11]))
    print(remove_duplicates([3, 3]))
    print(remove_duplicates([1]))


if __name__ == "__main__":
    main()
