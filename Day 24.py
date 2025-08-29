def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    queue = list(enumerate(a, start=1))
    last = None
    while queue:
        idx, candies = queue.pop(0)
        if candies > m:
            queue.append((idx, candies - m))
        else:
            last = idx
    print(last)

if __name__ == "__main__":
    main()