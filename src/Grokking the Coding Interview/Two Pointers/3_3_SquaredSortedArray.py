# Given a sorted array, create a new array containing squares of all the number of the input array in the sorted order.

# Example 1:

# Input: [-2, -1, 0, 2, 3]
# Output: [0, 1, 4, 4, 9]
# Example 2:

# Input: [-3, -1, 0, 1, 2]
# Output: [0 1 1 4 9]

def make_squares(arr):
    squares = [0 for x in range(len(arr))]
    left = 0
    right = len(arr) - 1
    arr_index = len(arr) - 1
    while(left <= right):
        sq_left = arr[left] * arr[left]
        sq_right = arr[right] * arr[right]
        if sq_left > sq_right:
            squares[arr_index] = sq_left
            left += 1
        else:
            squares[arr_index] = sq_right
            right -= 1
        arr_index -= 1
    return squares


def main():
    print(make_squares([-2, -1, 0, 2, 3]))
    print(make_squares([-3, -1, 0, 1, 2]))


if __name__ == "__main__":
    main()
