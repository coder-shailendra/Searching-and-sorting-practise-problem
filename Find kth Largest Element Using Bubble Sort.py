def kth_largest(arr, k):
    n = len(arr)
    if k > n or k <= 0:
        return "Invalid value of k"
    for i in range(k):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr[n - k]
numbers = [7, 2, 9, 4, 1, 5]
k = int(input("enter the kth term:"))
result = kth_largest(numbers, k)
print(result)
