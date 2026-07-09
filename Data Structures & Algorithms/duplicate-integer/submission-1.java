//import java.util.HashSet;
//import java.util.Set; 
class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set<Integer> view = new HashSet<>(); 
        for (int i : nums) {
            if (view.contains(i)) {
                return true; 
            }
            view.add(i);
        }
        return false; 
    }
}