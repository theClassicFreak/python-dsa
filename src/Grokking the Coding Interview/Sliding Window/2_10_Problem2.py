# Given a string and a pattern, find all anagrams of the pattern in the given string.

# Anagram is actually a Permutation of a string. For example, “abc” has the following six anagrams:

# abc
# acb
# bac
# bca
# cab
# cba
# Write a function to return a list of starting indices of the anagrams of the pattern in the given string.

# Example 1:

# Input: String = "ppqp", Pattern = "pq"
# Output: [1, 2]
# Explanation: The two anagrams of the pattern in the given string are "pq" and "qp".
# Example 2:

# Input: String = "abbcabc", Pattern = "abc"
# Output: [2, 3, 4]
# Explanation: The string contains "acb" which is a permutation of the given pattern.

def find_string_anagrams(str, pattern):
    window_start, window_end, matched = 0, 0, 0
    pattern_char_map = {}
    starting_indices = []

    for i in pattern:
        if i not in pattern_char_map:
            pattern_char_map[i] = 0
        pattern_char_map[i] += 1

    for window_end in range(len(str)):
        if str[window_end] in pattern_char_map:
            pattern_char_map[str[window_end]] -= 1
            if pattern_char_map[str[window_end]] == 0:
                matched += 1
        if matched == len(pattern_char_map):
            starting_indices.append(window_start)
        if window_end >= len(pattern) - 1:
            if str[window_start] in pattern_char_map:
                if pattern_char_map[str[window_start]] == 0:
                    matched -= 1
                pattern_char_map[str[window_start]] += 1
            window_start += 1

    return starting_indices


def main():
    print(find_string_anagrams("ppqp", "pq"))
    print(find_string_anagrams("abbcabc", "abc"))
    print(find_string_anagrams("cbaebabacd", "abc"))


if __name__ == "__main__":
    main()
