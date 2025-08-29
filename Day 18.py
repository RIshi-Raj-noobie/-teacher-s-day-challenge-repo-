def main():
    n = int(input().strip())
    arr = list(map(int, input().split()))

    max_val = max(arr)
    min_val = min(arr)

    # Find the first occurrence of max_val
    max_index = 0
    for i in range(n):
        if arr[i] == max_val:
            max_index = i
            break

    # Find the last occurrence of min_val
    min_index = n - 1
    for i in range(n - 1, -1, -1):
        if arr[i] == min_val:
            min_index = i
            break

    if max_index > min_index:
        result = max_index + (n - 1 - min_index) - 1
    else:
        result = max_index + (n - 1 - min_index)

    print(result)


if __name__ == "__main__":
    main()