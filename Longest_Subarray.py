def longest_subarray(arr, k):
    max_len = 0
    for i in range(len(arr)):
        total = 0
        for j in range(i, len(arr)):
            total += arr[j]
            if total == k:
                max_len = max(max_len, j - i + 1)
    return max_len

arr = list(input("Enter array elements: ")).split()
k = int(input("Enter k: "))

print("Longest subarray length =", longest_subarray(arr, k))
