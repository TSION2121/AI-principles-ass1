def length_of_LIS(arr):
    if not arr:
        return 0

    # Initialize the dp array with 1s
    dp = [1] * len(arr)

    # Fill the dp array
    for i in range(1, len(arr)):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    # The length of the longest increasing subsequence
    return max(dp)

# Example usage
arr = [10, 22, 9, 33, 21, 50, 41, 60, 80]
print(length_of_LIS(arr))  # Output should be 6
