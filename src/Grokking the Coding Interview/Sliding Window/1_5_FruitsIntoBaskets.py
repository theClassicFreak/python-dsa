# Given an array of characters where each character represents a fruit tree, you are given two baskets and your goal is to put maximum number of fruits in each basket. The only restriction is that each basket can have only one type of fruit.

# You can start with any tree, but once you have started you can’t skip a tree. You will pick one fruit from each tree until you cannot, i.e., you will stop when you have to pick from a third fruit type.

# Write a function to return the maximum number of fruits in both the baskets.

# Example 1:

# Input: Fruit = ['A', 'B', 'C', 'A', 'C']
# Output: 3
# Explanation: We can put 2 'C' in one basket and one 'A' in the other from the subarray['C', 'A', 'C']
# Example 2:

# Input: Fruit = ['A', 'B', 'C', 'B', 'B', 'C']
# Output: 5
# Explanation: We can put 3 'B' in one basket and two 'C' in the other basket.
# This can be done if we start with the second letter: ['B', 'C', 'B', 'B', 'C']

def fruits_into_baskets(arr):
    window_start = 0
    window_end = 0
    max_count = 0
    char_map = {}
    for window_end in range(0, len(arr)):
        if arr[window_end] in char_map:
            char_map[arr[window_end]] += 1
        else:
            char_map[arr[window_end]] = 1
        while(len(char_map) > 2):
            char_map[arr[window_start]] -= 1
            if char_map[arr[window_start]] == 0:
                del char_map[arr[window_start]]
            window_start += 1
        max_count = max(max_count, window_end - window_start + 1)
    return max_count


def main():
    print(fruits_into_baskets(['A', 'B', 'C', 'A', 'C']))
    print(fruits_into_baskets(['A', 'B', 'C', 'B', 'B', 'C']))
    print(fruits_into_baskets(['A', 'B', 'C', 'A', 'B', 'C']))


if __name__ == "__main__":
    main()
