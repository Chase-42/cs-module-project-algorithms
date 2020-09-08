'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    y = len(arr)-1
    for x in range(0, len(arr) -1):
        while arr[x] == 0:
            if arr[y] != 0: 
                # Swap em
                arr[x], arr[y] = arr[y], arr[x]
                # If x == y, return 
            elif x ==y:
                return arr
            else: 
                # move y index to right
                y -=1
    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")