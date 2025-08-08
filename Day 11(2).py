s = input().strip()
lower = sum(1 for c in s if c.islower())
upper = len(s) - lower
print(s.upper() if upper > lower else s.lower())