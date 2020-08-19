'''
Given a sorted array arr, two integers k and x, find the k closest elements to x in the array. The result should also be sorted in ascending order. If there is a tie, the smaller elements are always preferred.

 

Example 1:

Input: arr = [1,2,3,4,5], k = 4, x = 3
Output: [1,2,3,4]
Example 2:

Input: arr = [1,2,3,4,5], k = 4, x = -1
Output: [1,2,3,4]
 

Constraints:

1 <= k <= arr.length
1 <= arr.length <= 10^4
Absolute value of elements in the array and x will not exceed 104
'''

import collections

class Solution(object):
    def findClosestElements(self, arr, k, x): 
        def binary_search(a, target):
            low, high = 0, len(a) -1 
            while low != high:
                middle = (low + high)//2
                if a[middle] > target:
                    high = middle
                elif a[middle] < target:
                    low = middle + 1
                else:
                    return middle
            return low
        
        index = binary_search(arr, x)
        answers = collections.deque()
        low, high = index -1 , index
        while k > 0:
            if low < 0 :
                answers.extend(arr[high:high+k])
                break
            elif high > len(arr) - 1:
                answers.extendleft(arr[low:low-k:-1])
                break
            elif ((x - arr[low]) > (arr[high] -x)):
                answers.append(arr[high])
                high += 1
            else:
                answers.appendleft(arr[low])
                low -= 1
            k -= 1
        return list(answers)