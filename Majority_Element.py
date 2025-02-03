class Solution:
    def majorityElement(self, nums):
        count = 0
        candidate = None
        for num in nums:
            if count == 0:
                candidate, count = num, 1
            else:
                count += 1 if num == candidate else -1
        return candidate