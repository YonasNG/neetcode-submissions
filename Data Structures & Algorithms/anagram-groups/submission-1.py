class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = defaultdict(list)

        for s in strs:
            sorted_word = "".join(sorted(s))
            output[sorted_word].append(s)
        return list(output.values())