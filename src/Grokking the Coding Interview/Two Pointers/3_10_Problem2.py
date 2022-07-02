# Given two strings containing backspaces (identified by the character ‘#’), check if the two strings are equal.

# Example 1:

# Input: str1="xy#z", str2="xzz#"
# Output: true
# Explanation: After applying backspaces the strings become "xz" and "xz" respectively.
# Example 2:

# Input: str1="xy#z", str2="xyz#"
# Output: false
# Explanation: After applying backspaces the strings become "xz" and "xy" respectively.
# Example 3:

# Input: str1="xp#", str2="xyz##"
# Output: true
# Explanation: After applying backspaces the strings become "x" and "x" respectively.
# In "xyz##", the first '#' removes the character 'z' and the second '#' removes the character 'y'.
# Example 4:

# Input: str1="xywrrmp", str2="xywrrmu#p"
# Output: true
# Explanation: After applying backspaces the strings become "xywrrmp" and "xywrrmp" respectively.

def backspace_compare(str1, str2):
    index1 = len(str1) - 1
    index2 = len(str2) - 1
    while (index1 >= 0 or index2 >= 0):
        idx1 = get_next_char(str1, index1)
        idx2 = get_next_char(str2, index2)
        if idx1 < 0 and idx2 < 0:
            return True
        if idx1 < 0 or idx2 < 0:
            return False
        if str1[idx1] != str2[idx2]:
            return False
        index1 = idx1 - 1
        index2 = idx2 - 1
    return True


def get_next_char(str, index):
    backspace_count = 0
    while(index >= 0):
        if str[index] == "#":
            backspace_count += 1
        elif backspace_count > 0:
            backspace_count -= 1
        else:
            break
        index -= 1
    return index


def main():
    print(backspace_compare("xy#z", "xzz#"))
    print(backspace_compare("xy#z", "xyz#"))
    print(backspace_compare("xp#", "xyz##"))
    print(backspace_compare("xywrrmp", "xywrrmu#p"))


if __name__ == "__main__":
    main()
