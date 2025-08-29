t = int(input().strip())
results = []
for _ in range(t):
    n, m = map(int, input().split())
    result = (n * m + 1) // 2
    results.append(str(result))

print("\n".join(results))