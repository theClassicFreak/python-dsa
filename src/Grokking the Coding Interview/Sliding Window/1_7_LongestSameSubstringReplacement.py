# Given a string with lowercase letters only, if you are allowed to replace no more than ‘k’ letters with any letter, find the length of the longest substring having the same letters after replacement.

# Example 1:

# Input: String="aabccbb", k=2
# Output: 5
# Explanation: Replace the two 'c' with 'b' to have a longest repeating substring "bbbbb".
# Example 2:

# Input: String="abbcb", k=1
# Output: 4
# Explanation: Replace the 'c' with 'b' to have a longest repeating substring "bbbb".
# Example 3:

# Input: String="abccde", k=1
# Output: 3
# Explanation: Replace the 'b' or 'd' with 'c' to have the longest repeating substring "ccc".


def longest_substring_replacement(str, k):
    window_start = 0
    window_end = 0
    max_length = 0
    max_letter_repeat_count = 0
    char_map_index = {}
    for window_end in range(0, len(str)):
        if str[window_end] not in char_map_index:
            char_map_index[str[window_end]] = 0
        char_map_index[str[window_end]] += 1
        max_letter_repeat_count = max(
            max_letter_repeat_count, char_map_index[str[window_end]])
        if((window_end - window_start + 1) - max_letter_repeat_count > k):
            char_map_index[str[window_start]] -= 1
            window_start += 1
        max_length = max(max_length, window_end - window_start + 1)
    return max_length


def main():
    print(longest_substring_replacement('aabccbb', 2))
    print(longest_substring_replacement('abbcb', 1))
    print(longest_substring_replacement('abccde', 1))


if __name__ == "__main__":
    main()
