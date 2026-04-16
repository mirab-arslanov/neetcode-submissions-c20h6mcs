class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for word in strs:
            lets = [0] * 26
            for let in word:
                lets[ord(let) - ord('a')] += 1
            dic[tuple(lets)].append(word)
        return list(dic.values())