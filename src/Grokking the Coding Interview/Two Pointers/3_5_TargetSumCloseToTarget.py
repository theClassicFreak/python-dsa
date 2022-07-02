# Given an array of unsorted numbers and a target number, find a triplet in the array whose sum is as close to the target number as possible, return the sum of the triplet. If there are more than one such triplet, return the sum of the triplet with the smallest sum.

# Example 1:

# Input: [-2, 0, 1, 2], target=2
# Output: 1
# Explanation: The triplet [-2, 1, 2] has the closest sum to the target.
# Example 2:

# Input: [-3, -1, 1, 2], target=1
# Output: 0
# Explanation: The triplet [-3, 1, 2] has the closest sum to the target.
# Example 3:

# Input: [1, 0, 1, 1], target=100
# Output: 3
# Explanation: The triplet [1, 1, 1] has the closest sum to the target.
import math


def triplet_sum_close_to_target(arr, target_sum):
    arr.sort()
    smallest_difference = math.inf
    for i in range(len(arr)):
        left = i + 1
        right = len(arr) - 1
        while(left < right):
            target_diff = target_sum - (arr[i] + arr[left] + arr[right])
            if target_diff == 0:
                return target_sum - target_diff
            if abs(target_diff) < abs(smallest_difference) or (abs(target_diff) == abs(smallest_difference) and target_diff > smallest_difference):
                smallest_difference = target_diff
            if target_diff > 0:
                left += 1
            else:
                right -= 1
    return target_sum - smallest_difference


def main():
    print(triplet_sum_close_to_target([-2, 0, 1, 2], 2))
    print(triplet_sum_close_to_target([-3, -1, 1, 2], 1))
    print(triplet_sum_close_to_target([1, 0, 1, 1], 100))


if __name__ == "__main__":
    main()
