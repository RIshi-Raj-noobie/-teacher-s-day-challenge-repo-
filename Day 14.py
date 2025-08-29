s = input().strip()
# Replace all occurrences of "WUB" with a space
original = s.replace("WUB", " ")
# Collapse multiple spaces into one and strip leading/trailing spaces
words = original.split()
# Join the words with a space
result = " ".join(words)
print(result)