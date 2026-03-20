from typing import List

class Solution:
    """
    https://leetcode.cn/problems/group-anagrams-lcci
    """
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        dic = defaultdict(list)
        for s in strs:
            array = [0] * 26
            for c in s:
                idx = ord(c) - ord('a') 
                array[idx] += 1

            key = tuple(array)
            dic[key].append(s)

        result = [dic[key] for key in dic]
        return result
        

if __name__   == "__main__":
    s = Solution()
    strings = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(s.groupAnagrams(strings))