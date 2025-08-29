def main():
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        if n <= 30:
            print("NO")
        else:
            remainder = n - 30
            if remainder not in [6, 10, 14]:
                print("YES")
                print(f"6 10 14 {remainder}")
            else:
                print("YES")
                print(f"6 10 15 {n-31}")

if __name__ == "__main__":
    main()