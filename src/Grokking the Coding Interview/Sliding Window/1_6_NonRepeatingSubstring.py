# Given a string, find the length of the longest substring which has no repeating characters.

# Example 1:

# Input: String="aabccbb"
# Output: 3
# Explanation: The longest substring without any repeating characters is "abc".
# Example 2:

# Input: String="abbbb"
# Output: 2
# Explanation: The longest substring without any repeating characters is "ab".
# Example 3:

# Input: String="abccde"
# Output: 3
# Explanation: Longest substrings without any repeating characters are "abc" & "cde".

def non_repeat_substring(str):
    window_start = 0
    window_end = 0
    max_length = 0
    char_map_index = {}
    for window_end in range(0, len(str)):
        if str[window_end] in char_map_index:
            window_start = max(window_start, char_map_index[str[window_end]]+1)
        char_map_index[str[window_end]] = window_end
        max_length = max(max_length, window_end - window_start + 1)
    return max_length


def main():
    print(non_repeat_substring('aabccbb'))
    print(non_repeat_substring('abbbb'))
    print(non_repeat_substring('abccde'))


if __name__ == "__main__":
    main()
