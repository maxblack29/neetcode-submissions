class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {  
        Map<String, List<String>> tracker = new HashMap<>(); //Don't know if this is correct
        //first, find the anagrams
        for (String s : strs) {
            char[] charArray = s.toCharArray();
            Arrays.sort(charArray); //sorts char array alphabetically
            String key = String.valueOf(charArray); //convert back to string

            List<String> curGroup = tracker.getOrDefault(key, new ArrayList<>()); 

            curGroup.add(s); 

            tracker.put(key, curGroup); 
        }
        return new ArrayList<>(tracker.values()); 
    }
}
