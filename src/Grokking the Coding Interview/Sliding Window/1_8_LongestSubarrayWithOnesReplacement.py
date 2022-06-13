# Problem Statement
# Given an array containing 0s and 1s, if you are allowed to replace no more than ‘k’ 0s with 1s, find the length of the longest contiguous subarray having all 1s.

# Example 1:

# Input: Array = [0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], k = 2
# Output: 6
# Explanation: Replace the '0' at index 5 and 8 to have the longest contiguous subarray of 1s having length 6.
# Example 2:

# Input: Array = [0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], k = 3
# Output: 9
# Explanation: Replace the '0' at index 6, 9, and 10 to have the longest contiguous subarray of 1s having length 9.

def longest_subarray_replacement(arr, k):
    window_start = 0
    window_end = 0
    max_length = 0
    char_map_index = {0: 0, 1: 0}
    for window_end in range(0, len(arr)):
        char_map_index[arr[window_end]] += 1
        while(char_map_index[0] > k):
            char_map_index[arr[window_start]] -= 1
            window_start += 1
        max_length = max(max_length, window_end - window_start + 1)
    return max_length


def main():
    print(longest_subarray_replacement([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2))
    print(longest_subarray_replacement(
        [0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 3))


if __name__ == "__main__":
    main()
