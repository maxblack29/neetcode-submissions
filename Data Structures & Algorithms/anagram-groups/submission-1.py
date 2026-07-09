from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        track = defaultdict(list)
        for s in strs:
            sort = tuple(sorted(s))
            track[sort].append(s)
        return list(track.values())