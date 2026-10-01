class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashtable = {}
        for i in nums:
            if i in hashtable:
                hashtable[i] += 1
            else:
                hashtable[i] = 1

        for num in hashtable:
            if hashtable[num] > 1:
                return True
        return False