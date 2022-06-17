# Smallest Window containing Substring (hard) #
# Given a string and a pattern, find the smallest substring in the given string which has all the characters of the given pattern.

# Example 1:

# Input: String = "aabdec", Pattern = "abc"
# Output: "abdec"
# Explanation: The smallest substring having all characters of the pattern is "abdec"
# Example 2:

# Input: String = "abdabca", Pattern = "abc"
# Output: "abc"
# Explanation: The smallest substring having all characters of the pattern is "abc".
# Example 3:

# Input: String = "adcad", Pattern = "abc"
# Output: ""
# Explanation: No substring in the given string has all characters of the pattern.

def find_smallest_substring(str, pattern):
    window_start, window_end, matched = 0, 0, 0
    char_map = {}
    min_start, min_end = -1, -1
    min_length = len(str)
    for chr in pattern:
        if chr not in char_map:
            char_map[chr] = 0
        char_map[chr] += 1

    for window_end in range(len(str)):
        if str[window_end] in char_map:
            char_map[str[window_end]] -= 1
            if char_map[str[window_end]] == 0:
                matched += 1
        while(matched == len(char_map)):
            if str[window_start] in char_map:
                if char_map[str[window_start]] == 0:
                    matched -= 1
                char_map[str[window_start]] += 1
            if (window_end - window_start + 1) <= min_length:
                min_length = window_end - window_start + 1
                min_start = window_start
                min_end = window_end
            window_start += 1
    if min_length > len(str):
        return ""
    return str[min_start:min_end+1]


def main():
    print(find_smallest_substring("xyzyzx", "abc"))
    print(find_smallest_substring("aabdec", "abc"))
    print(find_smallest_substring("abdabca", "abc"))
    print(find_smallest_substring("adcad", "abc"))
    print(find_smallest_substring("aa", "aa"))
    print(find_smallest_substring("aaxbczabcy", "abc"))


if __name__ == "__main__":
    main()
