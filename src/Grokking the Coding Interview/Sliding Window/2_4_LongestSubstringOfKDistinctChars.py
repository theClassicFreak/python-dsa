# Given a string, find the length of the longest substring in it
# with no more than K distinct characters.

# Example 1:

# Input: String = "araaci", K = 2
# Output: 4
# Explanation: The longest substring
# with no more than '2' distinct characters is "araa".
# Example 2:

# Input: String = "araaci", K = 1
# Output: 2
# Explanation: The longest substring
# with no more than '1' distinct characters is "aa".
# Example 3:

# Input: String = "cbbebi", K = 3
# Output: 5
# Explanation: The longest substrings
# with no more than '3' distinct characters are "cbbeb" & "bbebi".

def longest_substring_with_k_distinct(str, k):
    char_map = {}
    window_start = 0
    window_end = 0
    max_length = 0
    for window_end in range(0, len(str)):
        if str[window_end] in char_map:
            char_map[str[window_end]] += 1
        else:
            char_map[str[window_end]] = 1
        while(len(char_map) > k):
            char_map[str[window_start]] -= 1
            if char_map[str[window_start]] == 0:
                del char_map[str[window_start]]
            window_start += 1
        max_length = max(max_length, window_end - window_start + 1)
    return(max_length)


def main():
    print(longest_substring_with_k_distinct('araaci', 2))
    print(longest_substring_with_k_distinct('araaci', 1))
    print(longest_substring_with_k_distinct('cbbebi', 3))


if __name__ == "__main__":
    main()
