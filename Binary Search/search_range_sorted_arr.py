'''
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
 

Constraints:

0 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
nums is a non decreasing array.
-10^9 <= target <= 10^9
'''

def first(arr, low, high, x, n) : 
    if(high >= low) : 
        mid = low + (high - low) // 2
        if( ( mid == 0 or x > arr[mid - 1]) and arr[mid] == x) : 
            return mid 
        elif(x > arr[mid]) : 
            return first(arr, (mid + 1), high, x, n) 
        else : 
            return first(arr, low, (mid - 1), x, n) 
    return -1
  
def last(arr, low, high, x, n) :
    if (high >= low) : 
        mid = low + (high - low) // 2
        if (( mid == n - 1 or x < arr[mid + 1]) and arr[mid] == x) : 
            return mid 
        elif (x < arr[mid]) : 
            return last(arr, low, (mid - 1), x, n) 
        else : 
            return last(arr, (mid + 1), high, x, n) 
              
    return -1
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1,-1]
        if len(nums) == 1 and nums[0] == target:
            return [0,0]
        x = first(nums,0,len(nums)-1,target,len(nums))
        y = last(nums,0,len(nums)-1,target,len(nums))
        return [x,y]