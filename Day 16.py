def main():
    n, t = map(int, input().split())
    s = list(input().strip())

    for _ in range(t):
        # Create a copy of the current state to check conditions
        temp = s[:]
        for i in range(n - 1):
            if temp[i] == 'B' and temp[i + 1] == 'G':
                s[i], s[i + 1] = s[i + 1], s[i]

    print(''.join(s))


if __name__ == "__main__":
    main()