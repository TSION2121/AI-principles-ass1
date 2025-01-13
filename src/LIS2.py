def length_of_LIS(arr):
    if not arr:
        return 0

    # Initialize an empty list to store the longest increasing subsequence
    lis = []

    for num in arr:
        # If lis is empty or num is greater than the last element in lis, append it
        if len(lis) == 0 or num > lis[-1]:
            lis.append(num)


    return len(lis), lis

# Taking input from the user
user_input = input("Enter the array elements separated by spaces: ")
arr = list(map(int, user_input.split()))

length, lis_array = length_of_LIS(arr)
print("Length of the Longest Increasing Subsequence is:", length)
print("The array is:", lis_array)
