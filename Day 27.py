def main():
    n = int(input().strip())
    for b in range(n//7, -1, -1):
        remainder = n - 7*b
        if remainder % 4 == 0:
            a = remainder // 4
            print('4'*a + '7'*b)
            return
    print(-1)

if __name__ == "__main__":
    main()