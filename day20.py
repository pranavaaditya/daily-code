""" You are given two 2D integer arrays nums1 and nums2.

nums1[i] = [idi, vali] indicate that the number with the id idi has a value equal to vali.
nums2[i] = [idi, vali] indicate that the number with the id idi has a value equal to vali.
Each array contains unique ids and is sorted in ascending order by id.

Merge the two arrays into one array that is sorted in ascending order by id, respecting the following conditions:

Only ids that appear in at least one of the two arrays should be included in the resulting array.
Each id should be included only once and its value should be the sum of the values of this id in the two arrays. If the id does not exist in one of the two arrays then its value in that array is considered to be 0.
Return the resulting array. The returned array must be sorted in ascending order by id.

 

Example 1:

Input: nums1 = [[1,2],[2,3],[4,5]], nums2 = [[1,4],[3,2],[4,1]]
Output: [[1,6],[2,3],[3,2],[4,6]]
Explanation: The resulting array contains the following:
- id = 1, the value of this id is 2 + 4 = 6.
- id = 2, the value of this id is 3.
- id = 3, the value of this id is 2.
- id = 4, the value of this id is 5 + 1 = 6.
Example 2:

Input: nums1 = [[2,4],[3,6],[5,5]], nums2 = [[1,3],[4,3]]
Output: [[1,3],[2,4],[3,6],[4,3],[5,5]]
Explanation: There are no common ids, so we just include each id with its value in the resulting list.
 

"""
class Solution:
    def mergeArrays(self, nums1, nums2):
        i, j = 0, 0
        merged = []

        while i < len(nums1) and j < len(nums2):
            if nums1[i][0] < nums2[j][0]:  # If nums1's id is smaller, add it
                merged.append(nums1[i])
                i += 1
            elif nums1[i][0] > nums2[j][0]:  # If nums2's id is smaller, add it
                merged.append(nums2[j])
                j += 1
            else:  # If IDs are the same, sum values
                merged.append([nums1[i][0], nums1[i][1] + nums2[j][1]])
                i += 1
                j += 1

        # Add remaining elements from either list
        while i < len(nums1):
            merged.append(nums1[i])
            i += 1
        while j < len(nums2):
            merged.append(nums2[j])
            j += 1

        return merged

# Example Usage
solution = Solution()

nums1 = [[1,2],[2,3],[4,5]]
nums2 = [[1,4],[3,2],[4,1]]
print(solution.mergeArrays(nums1, nums2))  # Output: [[1,6],[2,3],[3,2],[4,6]]

nums1 = [[2,4],[3,6],[5,5]]
nums2 = [[1,3],[4,3]]
print(solution.mergeArrays(nums1, nums2))  # Output: [[1,3],[2,4],[3,6],[4,3],[5,5]]

