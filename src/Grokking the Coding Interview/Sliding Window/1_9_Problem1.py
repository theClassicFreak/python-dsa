# Permutation in a String (hard) #
# Given a string and a pattern, find out if the string contains any permutation of the pattern.

# Permutation is defined as the re-arranging of the characters of the string. For example, “abc” has the following six permutations:

# abc
# acb
# bac
# bca
# cab
# cba
# If a string has ‘n’ distinct characters it will have n!n! permutations.

# Example 1:

# Input: String="oidbcaf", Pattern="abc"
# Output: true
# Explanation: The string contains "bca" which is a permutation of the given pattern.
# Example 2:

# Input: String="odicf", Pattern="dc"
# Output: false
# Explanation: No permutation of the pattern is present in the given string as a substring.
# Example 3:

# Input: String="bcdxabcdy", Pattern="bcdyabcdx"
# Output: true
# Explanation: Both the string and the pattern are a permutation of each other.
# Example 4:

# Input: String="aaacb", Pattern="abc"
# Output: true
# Explanation: The string contains "acb" which is a permutation of the given pattern.

def permutations_in_string(str, substr):
    window_start, window_end, matched = 0, 0, 0
    substr_char_map = {}

    for i in range(0, len(substr)):
        if substr[i] not in substr_char_map:
            substr_char_map[substr[i]] = 0
        substr_char_map[substr[i]] += 1

    for window_end in range(0, len(str)):
        if str[window_end] in substr_char_map:
            substr_char_map[str[window_end]] -= 1
            if substr_char_map[str[window_end]] == 0:
                matched += 1
        if matched == len(substr_char_map):
            return True

        if window_end >= len(substr) - 1:
            if str[window_start] in substr_char_map:
                if substr_char_map[str[window_start]] == 0:
                    matched -= 1
                substr_char_map[str[window_start]] += 1
            window_start += 1

    return False


def main():
    print(permutations_in_string("oidbcaf", "abc"))
    print(permutations_in_string("odicf", "dc"))
    print(permutations_in_string("bcdxabcdy", "bcdxabcdy"))
    print(permutations_in_string("aaacb", "abc"))
    print(permutations_in_string("coab", "abc"))


if __name__ == "__main__":
    main()
