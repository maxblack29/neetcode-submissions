class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        tracker = {} # empty hash mpa to hold vals
        for i in range(len(strs)):
            k = ''.join(sorted(strs[i])) # create alphabetically sorted string
            if k not in tracker:
                tracker[k] = [] # create empty tracker list
            tracker[k].append(strs[i]) # add string to the array stored from key k in tracker
        return list(tracker.values()) #returns list of just the values (not keys)