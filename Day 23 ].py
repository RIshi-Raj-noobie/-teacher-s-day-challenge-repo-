s = input().strip()
n = len(s)
# The number of distinct photobooks is (number of distinct positions to insert) * 26 minus duplicates.
# Actually, we can insert at n+1 positions, and for each position we can insert any of 26 letters.
# But if inserting the same letter at the same relative position as an existing one, it might duplicate?
# However, the problem is: we have a string s. We can insert one letter at any position (before first, between any two, after last). So there are (n+1) * 26 possibilities.
# But we need to subtract the duplicates. However, note: if the same string can be formed by multiple insertions, we count it only once.

# Alternatively, we can generate all possible insertions and use a set to count distinct ones.
# Since n is at most 20, the total possibilities are (21 * 26) = 546, which is manageable.

distinct = set()
for i in range(len(s) + 1):
    for c in 'abcdefghijklmnopqrstuvwxyz':
        new_str = s[:i] + c + s[i:]
        distinct.add(new_str)

print(len(distinct))