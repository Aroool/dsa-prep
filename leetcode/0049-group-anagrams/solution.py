from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)

        for s in strs:
            key = "".join(sorted(s))
            anagram_map[key].append(s)
        return list(anagram_map.values())



        # visited = [False] * len(strs)
        # result = []

        # for i in range(len(strs)):
        #     if visited[i]:
        #         continue
        #     group = [strs[i]]
        #     visited[i] = True
        #     key = sorted(strs[i])
        #     for j in range(i+1, len(strs)):
        #         if not visited[j] and sorted(strs[j]) == key:
        #             group.append(strs[j])
        #             visited[j] = True
        #     result.append(group)
        # return result
