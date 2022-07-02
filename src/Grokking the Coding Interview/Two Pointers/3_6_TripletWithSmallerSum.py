# Given an array arr of unsorted numbers and a target sum, count all triplets in it such that arr[i] + arr[j] + arr[k] < target where i, j, and k are three different indices. Write a function to return the count of such triplets.

# Example 1:

# Input: [-1, 0, 2, 3], target = 3
# Output: 2
# Explanation: There are two triplets whose sum is less than the target: [-1, 0, 3], [-1, 0, 2]
# Example 2:

# Input: [-1, 4, 2, 1, 3], target = 5
# Output: 4
# Explanation: There are four triplets whose sum is less than the target:
#    [-1, 1, 4], [-1, 1, 3], [-1, 1, 2], [-1, 2, 3]


def triplet_with_smaller_sum(arr, target):
    arr.sort()
    count = 0
    for x in range(len(arr)-2):
        count += search_pair(arr, target - arr[x], x)
    return count


def search_pair(arr, target_sum, start):
    count = 0
    left = start + 1
    right = len(arr) - 1
    while left < right:
        curr_sum = arr[left] + arr[right]
        if curr_sum < target_sum:
            count += right - left
            left += 1
        else:
            right -= 1
    return count


def main():
    print(triplet_with_smaller_sum([-1, 0, 2, 3], 3))
    print(triplet_with_smaller_sum([-1, 4, 2, 1, 3], 5))


if __name__ == "__main__":
    main()
