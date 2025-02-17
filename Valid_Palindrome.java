class Solution {
    public boolean isPalindrome(String s) {
        // Convert to lowercase and remove non-alphanumeric characters
        String cleaned = s.toLowerCase().replaceAll("[^a-z0-9]", "");
        
        // Initialize two pointers, one at the start and one at the end
        int left = 0;
        int right = cleaned.length() - 1;
        
        // Compare characters from the start and end, moving towards the center
        while (left < right) {
            if (cleaned.charAt(left) != cleaned.charAt(right)) {
                return false;
            }
            left++;
            right--;
        }
        
        // If we reach this point, the string is a palindrome
        return true;
    }
}
