def main():
    s = input().strip()
    i = 0
    n = len(s)
    valid = True
    while i < n:
        if s[i] == '1':
            # Check for "14" or "144"
            if i+1 < n and s[i+1] == '4':
                if i+2 < n and s[i+2] == '4':
                    i += 3
                else:
                    i += 2
            else:
                i += 1
        else:
            valid = False
            break
    print("YES" if valid else "NO")

if __name__ == "__main__":
    main()