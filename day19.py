
#Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
#You must implement a solution with a linear runtime complexity and use only constant extra space.

#Example 1:
#Input: nums = [2,2,1]
#Output: 1
#Example 2:
#Input: nums = [4,1,2,1,2]
#Output: 4
#Example 3:
#Input: nums = [1]
#Output: 1


class Solution:
    def singleNumber(self, nums):
        result = 0
        
        for num in nums:
            result ^= num  # XOR all numbers
        return result

# Example Usage
solution = Solution()
print(solution.singleNumber([2,2,1]))  # Output: 1
print(solution.singleNumber([4,1,2,1,2]))  # Output: 4
print(solution.singleNumber([1]))  # Output: 1
