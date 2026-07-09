class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false; //base case, can't be true unless both are the same length
        }
        int[] track = new int[26]; //build alphabet
        for (int i = 0; i < s.length(); i++) {
            track[s.charAt(i)-'a']++;
            track[t.charAt(i)-'a']--; 
        }
        for (int j : track) {
            if (j != 0) {return false;}
        }
        return true;
    }
}
