class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        // initialize hashSet
        unordered_set<int> hashSet;
        // left and right pointer at position 0
        // ans - track max length of window (substring)
        int l = 0, r = 0, ans = 0;
        // right pointer going through every character
        while (r < s.length()) {
            // if character is not in hashSet
            if (!hashSet.count(s[r])) {
                // add it 
                hashSet.insert(s[r]);
                // update window size 
                ans = max(ans, r - l + 1);
                // shift right pointer
                r++;
            } else {
                // delete character at left pointer position
                hashSet.erase(s[l]);
                //shift left pointer
                l++;
            }
        }
        // return result
        return ans;
    }    
};
