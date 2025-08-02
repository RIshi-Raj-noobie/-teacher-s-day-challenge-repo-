from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs):
        anagram_groups = defaultdict(list)

        for s in strs:
            count = [0] * 26  # for each letter a-z
            for c in s:
                count[ord(c) - ord('a')] += 1
            # Convert the list to a tuple to use as a key
            key = tuple(count)
            anagram_groups[key].append(s)

        return list(anagram_groups.values())