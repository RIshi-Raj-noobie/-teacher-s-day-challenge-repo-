n = input().strip()
lucky_digits = {'4', '7'}
count = sum(1 for ch in n if ch in lucky_digits)

if count == 0:
    print("NO")
else:
    is_lucky = True
    for ch in str(count):
        if ch not in lucky_digits:
            is_lucky = False
            break
    print("YES" if is_lucky else "NO")