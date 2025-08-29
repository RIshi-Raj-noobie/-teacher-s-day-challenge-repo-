def main():
    data = list(map(int, input().split()))
    n, k, l, c, d, p, nl, np = data
    total_drink = k * l
    total_slices = c * d
    toasts_drink = total_drink // (n * nl)
    toasts_slices = total_slices // n
    toasts_salt = p // (n * np)
    result = min(toasts_drink, toasts_slices, toasts_salt)
    print(result)

if __name__ == "__main__":
    main()