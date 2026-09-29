#include <vector>
#include <unordered_map>

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int, int> complementMap; //instantiating key value pair map
        for (int i = 0; i < nums.size(); i++) {
            int complement = target - nums[i]; //find the complement

            if (complementMap.find(complement) != complementMap.end()) {
                return {complementMap[complement], i};
            }

            complementMap[nums[i]] = i; //store key value pair
        }
        return {}; //return empty vector if no solution exists
    }
};
