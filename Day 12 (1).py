s = input().strip()
distinct = len(set(s))
print("CHAT WITH HER!" if distinct % 2 == 0 else "IGNORE HIM!")